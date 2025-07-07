#tasks as list which will contain all the tasks(to-do) as a dictionary itself.
tasks = []


#defining the tasks
def view_tasks() :
      print("TASKS:")
      if not tasks:
            print ("no tasks yet.")
      else :
            for index, task in enumerate (tasks, start = 1) :
                  if task["done"] :
                        print(f"{index}. {task['task']}✅")
                  else :
                        print(f"{index}. {task['task']}❌")

def add_tasks() :
      add = input("enter your task\n")
      new_tasks = {
            "task" : add,
            "done" : False
      }
      tasks.append (new_tasks)

      print("task added successfully")

def mark_tasks() :
      view_tasks() #call the task list
      task_number_done = int( input("enter the task number you finished\n"))
      
      try :
            index = task_number_done - 1
            if 0 <= index < len(tasks) :  #check whether the number is one from the list
                  tasks[index] ["done"] = True
                  print("Task marked as done! ")
            else :
                  print ("invalid number")
      except ValueError :
            print("please enter a number")
            

def delete_tasks() :
      view_tasks() #call the task list
      task_to_delete = int( input("enter the task number to delete\n"))

      try :
            index = task_to_delete - 1
            if 0 <= index < len(tasks) :  #check whether the number is one from the list
                  delete = tasks.pop(index)
                  print("task removed successfully.")
            else :
                  print ("invalid number")
      except ValueError :
            print("please enter a number")



#menu loop
while True:
        print("\n= = = TO-DO LIST MENU = = =")
        print("1) View Tasks")
        print("2) Add Tasks")
        print("3) Mark Tasks")
        print("4) Delete Tasks")
        print("5) Exit")
        choice = input("Enter your choice\n")
        if choice == "1":
              view_tasks() #call the task list
        elif choice == "2":
              add_tasks() #call the func to add task
        elif choice == "3":
              mark_tasks() #call the func to mark the tasks completed
        elif choice == "4":
              delete_tasks() 
        elif choice == "5":
              print("existing\nbye bye\nreturn soon!!")
              break 
        else :
              print("enter a valid choice")
        
