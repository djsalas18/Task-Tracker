# Task Priority Feature Documentation

Implemented By: Collin Geersen

### Description:

The task priority feature changes the underlying task data model to include the new parameter for priority 
(low, medium, or high). These changes are reflect throughout the class declarations and methods. Additionally,
route and ui changes were made to accommodate this change.

The feature also includes a sort function based on priority that can be used in the frontend to sort the tasks
from ascending or descending order.


## Changelog
- Updated sqlalchemy_task.py 
  - Added priority Column 
- Updated task.py 
  - Add priority to contructor and to_dict methods 
  - Adds get_priority_value method to get numberic value of priority 
  - Adds methods for eq, lt, and gt for sorting purposes 
- Updated database_task_repository.py 
  - Adds priority to abtract method add_task()
  - Adds priority to method load_tasks()
  - Adds priority to method save_tasks()
  - Adds priority to method add_task()
- Updated task_service.py 
  - Adds priority to init()
  - Adds get_all_tasks_sorted() function
- Updated tasks.py 
  - Adds priority data for add_task()
- Updated add_task.html 
  - Adds a select element to choose a priority level of a task
- Updated task_list.html 
  - Adds button that allows for sorting of tasks based on priority level 
  - Adds priority level to task sections
- Updated style.css 
  - Adds styling for select elements 
  - Adds styling for priority levels
- Updated ui.py 
  - Updated show_tasks() to include new get_all_tasks_sorted() function 
  - Updated show_tasks() to include a new data point tracking which sort function to use


## Future Improvements
- Could implement a separate priority class to abstract the value of low, medium, and high so it is not
hardcoded into the data model.