import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.root.configure(bg="#282C34")  # Dark theme background

        self.tasks = []

        # Title Label
        self.title_label = tk.Label(root, text="To-Do List", font=("Arial", 16, "bold"), fg="white", bg="#282C34")
        self.title_label.pack(pady=10)

        # Task Entry
        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(root, textvariable=self.task_var, font=("Arial", 12), width=30)
        self.task_entry.pack(pady=10)

        # Buttons
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#61AFEF", fg="white", font=("Arial", 12), width=12)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Task", command=self.update_task, bg="#98C379", fg="white", font=("Arial", 12), width=12)
        self.update_button.pack(pady=5)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, bg="#E06C75", fg="white", font=("Arial", 12), width=12)
        self.remove_button.pack(pady=5)

        self.clear_button = tk.Button(root, text="Clear All", command=self.clear_tasks, bg="#C678DD", fg="white", font=("Arial", 12), width=12)
        self.clear_button.pack(pady=5)

        # Tasks List
        self.tasks_frame = tk.Frame(root, bg="#282C34")
        self.tasks_frame.pack(pady=10)

        self.update_tasks_view()

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append(task)
            self.task_var.set("")
            self.update_tasks_view()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def remove_task(self):
        if self.tasks:
            task_index = self.get_task_index()
            if task_index is not None:
                del self.tasks[task_index]
                self.update_tasks_view()
        else:
            messagebox.showwarning("Warning", "No tasks to remove!")

    def update_task(self):
        if self.tasks:
            task_index = self.get_task_index()
            if task_index is not None:
                new_task = self.task_var.get()
                if new_task:
                    self.tasks[task_index] = new_task
                    self.task_var.set("")
                    self.update_tasks_view()
                else:
                    messagebox.showwarning("Warning", "Updated task cannot be empty!")
        else:
            messagebox.showwarning("Warning", "No tasks to update!")

    def clear_tasks(self):
        if self.tasks:
            self.tasks.clear()
            self.update_tasks_view()
        else:
            messagebox.showwarning("Warning", "No tasks to clear!")

    def update_tasks_view(self):
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        for index, task in enumerate(self.tasks, start=1):
            task_label = tk.Label(self.tasks_frame, text=f"{index}. {task}", font=("Arial", 12), fg="white", bg="#282C34")
            task_label.pack(anchor=tk.W)

    def get_task_index(self):
        try:
            index = int(self.task_var.get()) - 1
            if 0 <= index < len(self.tasks):
                return index
            else:
                messagebox.showwarning("Warning", "Invalid task number!")
        except ValueError:
            messagebox.showwarning("Warning", "Enter a valid task number!")
        return None


# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
