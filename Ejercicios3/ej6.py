tasks = []

def add_task():
    name = input("Enter the task description: ")
    task = {"name": name, "completed": False}
    tasks.append(task)
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks.")
        return
    print("\nTask List:")
    for i, task in enumerate(tasks):
        status = "✅ Completed" if task["completed"] else "❌ Pending"
        print(f"{i + 1}. {task['name']} - {status}")
    print()

def mark_completed():
    view_tasks()
    if not tasks:
        return
    try:
        number = int(input("Number of the task to mark as completed: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Number out of range.")
    except ValueError:
        print("Please, enter a valid number.")

def menu():
    while True:
        print("\n--- TASK MENU ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Exit")
        option = input("Select an option: ")

        if option == "1":
            add_task()
        elif option == "2":
            view_tasks()
        elif option == "3":
            mark_completed()
        elif option == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

menu()
