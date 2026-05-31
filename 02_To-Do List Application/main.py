# To-Do list Application
print("Welcome to the To-Do list")

tasks = []

while True:
    print("\n====To-Do List====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")

    choice = input("Enter Choice: \n")
    if choice == "1":
        task = input("Enter Task: ")
        tasks.append(task)
        print("Task added sucessfully")

    elif choice == "2":
        for i, task in enumerate(tasks, start=1):
            print(i, task)

    elif choice == "3":
        num = int(input("Enter your task number: "))
        tasks[num - 1] = "[✔]" + tasks[num - 1]

    elif choice == "4":
        print("I hope you completed all task on time!\nGoodbye")
        break

    else:
        print("Invalid choice!")

