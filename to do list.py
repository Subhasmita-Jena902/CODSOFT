tasks = []

def add_task():
    title = input("Enter task title: ")
    tasks.append({"title": title, "completed": False})
    print("Task added!")

def show_tasks():
    for i, task in enumerate(tasks):
        status = "✔️" if task["completed"] else "❌"
        print(f"{i + 1}. {task['title']} [{status}]")

def mark_complete():
    show_tasks()
    index = int(input("Enter task number to mark as done: ")) - 1
    tasks[index]["completed"] = True
    print("Marked as completed!")

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Mark Completed\n4. Exit")
    choice = input("Choose: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        mark_complete()
    elif choice == '4':
        break
