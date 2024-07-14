import json

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        try:
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()

    def edit_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task
            self.save_tasks()

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)

def main():
    manager = TaskManager()
    
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Edit Task")
        print("4. List Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            manager.add_task(task)
        elif choice == '2':
            index = int(input("Enter the task number to remove: ")) - 1
            manager.remove_task(index)
        elif choice == '3':
            index = int(input("Enter the task number to edit: ")) - 1
            new_task = input("Enter the new task: ")
            manager.edit_task(index, new_task)
        elif choice == '4':
            manager.list_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
