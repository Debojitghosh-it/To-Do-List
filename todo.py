def task():
    tasks = []

    print("--- Welcome To The Application ---")

    total_task = int(input("Enter number of tasks = "))

    for i in range(1, total_task + 1):
        task_name = input(f"Enter Task {i} = ")
        tasks.append(task_name)

    print("\nToday's Tasks:")
    for t in tasks:
        print("-", t)

    while True:
        print("\nChoose Operation")
        operation = input("1-Add\n2-Update\n3-Delete\n4-View\n5-Exit\n")

        if operation == "1":
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task '{add}' has been added.")

        elif operation == "2":
            updated_val = input("Enter the task you want to update = ")
            if updated_val in tasks:
                new_task = input("Enter new task = ")
                index = tasks.index(updated_val)
                tasks[index] = new_task
                print("Task updated successfully.")
            else:
                print("Task not found.")

        elif operation == "3":
            delete_val = input("Enter task you want to delete = ")
            if delete_val in tasks:
                tasks.remove(delete_val)
                print("Task deleted successfully.")
            else:
                print("Task not found.")

        elif operation == "4":
            if len(tasks) == 0:
                print("No tasks available.")
            else:
                print("Your Tasks:")
                for t in tasks:
                    print("-", t)

        elif operation == "5":
            print("Closing the program...")
            break

        else:
            print("Invalid option. Please try again.")

task()