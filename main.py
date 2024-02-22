# This is the Application title and tagline
print("Welcome to Quicky To-Do List")
print("Prepare your day and goals Using Quicky To-Do List\n")

# This is the dictionary that houses the tasks
todo_list = []


# This function adds a new entry into the To-Do List
def add_new_task(todo_list, todo_title, todo_description):
    todo_position = len(todo_list) + 1
    todo_entry = {"todo_position": todo_position, "title": todo_title, "description": todo_description}
    todo_list.append(todo_entry)

    return todo_list


# This function deletes a specific task by using its index in the dictionary
def delete_specific_task(todo_list, todo_position):
    if 0 < todo_position <= len(todo_list):
        todo_list.pop(todo_position - 1)
        print("You have successfully deleted To-Do Task Numbeer: ", todo_position)
        print("\n")
    else:
        print("Your Todo Task was not found.\n")


# This function shows all tasks you entered
def view_all_tasks(todo_list):
    if todo_list:
        for todo_position, todo_entry in enumerate(todo_list, start=1):
            print("TO-DO TASK NUMBER", todo_position)
            print("Title: ", todo_entry["title"])
            print("Description: ", todo_entry["description"])
            print("\n")
    else:
        print("No To-Do Tasks were found.\n")


# This function shows a specific task by using the index in the dictionary
def view_specific_task(todo_list, todo_position):
    if 0 < todo_position <= len(todo_list):
        todo_entry = todo_list[todo_position - 1]
        print("TO-DO TASK NUMBER", todo_entry["todo_position"])
        print("Title: ", todo_entry["title"])
        print("Description: ", todo_entry["description"])
        print("\n")
    else:
        print("Your To-Do Task was not found.\n")

# This function deletes all the tasks you entered
def delete_all_tasks(todo_list):
    todo_list.clear()
    print("All your Tasks have been deleted.")


# The while loop ensures the app is running after entering an option until you choose to exit
while True:
    # The Try-Except ensures user enters correct numerical character
    try:
        option_selection = int(input("Press 1 to Add New Task.\nPress 2 to View Specific Task\n"
                                     "Press 3 to View All Tasks\nPress 4 to Delete Specific Task\n"
                                     "Press 5 to Delete All Tasks\nPress 0 to Exit Application.\n"))

        # This option allows user to add new task
        if option_selection == 1:
            todo_title = input("Please Enter Title for Your Task: \n")
            todo_description = input("Please Enter Description of Your Task: \n")

            todo_list = add_new_task(todo_list, todo_title, todo_description)

        # This option allows user view a specific task. It also prevents errors if user enters wrong character
        elif option_selection == 2:
            while True:
                try:
                    todo_selection = int(input("Please select the To-Do Task number:\n"))
                    view_specific_task(todo_list, todo_selection)
                    break

                except ValueError:
                    print("You've entered a wrong character, please enter a numerical character.")

        # This option allows user to see all tasks that were entered.
        elif option_selection == 3:
            view_all_tasks(todo_list)

        # This option allows user  to delete specific task. It also prevents errors when user enters wrong character
        elif option_selection == 4:
            while True:
                try:
                    todo_selection = int(input("Please select the To-Do Task number:\n"))
                    delete_specific_task(todo_list, todo_selection)

                    break
                except ValueError:
                    print("You've entered a wrong character, please enter a numerical character.")

        # This option deletes all entered entries
        elif option_selection == 5:
            delete_all_tasks(todo_list)

        # This option deletes all tasks that were entered
        elif option_selection == 0:
            print("Thank You for using my application. Have a Good Day.\nExiting...")

            break

        # This is an error message when user enters the wrong option but is a numerical character
        else:
            print("You've entered an invalid option, please try again.")

    except ValueError:
        print("You've entered a wrong character, please enter a numerical character.")
