class Task:
    """Domain model for a Task, with id, title, description, and completed status."""
    def __init__(self, task_id: int, title: str, priority: str, description: str = "", completed: bool = False) -> None:
        self.id: int = task_id
        self.title: str = title
        self.priority: str = priority
        self.description: str = description
        self.completed: bool = completed

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def to_dict(self) -> dict[str, object]:
        """Serialize Task object to a dictionary (for JSON serialization)."""
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "description": self.description,
            "completed": self.completed
        }


    def get_priority_value(self):
        priority = self.priority

        # This is hardcoded, though could be done through enumerates
        if  priority == 'low':
            return 0
        elif priority == 'medium':
            return 1
        elif priority == 'high':
            return 2
        else:
            raise ValueError("Priority must be low, medium, or high")

    def __eq__(self, other):
        if isinstance(other, Task):
            if other.get_priority_value() == self.get_priority_value():
                return True
        return False


    def __lt__(self, other):
        return self.get_priority_value() < other.get_priority_value()


    def __gt__(self, other):
        return self.get_priority_value() > other.get_priority_value()