# app/routes/ui/py

from flask import Blueprint, render_template, request, redirect, url_for, current_app

"""
📚 UI ROUTES - WEB INTERFACE FOR TASK MANAGEMENT:

🎯 BLUEPRINT PATTERN:
This file uses Flask's Blueprint pattern to organize related routes.
Blueprints allow modular application structure and URL prefixing.

🔄 ROUTE PATTERNS DEMONSTRATED:
- GET routes: Display forms and data (task_form, show_tasks, task_report)
- POST routes: Process form submissions (create_task, delete_task, complete_task)
- Redirects: Post-Redirect-Get pattern for form handling
- URL parameters: Dynamic routes with <int:task_id>

💡 VALIDATION STRATEGY:
- Frontend: HTML 'required' attribute (user experience)
- Backend: Python validation (security and data integrity)
- Error handling: Display messages to users

👉 FOR STUDENTS / GROUP PROJECT HINT:
- This file currently performs simple server-side validation in the controller (`ui.py`) for clarity in the lab.
- In larger or collaborative projects it's better to centralize validation in the service layer (e.g. `TaskService`) or a shared schema:
  - Pros: single source of truth, reuse across UI and API, easier to test, clearer contract for business rules.
  - Suggestion: have controllers perform only minimal syntactic checks (trim/required) and let `TaskService` raise a semantic `ValidationError` for domain rules.
  - Adopt a custom `ValidationError`, update tests and controllers to catch that class rather than broad `Exception`.

🔗 BACKEND INTEGRATION:
All routes use current_app.task_service for business logic,
maintaining separation between web layer and business layer.
"""

ui_bp = Blueprint("ui", __name__)

@ui_bp.route("/")
def home():
    """
    Home page - redirect to task form.
    
    📚 STUDENT NOTE: This demonstrates a common web pattern where
    the root URL redirects to a more specific landing page.
    """
    return redirect(url_for("ui.task_submit"))

@ui_bp.route("/tasks/new", methods=["GET", "POST"])
def task_submit():
    """
    Create new task - handles both form display and submission.
    
    📚 VALIDATION LAYERS EXPLAINED:
    1. Frontend (HTML): 'required' attribute prevents empty submission
    2. Backend (Python): Server-side validation ensures data integrity
    3. Business Logic: TaskService.add_task() may have additional rules
    
    This demonstrates the "defense in depth" security principle.
    """
    error = None
    
    if request.method == "POST":
        # Extract and clean form data
        title = request.form.get("title", "").strip()
        priority = request.form.get("priority", "")
        description = request.form.get("description", "").strip()
        
        # Server-side validation - NEVER trust frontend alone!
        if not title:
            error = "Title is required."
        elif not priority:
            error = "Priority is required."
        else:
            try:
                # Call business logic layer
                current_app.task_service.add_task(title, priority, description)
                # Post-Redirect-Get pattern: redirect after successful POST
                return redirect(url_for("ui.show_tasks"))
            except Exception as e:
                # Handle business logic errors (e.g., validation in TaskService)
                error = f"Error creating task: {str(e)}"
    
    # GET request or POST with validation error
    return render_template("add_task.html", error=error)

@ui_bp.route("/tasks", methods=["GET"])
def show_tasks():
    """
    Display all tasks in a list view.
    
    📚 DATA FLOW: 
    1. Route calls TaskService.get_all_tasks()
    2. Service returns list of Task objects converted to dicts either ascending or descending sort
    3. Template receives 'tasks' variable for rendering
    4. Jinja2 loops through tasks with {% for task in tasks %}
    
    This demonstrates the MVC pattern: Route (Controller) → Service (Model) → Template (View)
    """

    # Get the current sort order from frontend
    sort_order = request.args.get('sort')

    if sort_order == 'Descending':
        # When the order is descending, reverse the order (high to low)
        tasks = current_app.task_service.get_all_tasks_sorted(reverse=True)
        sort_order_toggle = 'Ascending'
    else:
        # Default order is ascending (low to high)
        tasks = current_app.task_service.get_all_tasks_sorted()
        sort_order_toggle = 'Descending'

    return render_template("task_list.html", tasks=tasks, sort_order={'sort_order': sort_order_toggle})

@ui_bp.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    """
    Delete a specific task by ID.
    
    📚 TECHNICAL CONCEPTS:
    - URL Parameters: <int:task_id> automatically converts to integer
    - HTTP Method: POST for destructive actions (RESTful design)
    - Error Handling: TaskService will raise exception if task not found
    - Redirect: Post-Redirect-Get pattern prevents duplicate submissions
    """
    try:
        current_app.task_service.delete_task(task_id)
    except Exception as e:
        # In production, you'd handle this error gracefully
        # For now, let the error bubble up for debugging
        pass
    return redirect(url_for("ui.show_tasks"))

@ui_bp.route("/tasks/<int:task_id>/complete", methods=["POST"])
def complete_task(task_id):
    """
    Mark a specific task as completed.
    
    📚 BUSINESS LOGIC:
    - Calls TaskService.complete_task() which handles the state change
    - Service layer ensures business rules are followed
    - Database/storage layer persists the change
    - UI layer just orchestrates the flow
    
    This separation of concerns makes the code maintainable and testable.
    """
    try:
        current_app.task_service.complete_task(task_id)
    except Exception as e:
        # In production, you'd show user-friendly error messages
        pass
    return redirect(url_for("ui.show_tasks"))

@ui_bp.route("/tasks/report")
def task_report():
    """
    Generate and display task analytics/statistics.
    
    📚 DATA ANALYTICS PATTERN:
    This route demonstrates a common business intelligence pattern:
    1. Fetch raw data (all tasks)
    2. Apply aggregation logic (count totals, completed, remaining)
    3. Pass calculated metrics to presentation layer
    
    🔍 PYTHON TECHNIQUES:
    - List comprehension: [t for t in tasks if t.get("completed", False)]
    - Safe dictionary access: t.get("completed", False) handles missing keys
    - Mathematical operations: remaining = total - completed
    
    📊 REAL-WORLD APPLICATIONS:
    - Dashboard KPIs in business applications
    - Analytics reporting in web applications
    - Data aggregation for charts and visualizations
    """
    tasks = current_app.task_service.get_tasks()
    total = len(tasks)
    completed = len([t for t in tasks if t.get("completed", False)])
    remaining = total - completed
    return render_template("report.html", total=total, completed=completed, remaining=remaining)
