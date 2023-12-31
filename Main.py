tasks = []

def addTask():
    task = input ("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added to the list")

def listTasks():
    if not tasks:
        print("There are no tasks currently")
    else:
        print("Current Tasks:")
    for index, task in enumerate(tasks):
        print(f"Tasks #{index}. {task}")
        
def deleteTask():
    listTasks()
    try: 
        taskToDelete = int(input("Enter the number: "))
        if taskToDelete < len(tasks) and taskToDelete >=0:
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed")
        else: 
            print(f"Task #{taskToDelete} was not found")
    except: 
        print("Invalid input.") 

if __name__ == "__main__":
###Create a loop to run the app
    print("Welcome to my first To Do List app")
iterations = 0
while iterations < 5 :
    print("\n")
    print("Please select on of the options")
    print("-------------------------------")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. List tasks")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if (choice == "1"):
        addTask()
    elif (choice == "2"):
        deleteTask()
    elif (choice == "3"):
        listTasks()
    elif (choice == "4"):
        break
    else:
        print("Invalid input. Please try again")

print("Goodbye!")

iterations += 1 #increment the counter after each run
if iterations >=5:
    print("Maximum iterations reached")
