tasks = []

while True:
    print("\n--- TO-DO APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    # Safe input
    try:
        choice = int(input("Enter choice: "))
    except:
        print("Please enter a valid number")
        continue

    # Add Task
    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    # View Tasks
    elif choice == 2:
        if not tasks:
            print("No tasks available")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks):
                print(i + 1, ".", task)

    # Delete Task
    elif choice == 3:
        if not tasks:
            print("No tasks to delete")
        else:
            try:
                num = int(input("Enter task number to delete: "))
                if 0 < num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"Task '{removed}' deleted!")
                else:
                    print("Invalid number")
            except:
                print("Please enter a valid number")

    # Exit
    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
