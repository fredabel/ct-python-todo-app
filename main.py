
tasks = []
todo_list = ["Add Task","View Task","Delete Task","Quit"]
warning_msg = ["Please follow the instruction. Try again! ","It seems you're not sure what to do. ","Please call 123456 if you need help."]
return_err_msg = "Multiple invalid attempts. Returning to the main menu."
exit_err_msg = "Multiple invalid attempts. Good Bye!!!"
error_limit = 3


def display_menu():
    print("\nSelect Todo List:")
    for i, todo in enumerate(todo_list,1):
        print(f"{i}. {todo}")
    print("\n")
    
# Add a task
def add_task():
    errors = 0
    while True:
        try:
            task = input("Enter the name of your task: ")
            if len(task) < 3:
                errors += 1
                print(f"Task name must be at least '3 characters'. Attempts {errors} of 3.\n")
                if errors == error_limit:
                    print(f"\n{return_err_msg}")
                    return False
            else:
                tasks.append(task)
                print(f"\nYou have successfully added the '{task}' task!\n")
                ask_to_view()
                return False
        except ValueError as e:
            print(f"{return_err_msg}\n")
            return False
        
#Ask to view         
def ask_to_view():
    errors = 0
    while True:
        try:
            view = input("Do you want to view the tasks list? (yes/no): ")
            print("\n")
            if view.lower() == "yes":
                errors = 0
                view_tasks()
                return False
            elif view.lower() == "no":
                errors = 0
                return False
            else:
                errors += 1
                print(f"\nInvalid input. Attempt {errors} of 3.\n")
            if errors == 3:
                print(f"\n{return_err_msg}\n")
                return False
        except ValueError as e:
            print(f"{return_err_msg}\n")
            return False
            
# View 
def view_tasks():
    if not tasks:
        print("\nThere are currently no tasks!\n")
        ask_add_task()
        return False
    else:
        print("\n*** TASKS LIST ***")   
        for i, task in enumerate(tasks,1):
            print(f"{i}. {task.upper()}") 
        print("******************")
       
# Delete
def delete_task():
    if not tasks:
        print("\nThere are no tasks to delete!\n")
        ask_add_task()
        return False
        
    errors = 0
    while True:
        try:
            view_tasks() 
            idx = input("Enter the task number you want to delete: ")
            
            idx = int(idx) - 1
            if 0 <= idx < len(tasks):
                removed = tasks.pop(idx)
                print(f"\nTask '{removed}' was deleted successfully!\n") 
                return False
            else:
                errors += 1
                print(f"\nMake sure you type the task number. Attempt {errors} of 3.\n")
                if errors == error_limit:
                    print(f"\n{return_err_msg}\n")
                    return False
        except ValueError as e:
            errors += 1
            print(f"\nInvalid input. Attempt {errors} of 3.\n")
            if errors == 3:
                print(f"\n{return_err_msg}\n")
                return False
        

# Ask to add a task
def ask_add_task():
    errors = 0
    while True:
        add = input("Would you like to add a task? (yes/no): ")
        if add.lower() == "yes":
            errors = 0
            add_task()
            return False
        elif add.lower() == "no":
            errors = 0
            return False
        else:
            errors += 1
            print(f"\nInvalid input. Attempt {errors} of 3.\n")
            if errors == error_limit:
                print(f"\n{return_err_msg}\n")
                return False
            
# Main function
def main():
    errors = 0
    print("\nWelcome to my Todo Application List")
    while True:
        try:
            display_menu()
            choice = input("What would you like to do? (Type the number): ")
            print("\n")
            choice = int(choice) 
            if choice == 1:
                add_task()
                errors = 0
            elif choice == 2:
                errors = 0
                view_task = view_tasks()
            elif choice == 3:
                errors = 0
                del_task = delete_task()
            elif choice == 4:
                print("Goodbye!\n")
                break
            else:
                print("\nInvalid choice. Please try again.")
        except ValueError as e:
            # print(f"\nAn error occurred: {e}")
            errors += 1
            print(f"\nInvalid input. Attempt {errors} of 3.")
            print(f"{warning_msg[errors - 1]}\n")
            if errors == error_limit:
                print(f"{exit_err_msg}\n")
                break
             
main()
    