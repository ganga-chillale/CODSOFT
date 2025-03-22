import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")
        self.root.configure(bg="#282C34")  # Dark theme

        # Title Label
        self.title_label = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), fg="white", bg="#282C34")
        self.title_label.pack(pady=10)

        # Password Length Input
        self.length_label = tk.Label(root, text="Password Length:", font=("Arial", 12), fg="white", bg="#282C34")
        self.length_label.pack(pady=5)

        self.length_var = tk.IntVar(value=12)  # Default length
        self.length_entry = tk.Entry(root, textvariable=self.length_var, font=("Arial", 12), width=5)
        self.length_entry.pack(pady=5)

        # Checkboxes for character selection
        self.include_upper = tk.BooleanVar(value=True)
        self.include_lower = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)

        tk.Checkbutton(root, text="Uppercase Letters", variable=self.include_upper, bg="#282C34", fg="white", font=("Arial", 10)).pack()
        tk.Checkbutton(root, text="Lowercase Letters", variable=self.include_lower, bg="#282C34", fg="white", font=("Arial", 10)).pack()
        tk.Checkbutton(root, text="Numbers", variable=self.include_digits, bg="#282C34", fg="white", font=("Arial", 10)).pack()
        tk.Checkbutton(root, text="Special Characters", variable=self.include_special, bg="#282C34", fg="white", font=("Arial", 10)).pack()

        # Generate Button
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, bg="#61AFEF", fg="white", font=("Arial", 12), width=18)
        self.generate_button.pack(pady=10)

        # Password Display
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(root, textvariable=self.password_var, font=("Arial", 12), width=25, state="readonly")
        self.password_entry.pack(pady=5)

        # Copy Button
        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_password, bg="#98C379", fg="white", font=("Arial", 12), width=18)
        self.copy_button.pack(pady=5)

    def generate_password(self):
        length = self.length_var.get()

        if length < 4:
            messagebox.showwarning("Warning", "Password length must be at least 4!")
            return

        characters = ""
        if self.include_upper.get():
            characters += string.ascii_uppercase
        if self.include_lower.get():
            characters += string.ascii_lowercase
        if self.include_digits.get():
            characters += string.digits
        if self.include_special.get():
            characters += string.punctuation

        if not characters:
            messagebox.showwarning("Warning", "Select at least one character type!")
            return

        password = "".join(random.choice(characters) for _ in range(length))
        self.password_var.set(password)

    def copy_password(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.password_var.get())
        self.root.update()
        messagebox.showinfo("Success", "Password copied to clipboard!")

# Run Application
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
