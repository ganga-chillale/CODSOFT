import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stylish Calculator")
        self.root.geometry("350x400")
        self.root.configure(bg="#282C34")  # Dark background

        # Title Label
        self.title_label = tk.Label(root, text="Calculator", font=("Arial", 18, "bold"), fg="white", bg="#282C34")
        self.title_label.pack(pady=10)

        # Entry Fields for Numbers
        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()

        self.num1_entry = tk.Entry(root, textvariable=self.num1_var, font=("Arial", 14), width=15)
        self.num1_entry.pack(pady=5)

        self.num2_entry = tk.Entry(root, textvariable=self.num2_var, font=("Arial", 14), width=15)
        self.num2_entry.pack(pady=5)

        # Operation Selection
        self.operation_var = tk.StringVar()
        self.operation_var.set("+")  # Default operation

        self.operation_menu = tk.OptionMenu(root, self.operation_var, "+", "-", "*", "/")
        self.operation_menu.config(font=("Arial", 12), bg="#61AFEF", fg="white", width=10)
        self.operation_menu.pack(pady=10)

        # Calculate Button
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate, bg="#98C379", fg="white", font=("Arial", 14), width=12)
        self.calculate_button.pack(pady=10)

        # Result Display
        self.result_label = tk.Label(root, text="Result: ", font=("Arial", 14), fg="white", bg="#282C34")
        self.result_label.pack(pady=10)

    def calculate(self):
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
            operation = self.operation_var.get()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    messagebox.showerror("Error", "Cannot divide by zero!")
                    return
                result = num1 / num2

            self.result_label.config(text=f"Result: {result:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")

# Run Application
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
