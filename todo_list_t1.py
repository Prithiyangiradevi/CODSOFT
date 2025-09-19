# CODSOFT Internship - Task 1 
# Author: Prithiyangira Devi
# Project: To-Do List with Save/Load Feature

import os

# File to store tasks
FILE_NAME = "tasks.txt"

# Load tasks from file if exists
def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                task, status = line.strip().split(" | ")
                tasks.append({"title": task, "status": status})
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(f"{task['title']} | {task['status']}\n")

# Display menu
def show_options():
    print("\n===== MY TO-DO LIST =====")
    print("1. Show all tasks")
    print("2. Add a new task")
    print("3. Mark a task as done")
    print("4. Edit a task")
    print("5. Delete a task")
    print("6. Exit")

# Show all tasks
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet. Start adding some!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['title']} - [{task['status']}]")

# Add a new task
def add_task(tasks):
    title = input("\nEnter task name: ")
    tasks.append({"title": title, "status": "Not Done"})
    print(f"Task '{title}' added!")

# Mark task as done
def mark_done(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            num = int(input("\nEnter task number to mark done: "))
            if 1 <= num <= len(tasks):
                tasks[num-1]["status"] = "Done"
                print("Task marked as Done ✅")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

# Edit task title
def edit_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            num = int(input("\nEnter task number to edit: "))
            if 1 <= num <= len(tasks):
                new_title = input("Enter new task name: ")
                tasks[num-1]["title"] = new_title
                print("Task updated!")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            num = int(input("\nEnter task number to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num-1)
                print(f"Task '{removed['title']}' deleted.")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

# Main program
def main():
    tasks = load_tasks()

    while True:
        show_options()
        choice = input("\nChoose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("\nTasks saved! Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
