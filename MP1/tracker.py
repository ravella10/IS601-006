from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy() # don't delete this
    #id - pr457, date - 2/20/23
    # message dictionary which contains different messages for different outputs
    message = {'success':'Task added successfully','name':'Adding task failed due to missing name', 'description':'Adding task failed due to missing description','due':'Adding task failed due to missing due date','dueformat':'Adding task failed due to wrong due date format'}
    message_key = 'success'
    # update lastActivity with the current datetime value
    if name:
        task['name'] = name
        if description:
            task['description'] = description
            if due:
                try:
                    task['due'] = str_to_datetime(due)
                    task['lastActivity'] = str(datetime.now())
                    tasks.append(task)
                except:
                    message_key = 'dueformat'
            else:
                message_key = 'due'
        else:
            message_key = 'description'
    else:
        message_key = 'name'
        # set the name, description, and due date (all must be provided)
        # due date must match one of the formats mentioned in str_to_datetime()
        # add the new task to the tasks list
    # output a message confirming the new task was added or if the addition was rejected due to missing data
    print(message[message_key])
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    save()

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # show the existing value of each property where the TODOs are marked in the text of the inputs (replace the TODO related text)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    #id - pr457, date - 2/20/23
    if index>=len(tasks):
        print("Index out of bounds. Please give a index between 0 and ",len(tasks))
        return 0
    else:
        task = tasks[index]
    name = input(f"What's the name of this task? {task['name']} \n").strip()
    desc = input(f"What's a brief descriptions of this task? {task['description']}\n").strip()
    due = input(f"When is this task due (format: m/d/y H:M:S) {task['due']} \n").strip()
    update_task(index, name=name, description=desc, due=due)

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    # find the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    #id - pr457, date - 2/20/23
    if index>=len(tasks):
        print("Index out of bounds. Please give a index between 0 and ",len(tasks))
        return 0
    else:
        task = tasks[index]
    flag = False
    # update incoming task data if it's provided (if it's not provided use the original task property value)
    if name:
        task['name'] = name
        flag = True
    if description:
        task['description'] = description
        flag = True
    if due:
        task['due'] = due
        flag = True
    # update lastActivity with the current datetime value
    task['lastActivity'] = str(datetime.now())
    # output that the task was updated if any items were changed, otherwise mention task was not updated
    if flag:
        tasks[index] = task
        print("Task updated successfully")
    else:
        print("Task was not updated. No changes to save")
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    save()

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # if it's not done, record the current datetime as the value
    # if it is done, print a message saying it's already completed
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    #id - pr457, date - 2/20/23
    #checks if the index is out of bounds, prints an error message if it is or else the task is retrieved by index
    #If the retrieved task is not yet completed then assign current datetime or else print task is already completed
    if index>=len(tasks):
        print("Index out of bounds. Please give a index between 0 and ",len(tasks))
    else:
        task = tasks[index]
        if not task['done']:
            task['done'] = str(datetime.now())
            print("Marked as Done")
        else:
            print("Task's already completed!")
    save()

def view_task(index):
    """ View more info about a specific task fetch by index """
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # utilize the given print statement when a task is found
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    #id - pr457, date - 2/20/23
    #checks if the index is out of bounds, prints an error message if it is or else the task is retrieved by index and prints out the task
    if index>=len(tasks):
        print("Index out of bounds. Please give a index between 0 and ",len(tasks))
        return 0
    task = tasks[index]
    print(f"""
        [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
        Description: {task['description']} \n 
        Last Activity: {task['lastActivity']} \n
        Due: {task['due']}\n
        Completed: {task['done'] if task['done'] else '-'} \n
        """.replace('  ', ' '))


def delete_task(index):
    """ deletes a task from the tasks list by index """
    # delete/remove task from list by index
    # message should show if it was successful or not
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # make sure save() is still called last in this function
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    #id - pr457, date - 2/20/23
    #checks if the index is out of bounds, prints an error message if it is or else the task is retrieved by index
    if index>=len(tasks):
        print("Index out of bounds. Please give a index between 0 and ",len(tasks))
    else:
        # deletes the task with given index from tasks
        del tasks[index]
        print("Deleted task successfully")
    save()

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    # generate a list of tasks where the task is not done
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    #id - pr457, date - 2/20/23
    # list comprehension to rerieve all the tasks that are not done yet by checking if the value of 'done' key is false
    _tasks = [task for task in tasks if not task['done']]
    if len(_tasks) != 0:
        list_tasks(_tasks)
    else:
        print("No Incomplete Activities!")

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than now and that are not complete
    # pass that list into list_tasks()
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    #id - pr457, date - 2/20/23
    # list comprehension to retrieve all the tasks past due date by using if condition to compare the due datetime with current datetime
    _tasks = [task for task in tasks if str_to_datetime(task['due'])<datetime.now() and not task['done']]
    if len(_tasks) != 0:
        list_tasks(_tasks)
    else:
        print("No OverDue Tasks")
def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # get the days, hours, minutes, seconds between the due date and now
    # display the remaining time via print in a clear format showing days, hours, minutes, seconds
    # if the due date is in the past print out how many days, hours, minutes, seconds the task is over due (clearly note that it's over due, values should be positive)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    #id - pr457, date - 2/20/23
    #checks if the index is out of bounds, prints an error message if it is or else the task is retrieved by index
    if index>=len(tasks):
        print("Index out of bounds. Please give a index between 0 and ",len(tasks))
    else:
        task = tasks[index]
        #Compares the current datetime with task due and prints out the time remaining or past due by time
        if datetime.now()<str_to_datetime(task['due']):
            #print("Time remaining ", str_to_datetime(task['due']) - datetime.now())
            diff = str_to_datetime(task['due']) - datetime.now()
            seconds = diff.total_seconds()
            minutes, seconds = divmod(seconds, 60)
            hours, minutes = divmod(minutes, 60)
            days, hours = divmod(hours, 24)
            print(f"Time remaining {int(days)} days {int(hours)} hours {int(minutes)} minutes {int(seconds)} seconds ")
        else:
            # print("Past Due by", datetime.now() - str_to_datetime(task['due']))
            diff = datetime.now() - str_to_datetime(task['due'])
            seconds = diff.total_seconds()
            minutes, seconds = divmod(seconds, 60)
            hours, minutes = divmod(minutes, 60)
            days, hours = divmod(hours, 24)
            print(f"Past Due By {int(days)} days {int(hours)} hours {int(minutes)} minutes {int(seconds)} seconds ")

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()