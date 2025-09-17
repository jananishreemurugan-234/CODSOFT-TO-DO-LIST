# CODSOFT-TO-DO-LIST

## Project Overview 
The **Codsoft To-Do List Application** is a simple and efficient desktop application created using Python and Tkinter. 
It is designed to help users manage their daily tasks by providing an easy-to-use graphical interface to add, view, complete, and delete tasks. 
The application automatically saves tasks in a file, allowing them to persist between sessions. 

## Objective 
This project was developed as part of the **Codsoft Internship** to give users a practical tool for task management while demonstrating core programming concepts such as GUI development, file handling, and state persistence. 
The goal is to provide a lightweight solution to organize and track personal tasks without relying on complex software. 

## Application Features 
- Add tasks with a text input and a bright green **Add** button. 
- View all tasks in a scrollable listbox with a simple clean display. 
- Mark selected tasks as **Done** (changes appearance to indicate completion). 
- Delete selected tasks permanently. 
- Tasks are automatically saved to a `tasks.json` file. 
- Attractive interface with colorful design elements and user-friendly buttons. 

## User Interface Design 
The application presents a clean, colorful layout as shown in the image: 
- A bright pink heading at the top: 
  **Codsoft To-Do List** 
- An entry field next to a green **Add** button for typing and adding new tasks. 
- A large white listbox in the center that displays all tasks clearly. 
- Two colored buttons below the listbox: 
   - **Done** (blue background): Marks the selected task as completed. 
   - **Delete** (red background): Removes the selected task permanently. 
- The background color is a soft blue (`#188DE7`) to provide a pleasant user experience. 

## How It Works 
1. On launching the application, it loads tasks from `tasks.json` if it exists. 
2. Users type their tasks in the input box and click **Add** → The new task appears in the list. 
3. To mark a task as done, the user selects a task and clicks **Done** → Changes color or appearance. 
4. To remove a task, the user selects it and clicks **Delete** → The task disappears from the list. 
5. Every action automatically updates `tasks.json` for persistence. 

## How to Run 
1. Ensure you have **Python 3.13.7** installed. 
2. Download or clone this repository. 
3. Open your terminal and navigate to the folder where the code is located. 
4. Run the following command: 
   python todo_app.py
5. The GUI window will open and you can start managing your tasks immediately.

##  Conclusion
- This Codsoft To-Do List Application provides a simple yet effective solution for task management.
- It is ideal for beginners who want to learn GUI programming and file handling in Python.
- The attractive design makes it easy and enjoyable to use, while the automatic save feature ensures no task is lost.

## Output
- By using the Done button
<img width="500" height="659" alt="Screenshot 2025-09-17 190829" src="https://github.com/user-attachments/assets/38e400e7-9e66-4754-b02e-033d8d71e1df" />

- By using the Delete button
<img width="496" height="659" alt="Screenshot 2025-09-17 190859" src="https://github.com/user-attachments/assets/36777b86-6ea7-48ed-9f07-4118da3f2c7c" />

