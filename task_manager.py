#=====importing libraries===========
import datetime

# Constants for file names
USER_FILE = "user.txt"
TASKS_FILE = "tasks.txt"

#====Login Section====
# Function to read user credentials from file
def read_user_credentials():
    """Reads user credentials from the user file."""
    user_credentials = {}
    with open(USER_FILE, "r") as user_file:
        for line in user_file:
            username, password = line.strip().split(', ')
            user_credentials[username] = password
    return user_credentials

# Function to write user credentials to file
def write_user_credentials(username, password):
    """Writes new user credentials to the user file."""
    with open(USER_FILE, "a") as user_file:
        user_file.write(f"\n{username}, {password}\n")

# Function to display statistics (number of users and tasks)
def display_statistics():
    """Displays statistics including the number of registered users and tasks."""
    num_users = len(read_user_credentials())
    with open(TASKS_FILE, "r") as task_file:
        tasks = task_file.readlines()
    num_tasks = len(tasks)
    print(f"Number of registered users: {num_users}")
    print(f"Number of tasks: {num_tasks}")

# Function to add a task
def add_task(username):
    """Allows a user to add a new task."""
    assigned_to = username if username != "admin" else input("Enter the username of the person the task is assigned to: ")
    task_title = input("Enter the title of the task: ")
    task_description = input("Enter the description of the task: ")
    due_date = input("Enter the due date of the task (YYYY-MM-DD): ")

    try:
        datetime.datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    with open(TASKS_FILE, "a") as task_file:
        task_file.write(f"{assigned_to}, {task_title}, {task_description}, {due_date}, {current_date}, No\n")
    print("Task added successfully.")

# Function to view all tasks
def view_all_tasks():
    """Displays all tasks stored in the tasks file."""
    with open(TASKS_FILE, "r") as task_file:
        tasks = task_file.readlines()
    if tasks:
        print("All Tasks:")
        for task in tasks:
            task_data = task.strip().split(", ")
            if len(task_data) == 6:
                assigned_to, task_title, task_description, due_date, current_date, status = task_data
                print(f"Assigned to: {assigned_to}")
                print(f"Task Title: {task_title}")
                print(f"Description: {task_description}")
                print(f"Due Date: {due_date}")
                print(f"Created Date: {current_date}")
                print(f"Status: {status}\n")
                print("-" * 30)
            else:
                print(f"Invalid task format: {task}")
    else:
        print("No tasks available.")

# Function to view tasks assigned to a specific user
def view_my_tasks(username):
    """Displays tasks assigned to a specific user."""
    with open(TASKS_FILE, "r") as task_file:
        tasks = task_file.readlines()
    user_tasks = []
    if tasks:
        for task in tasks:
            task_data = task.strip().split(", ")
            if len(task_data) == 6:
                assigned_to, task_title, task_description, due_date, current_date, status = task_data
                if assigned_to == username:
                    task_dict = {
                        "Assigned to": assigned_to,
                        "Task Title": task_title,
                        "Description": task_description,
                        "Due Date": due_date,
                        "Created Date": current_date,
                        "Status": status
                    }
                    user_tasks.append(task_dict)

        if user_tasks:
            print(f"Tasks for {username}:")
            for task in user_tasks:
                print("Task Details:")
                for field, value in task.items():
                    print(f"{field}: {value}")
                print("-" * 30)
        else:
            print(f"No tasks available for {username}.")

# Main function that serves as the entry point
def main():
    """Main function that handles user authentication and menu options."""
    user_credentials = read_user_credentials()

    while True:
        username = input("Enter your username: ")

        if username in user_credentials:
            password = input("Enter your password: ")
            if password == user_credentials[username]:
                is_admin = (username == "admin")

                while True:
                    menu = input(f'''Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
{"r - register a user" if is_admin else ""}
{"s - view statistics" if is_admin else ""}
: ''').lower()

                    if is_admin and menu == 'r':
                        new_username = input("Enter a new username: ")
                        if new_username in user_credentials:
                            print("Username already exists. Choose a different username.")
                        else:
                            new_password = input("Enter a new password: ")
                            confirm_password = input("Confirm the password: ")
                            if new_password == confirm_password:
                                user_credentials[new_username] = new_password
                                write_user_credentials(new_username, new_password)
                                print("User registered successfully.")
                            else:
                                print("Passwords do not match. User registration failed.")
                            continue

                    elif is_admin and menu == 's':
                        display_statistics()

                    elif menu == 'a':
                        add_task(username)

                    elif menu == 'va':
                        view_all_tasks()

                    elif menu == 'vm':
                        view_my_tasks(username)

                    elif menu == 'e':
                        print('Goodbye!!!')
                        break
                    else:
                        print("Invalid input. Please try again.")
            else:
                print("Incorrect password. Access denied.")
        else:
            print("Username not found. Access denied.")

if __name__ == "__main__":
    main()