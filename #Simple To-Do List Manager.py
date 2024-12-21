#Simple To-Do List Manager
def to_do_list_manager():
    to_do_list = []
    print("Welcome to the To-Do List Manager!")
    print("Options: [1] Add Task [2] View Tasks [3] Remove Task [4] Exit")

    while True:
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a new task: ")
            to_do_list.append(task)
            print(f"Task '{task}' added to your list!")
        elif choice == "2":
            if not to_do_list:
                print("Your to-do list is empty.")
            else:
                print("Here are your tasks:")
                for i, task in enumerate(to_do_list,start=1):
                    print(f"{i}. {task}")
        elif choice == "3":
            if not to_do_list:
                print("Your to-do list is empty. Nothing to remove.")
            else:
                print("Here are your tasks:")
                for i, task in enumerate(to_do_list, start=1):
                    print (f"{i}.{task}")
                try:
                    task_number = int(input("Enter the number of the task to remove: "))
                    if 1 <= task_number <= len(to_do_list):
                        removed_task = to_do_list.pop(task_number - 1)
                        print(f"Task '{removed_task} removed from your list!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose between [1], [2], [3], or [4]. ")

#Run the To-Do List Manager
to_do_list_manager()