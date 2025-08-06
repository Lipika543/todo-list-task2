TASK_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task '{task}' added.\n")

def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks yet.\n")
    else:
        print("📝 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to remove: "))
        removed = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"❌ Task '{removed}' removed.\n")
    except (IndexError, ValueError):
        print("⚠️ Invalid task number.\n")

def main():
    tasks = load_tasks()

    while True:
        print("📋 TO-DO LIST MENU")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
