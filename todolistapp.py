print("-------TASK MANAGER--------")
task_num = int(input("Enter no. of tasks you want: "))
alltask = []
for i in range(1,task_num + 1):
    task = str(input("Enter task: "))
    alltask.append(task)
print("Your today's tasks: " , alltask)

while True:
    print("1. Add")
    print("2. Update")
    print("3. Delete")
    print("4. View")
    print("5. Exit/stop")
    choice = int(input("Enter choice: "))
    if (choice==1):
     new_task = str(input("Enter the task you want to add: "))
     alltask.append(new_task)
     print("Task successfully added....  ")
    elif (choice==2):
     update_task = str(input("Enter the task you want to update: "))
     idx = alltask.index(update_task)
     update2_task = str(input("Enter new task: "))
     alltask[idx] = update2_task
     print("Task successfully update.... ")
    elif (choice==3):
     del_task = str(input("Enter task you want to delete: "))
     try:
         alltask.remove(del_task)
         print("Task deleted successfully.... ")
     except ValueError:
         print("This task doesn't exist. ")
    elif (choice==4):
     print("Your today's task: " , alltask)
    elif (choice==5):
       print("Successfully exited.... ")
       break