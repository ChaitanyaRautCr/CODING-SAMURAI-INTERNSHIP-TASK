import os

tasks = []

# Load tasks from file
def load_tasks():
    global tasks
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]

# Save tasks to file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Add task
def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks()
    print("Task added successfully!")

# View tasks
def view_tasks():
    print("\n===== YOUR TASKS =====")
    
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Delete task
def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_num = int(input("Enter task number to delete: "))

        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks()
            print(f"'{removed_task}' deleted successfully!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")

# Main Program
load_tasks()

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Thank you for using To-Do List Application!")
        break

    else:
        print("Invalid choice! Please try again.")