import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Add task
def add_task():
    task = entry.get()
    if task != "":
        tasks.append({"task": task, "done": False})
        update_listbox()
        save_tasks(tasks)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Delete task
def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        tasks.pop(selected_index)
        update_listbox()
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

# Mark as done
def mark_done():
    try:
        selected_index = listbox.curselection()[0]
        tasks[selected_index]["done"] = True
        update_listbox()
        save_tasks(tasks)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

# Update listbox display
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        if task["done"]:
            listbox.insert(tk.END,task["task"])
            listbox.itemconfig(tk.END, fg="green")
        else:
            listbox.insert(tk.END,task["task"])

# GUI
root = tk.Tk()
root.title("Codsoft To-Do List Application")
root.geometry("400x500")
root.config(bg="#188DE7")

tasks = load_tasks()

# Heading
title = tk.Label(root, text="Codsoft To-Do List", font=("Arial", 18, "bold"), bg="#f90a95", fg="#ecf5fb")
title.pack(pady=10)

# Task entry
entry_frame = tk.Frame(root, bg="#f0f4f7")
entry_frame.pack(pady=10)

entry = tk.Entry(entry_frame, font=("Arial", 14), width=22)
entry.grid(row=0, column=0, padx=5)

add_btn = tk.Button(entry_frame, text="Add", command=add_task, bg="#27ae60", fg="white", font=("Arial", 12), width=8)
add_btn.grid(row=0, column=1)

# Task listbox
listbox = tk.Listbox(root, font=("Arial", 14), width=30, height=12, bd=0, selectbackground="#3498db")
listbox.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root, bg="#b6dbf6")
btn_frame.pack(pady=10)

done_btn = tk.Button(btn_frame, text="Done", command=mark_done, bg="#2980b9", fg="white", font=("Arial", 12), width=8)
done_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete", command=delete_task, bg="#c0392b", fg="white", font=("Arial", 12), width=8)
delete_btn.grid(row=0, column=1, padx=5)

# Load existing tasks
update_listbox()

root.mainloop()