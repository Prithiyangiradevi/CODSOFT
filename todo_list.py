# CODSOFT - Task 1: To-Do List
# Author: Your Name
# Internship: Python Programming

# A simple command-line To-Do List app

# Store tasks in a list (each task is a dictionary)
tasks = []

def show_menu():
    print("\n====== TO-DO LIST MENU ======")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['task']} - [{task['status']}]")

def add_task():
    task_name = input("\nEnter task name: ")
    tasks.append({"task": task_name, "status": "Not Done"})
    print(f"Task '{task_name}' added successfully!")

def update_task():
    view_tasks()
    if tasks:
        try:
            task_no = int(input("\nEnter task number to update: "))
            if 1 <= task_no <= len(tasks):
                print("1. Mark as Done")
                print("2. Edit Task Name")
                choice = input("Choose an option: ")
                
                if choice == "1":
                    tasks[task_no - 1]["status"] = "Done"
                    print("Task marked as Done!")
                elif choice == "2":
                    new_name = input("Enter new task name: ")
                    tasks[task_no - 1]["task"] = new_name
                    print("Task updated successfully!")
                else:
                    print("Invalid option.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_no = int(input("\nEnter task number to delete: "))
            if 1 <= task_no <= len(tasks):
                removed = tasks.pop(task_no - 1)
                print(f"Task '{removed['task']}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main program loop
while True:
    show_menu()
    option = input("\nChoose an option: ")

    if option == "1":
        view_tasks()
    elif option == "2":
        add_task()
    elif option == "3":
        update_task()
    elif option == "4":
        delete_task()
    elif option == "5":
        print("\nThank you for using To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
