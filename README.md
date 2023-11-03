# Task-manager
This project is a basic user and task management system in Python. It allows users to register, log in, add tasks, view all tasks, view their own tasks, and view system statistics. Administrators can also register new users and view additional statistics. Task details include the assignee, task title, description, due date, creation date, and task status. The system stores user credentials in a text file and task data in another text file, offering a simple yet functional way to manage tasks and user accounts.

How to use this program:

1. Prepare Data Files:

  Create two text files in the same directory as the program: "user.txt" and "tasks.txt".
  In "user.txt," add user credentials in the format "username, password" for each user,     one per line. For example:
      Copy code
      user1, password1
      user2, password2
      admin, adminpassword
  Leave "tasks.txt" empty for now; you will add tasks through the program.
  
2. Run the Program:

  Execute the Python script in your preferred Python environment.
  The program will prompt you to enter a username and password. Use the credentials from   "user.txt."
  Main Menu:

  After successfully logging in, you will see a main menu with options:
  "a" to add a task.
  "va" to view all tasks.
  "vm" to view your tasks.
  "e" to exit the program.
  If you are the admin:
  "r" to register a new user.
  "s" to view statistics.
  
3. Add a Task:

  If you choose "a" to add a task, you will be prompted to provide details such as:
  Assigned user (either your username or another user's username, or "admin" if you are     the admin).
  Task title.
  Task description.
  Due date in the format "YYYY-MM-DD."
  
4. View Tasks:

  If you choose "va" or "vm," the program will display tasks.
  "va" shows all tasks.
  "vm" shows tasks assigned to you if you are not the admin, or tasks assigned to a   specific user if you are the admin.
  
5. Register a New User (Admin Only):

   If you are the admin and choose "r," you can register a new user by providing a           username and password. Make sure the username is unique and the password matches the      confirmation.

7. View Statistics (Admin Only):

  If you are the admin and choose "s," the program will display the number of registered   users and tasks.

8. Exiting the Program:

  To exit the program, choose "e."
  
9. Invalid Inputs:

  If you provide an invalid input, incorrect password, or an unknown username, the          program will provide appropriate feedback.
  
10. Repeat as Needed:

  You can use the program to manage tasks and user accounts as required, and data will be   saved in "tasks.txt" and "user.txt."
