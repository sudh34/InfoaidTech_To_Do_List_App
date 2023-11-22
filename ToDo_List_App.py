import json

class Task:
    def __init__(self, title, description, status="Incomplete"):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"{self.title} - {self.description} - {self.status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        print(f"Task '{title}' added successfully.")

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task '{title}' deleted successfully.")
                return
        print(f"Task '{title}' not found.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    def save_tasks(self, filename="tasks.json"):
        with open(filename, "w") as file:
            task_list = [{"title": task.title, "description": task.description, "status": task.status} for task in self.tasks]
            json.dump(task_list, file)
        print("Tasks saved successfully.")

    def load_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "r") as file:
                task_list = json.load(file)
                self.tasks = [Task(task["title"], task["description"], task["status"]) for task in task_list]
            print("Tasks loaded successfully.")
        except FileNotFoundError:
            print("No saved tasks found.")

# Test the app
todo_list = ToDoList()

while True:
    print("\n===== To-Do List App =====")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Save Tasks")
    print("5. Load Tasks")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        todo_list.add_task(title, description)
    elif choice == "2":
        title = input("Enter task title to delete: ")
        todo_list.delete_task(title)
    elif choice == "3":
        todo_list.view_tasks()
    elif choice == "4":
        todo_list.save_tasks()
    elif choice == "5":
        todo_list.load_tasks()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
