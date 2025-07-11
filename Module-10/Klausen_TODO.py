# Author: Kyle Klausen
# Assignment: Module10_2
# Date: 07/10/25 
# Description: A simple code which creates a to-do list that has functions to help improve functionality

import tkinter as tk
from tkinter import messagebox

class Todo(tk.Tk):
    """
    A simple Tkinter To-Do list application with scrolling and task deletion.
    """
    def __init__(self):
        super().__init__()
        self.title("Klausen-ToDo")
        self.geometry("400x550")

        # --- Menu Bar ---
        menu_bar = tk.Menu(self, bg="purple", fg="white")
        file_menu = tk.Menu(menu_bar, tearoff=0, bg="gold", fg="black")
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu_bar)

        # Instruction Label
        instruction_label = tk.Label(self, text="Right-click a task to delete it",
                                     bg="#fff8dc", fg="black", font=("Inter", 10, "italic"))
        instruction_label.pack(pady=(5, 0))

        # --- Colors for alternating tasks ---
        self.colour_schemes = [
            {"bg": "lightblue", "fg": "black"},
            {"bg": "lightgrey", "fg": "black"}
        ]

        # --- Task Input Frame ---
        self.task_add_frame = tk.Frame(self, bg="#f0f0f0", padx=10, pady=10, bd=2, relief="groove")
        self.task_add_frame.pack(fill="x", padx=10, pady=5)

        self.task_label = tk.Label(self.task_add_frame, text="New Task:", bg="#f0f0f0", font=("Inter", 10, "bold"))
        self.task_label.pack(side="left", padx=(0, 5))

        self.task_input = tk.Entry(self.task_add_frame, width=30, font=("Inter", 10), bd=2, relief="sunken")
        self.task_input.pack(side="left", fill="x", expand=True, padx=(0, 5))
        self.task_input.bind("<Return>", lambda event: self.add_task())

        self.add_task_button = tk.Button(
            self.task_add_frame,
            text="Add Task",
            command=self.add_task,
            bg="#4CAF50", fg="white",
            font=("Inter", 10, "bold"),
            relief="raised", bd=3,
            activebackground="#45a049", activeforeground="white",
            padx=10, pady=5
        )
        self.add_task_button.pack(side="right")

        # --- Task Display Area ---
        self.tasks_canvas = tk.Canvas(self, bg="#f5f5f5", bd=0, highlightthickness=0)
        self.tasks_canvas.pack(side="left", fill="both", expand=True, padx=10, pady=5)

        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.tasks_canvas.yview)
        self.scrollbar.pack(side="right", fill="y", pady=5)

        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.tasks_canvas.bind('<Configure>', self.on_canvas_configure)

        self.tasks_frame = tk.Frame(self.tasks_canvas, bg="#f5f5f5")
        self.tasks_canvas.create_window((0, 0), window=self.tasks_frame, anchor="nw", tags="self.tasks_frame")

        self.tasks_canvas.bind_all("<MouseWheel>", self.mouse_scroll)
        self.tasks_canvas.bind_all("<Button-4>", self.mouse_scroll)  # For Linux
        self.tasks_canvas.bind_all("<Button-5>", self.mouse_scroll)

        self.tasks = []
        self.load_tasks()

        self.tasks_frame.bind("<Configure>", self.on_frame_configure)

    def add_task(self):
        task_text = self.task_input.get().strip()
        if task_text:
            self.create_task_widget(task_text)
            self.task_input.delete(0, tk.END)
            self.update_task_display()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def create_task_widget(self, text):
        task_frame = tk.Frame(self.tasks_frame, bd=1, relief="solid")
        task_frame.pack(fill="x", padx=5, pady=2)

        task_label = tk.Label(task_frame, text=text, wraplength=250, justify="left", font=("Inter", 10))
        task_label.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        # Right-click to delete task
        task_frame.bind("<Button-3>", lambda event: self.delete_task(task_frame))
        task_label.bind("<Button-3>", lambda event: self.delete_task(task_frame))

        self.tasks.append(task_frame)
        self.set_task_colour(len(self.tasks) - 1, task_frame)

    def delete_task(self, task_frame_to_delete):
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this task?"):
            task_frame_to_delete.destroy()
            self.tasks = [task for task in self.tasks if task != task_frame_to_delete]
            self.update_task_display()

    def set_task_colour(self, position, task_frame):
        _, style_index = divmod(position, len(self.colour_schemes))
        scheme = self.colour_schemes[style_index]
        task_frame.configure(bg=scheme["bg"])
        for widget in task_frame.winfo_children():
            widget.configure(bg=scheme["bg"], fg=scheme["fg"])

    def update_task_display(self):
        for i, task_frame in enumerate(self.tasks):
            self.set_task_colour(i, task_frame)
        self.on_frame_configure()

    def on_frame_configure(self, event=None):
        self.tasks_canvas.update_idletasks()
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def on_canvas_configure(self, event):
        canvas_width = event.width
        self.tasks_canvas.itemconfig(self.tasks_canvas.find_withtag("self.tasks_frame"), width=canvas_width)

    def mouse_scroll(self, event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            move = -1 if event.num == 4 else 1 if event.num == 5 else 0
            self.tasks_canvas.yview_scroll(move, "units")

    def load_tasks(self):
        sample_tasks = [
            "Buy groceries",
            "Finish Python project",
            "Call mom",
            "Adjust calendar",
            "Update Reminders",
            "Go for a run",
            "Read 'Tkinter By Example' Chapter 3",
            "Plan weekend trip",
            "Water plants",
            "Schedule dentist appointment",
            "Learn new recipe",
            "Organize desk"
        ]
        for task in sample_tasks:
            self.create_task_widget(task)
        self.update_task_display()

if __name__ == "__main__":
    todo = Todo()
    todo.mainloop()