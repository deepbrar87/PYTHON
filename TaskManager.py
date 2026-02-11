import os

#file to store tasks

file_name = "task.txt"

def load_task():
    tasks = {}
    if os.path.exists(file_name):
        with open(file_name,'r') as file:
            for line in file:
                task_id, title, status = line.strip().split(' | ')
                tasks[int(task_id)] = {"title" : title, 'Status' : status}
    return tasks

#save task to file

def save_tasks(tasks):
    with open(file_name,'w') as file:
        for task_id, task in tasks.items():
            file.write(f'{task_id} | {task['title']} | {task['status']}\n')

# Add a new task

def add_task(tasks):
    title = input('Enter task title')
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "status":"incomplete"}
    print(f"Task '{title}' added")
    
#view all task

def view_tasks(tasks):
    if not tasks:
        print("no task available")
    else:
        for task_id, task in tasks.items():
            print(f'{task_id} | {task['title']} - {task['status']}')
            
            
# Mark task as complete

def mark_task_complete(tasks):
    task_id = int(input("Enter task id to mark as complete: ")  )
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"Task '{tasks[task_id]['title']}' marked as complete")
    else:
        print("Task ID not found") 
        
# Delete a task
def delete_task(tasks):
    task_id = int(input("Enter task id to delete: "))
    if task_id in tasks:
        print(f"Task '{tasks[task_id]['title']}' deleted")
        del tasks[task_id]
    else:
        print("Task ID not found")
# Main function to run the task manager
def main():
    tasks = load_task()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
            save_tasks(tasks)
        elif choice == '4':
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")
            
if __name__ == "__main__":
    main()

    
            
