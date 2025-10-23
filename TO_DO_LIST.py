print("Welcome to TO DO LIST.")
tasks_list = []

while True:
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Remove Task")
    print("4. EXIT")
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("❌ Please enter a valid number!")
        continue

    if choice == 1:
        num = int(input("How many tasks do you want to add (1-10): "))
        for i in range(num):
            task = input("Enter your task: ")
            tasks_list.append(task)
            print("✅ Task added!")

    elif choice == 2:
        if not tasks_list:
            print("📭 No tasks added!")
        else:
            print("\nYour task list:")
            print("-" * 30)
            for index, task in enumerate(tasks_list, start=1):
                print(f"{index}. {task}")
            print("-" * 30)

    elif choice == 3:
        if not tasks_list:
            print("📭 No tasks to remove!")
            continue
        remove = int(input("Which task do you want to remove: "))
        if 1 <= remove <= len(tasks_list):
            tasks_list.pop(remove - 1)
            print("🗑️ Task removed!")
        else:
            print("❌ Invalid task number!")

    elif choice == 4:
        print("👋 Exiting the TO DO List.")
        break

    else:
        print("❌ Invalid choice! Please select 1–4.")
