# Task Manager Program

# Initialize an empty list to store tasks
tasks = []

# Start an infinite loop for user interaction
while True:
    # Display menu options for user commands
    print("Options: add, view, delete, exit")
    command = input("Enter command: ")

    # Adding a new task
    if command == "add":
        task_description = input("Enter task description: ")
        if task_description:  # Check if not empty
            tasks.append(task_description)  # Add to tasks list
            print("Task added successfully.")
        else:
            print("Task cannot be empty.")

    # Viewing all current tasks
    elif command == "view":
        if not tasks:  # Check if the list is empty
            print("No tasks available.")
        else:
            for index, task in enumerate(tasks):
                print(f"{index + 1}: {task}")  # Display each task with its index

    # Deleting a specific task by index
    elif command == "delete":
        try:
            index_to_delete = int(input("Enter task number to delete: ")) - 1  # Convert to zero-based index
            if 0 <= index_to_delete < len(tasks):
                removed_task = tasks.pop(index_to_delete)  # Remove from list
                print(f"Task '{removed_task}' deleted successfully.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Please enter a valid number.")

    # Exiting the program
    elif command == "exit":
        break

# End of program