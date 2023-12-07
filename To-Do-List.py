tasks = []  # Empty list to store tasks

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        task = tasks.pop(task_index - 1)
        print(f"Task '{task}' removed!")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n1. Add task\n2. View tasks\n3. Remove task\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            task_index = int(input("Enter task number to remove: "))
            remove_task(task_index)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
