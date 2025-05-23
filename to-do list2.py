import datetime
from plyer import notification

tasks = []

def add_task():
    """Add a new task."""
    task = input("Enter task: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({"task": task, "due_date": due_date, "completed": False, "reminder_set": False})
    print("Task added!")

def view_tasks():
    """Display all tasks."""
    if not tasks:
        print("No tasks in the list!")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Not Completed"
            reminder = "Set" if task["reminder_set"] else "Not Set"
            print(f"{i+1}. {task['task']} (Due: {task['due_date']}) - {status} - Reminder: {reminder}")

def complete_task():
    """Mark a task as completed."""
    if not tasks:
        print("No tasks to complete!")
    else:
        view_tasks()
        try:
            index = int(input("Enter the number of task the to complete: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index]["completed"] = True
                print("Task completed!")
            else:
                print("Invalid index!")
        except ValueError:
            print("Invalid input!")

def remove_task():
    """Remove a task."""
    if not tasks:
        print("No tasks to remove!")
    else:
        view_tasks()
        try:
            index = int(input("Enter the number of the task to remove: ")) - 1
            if 0 <= index < len(tasks):
                del tasks[index]
                print("Task removed!")
            else:
                print("Invalid index!")
        except ValueError:
            print("Invalid input!")

def fix_date():
    """Fix due date of a task."""
    if not tasks:
        print("No tasks to fix date for!")
    else:
        view_tasks()
        try:
            index = int(input("Enter index of task to fix date for: ")) - 1
            if 0 <= index < len(tasks):
                new_date = input("Enter new due date (YYYY-MM-DD): ")
                tasks[index]["due_date"] = new_date
                print("Date fixed!")
            else:
                print("Invalid index!")
        except ValueError:
            print("Invalid input!")

def set_reminder():
    """Set reminder for a task."""
    if not tasks:
        print("No tasks to set reminder for!")
    else:
        view_tasks()
        try:
            index = int(input("Enter the number of the task to set reminder for: ")) - 1
            if 0 <= index < len(tasks):
                task_name = tasks[index]["task"]
                due_date = tasks[index]["due_date"]
                notification.notify(title="Task Reminder", message=f"Task'{task_name}' is due on {due_date}!",timeout=10)
                tasks[index]["reminder_set"]=True
                print("Reminder set!")
            else:
                print("Invalid Index!")
        except ValueError:
            print("Invalid Index!")

def exit_app():
    """Save tasks and exit the app."""
    print("Exiting app...")

while True:
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Remove Task")
    print("5. Fix Date")
    print("6. Set Reminder")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        fix_date()
    elif choice == "6":
        set_reminder()
    elif choice == "7":
        exit_app()
        break
    else:
        print("Invalid choice!")

