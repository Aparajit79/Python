tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Delete a Task")
    print("4. Exit")
    

    try:
        play = int(input("Enter a number: "))
    except ValueError:
        print("Please enter a valid number (1-4).")
        continue

    match play:
        case 1:
            add = input("Enter a task to add: ").strip()
            if add:
                tasks.append(add)
                print(f"'{add}' added successfully!")
            else:
                print("Task cannot be empty.")
                
        case 2:
            if not tasks:
                print("Your list is empty.")
            else:
                print("\nYOUR TASKS:")
                
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                    
        case 3:
            if not tasks:
                print("No tasks to delete.")
                continue
                
    
            print("\nYOUR TASKS:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
                
            try:
                task_num = int(input("Enter the task number to remove: "))
               
                removed_task = tasks.pop(task_num - 1)
                print(f"'{removed_task}' removed successfully!")
            except (ValueError, IndexError):
          
                print("Invalid task number.")
                
        case 4:
            print("Goodbye!")
            break
            
        case _:
            print("Invalid option. Please choose a number between 1 and 4.")
