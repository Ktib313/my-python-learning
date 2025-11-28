
todo_list = []

def add_task():
    user_prompt = input("Enter a task:\n")
    todo_list.append(user_prompt)


def show_task(todos):
    for item in todos:
        print(f"{todos.index(item) + 1}. {item} [ ]")


def delete_task(todos):
    task = input("What task do you want to delete: ")
    todos.remove(task)

def save_tasks(todos):
    with open("tasks.txt", "w") as f:
        for item in todos:
            f.write(item + '\n')


def show_menu():
    print("1. Add task")
    print("2. Show Tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Quit")

def load_tasks():
    filepath = 'tasks.txt'
    try:
        with open(filepath, 'r') as f:
            tasks = f.read()
            print(tasks)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

while True:
    print("Welcome to MoTask")
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        show_task(todo_list)
    elif choice == "4":
        delete_task(todo_list)
    elif choice == "5":
        save_tasks(todo_list)
        break

