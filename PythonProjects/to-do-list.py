import os
import json
# Function to load tasks from a file
def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
        return tasks
    else:
        return []
# Function to save tasks to a file
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)
# Function to display the menu
def display_menu():
    print("\n===== To-Do List =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
# Function to view tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['title']} - {'Completed' if task['completed'] else 'Not Completed'}")
# Function to add a task
def add_task(tasks):
    title = input("Enter the task: ")
    tasks.append({"title": title, "completed": False})
    save_tasks(tasks)
    print("Task added successfully.")
# Function to mark a task as completed
def mark_completed(tasks):
    view_tasks(tasks)
    choice = int(input("Enter the task number to mark as completed: ")) 
    if 1 <= choice <= len(tasks):
        tasks[choice - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")
# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    choice = int(input("Enter the task number to delete: "))
    if 1 <= choice <= len(tasks):
        deleted_task = tasks.pop(choice - 1)
        save_tasks(tasks)
        print(f"Task '{deleted_task['title']}' deleted successfully.")
    else:
        print("Invalid task number.")
# Main function
def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()
