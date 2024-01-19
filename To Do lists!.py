#To Do lists!
#Stephanie and Hanan

#Creates a todo list for a user
def toDolistMaker():
    print("Welcome to your To-Do List!")
    print("Please choose what to do with your list: (Type in a number bewteen 1 - 5)")
    print("1. Add task \n2. View List \n3. Mark task as complete \n4. Remove a task \n5. Clear all tasks \n6. Print number of tasks available \n7. Alphabetize tasks \n8. Quit")
    option = int(input("What would you like to do with your list?"))
    toDo = []
    #Adds a task to the list 
    def addTask():
        newTask = input("What would you like to add to your list?")
        toDo.append(newTask)

    #Allows someone to view the list 
    def viewTask():
        print(toDo)
#Aloows user to mark a task as completed 
    def completeTask():
        done = int(input("Please provide the number printed to complete the item in the list"))
        toDo.pop(done)
        toDo.append("☑")
        print("This task is marked as complete")

    #Removes a task from the list 
    def removeTask():
        ans = int(input("Please provide the number printed to remove the item in the list"))
        toDo.pop(ans)
        print("This task was removed")

    #Clears All items from the list 
    def clearTask():
        toDo.clear
        print("This list has been cleared!")

    #Prints number of items in the list
    def numTask():
        print(len(toDo) + " items in this list!")
        
    #Sort the list alphabethically 
    def abcTask():
        toDo.sort()
        print(toDo)

    
    if option == 1:
        addTask()
            
    if option == 2:
        viewTask()

    if option == 3:
        print(toDo)
        taskNum = input("What task do you want to mark as complete?")
        u = toDo.index(taskNum)
        print(u)
        completeTask()

    if option == 4:
        taskNumber = input("What task do you want to remove?")
        i = toDo.index(taskNumber)
        print(i)
        removeTask()
    
    if option == 5:
        clearTask()

    if option == 6:
        numTask()
    
    if option == 7:
        abcTask()

    if option == 8:
        quit()
    
#Allows for the function to continue infinetly till the user quits 
while True:
    toDolistMaker()


       
