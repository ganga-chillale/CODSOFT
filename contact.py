import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("500x500")
        self.root.configure(bg="#282C34")  # Dark theme

        self.contacts = {}  # Store contacts in a dictionary

        # Title Label
        self.title_label = tk.Label(root, text="Contact Book", font=("Arial", 16, "bold"), fg="white", bg="#282C34")
        self.title_label.pack(pady=10)

        # Entry Fields
        self.name_label = tk.Label(root, text="Name:", font=("Arial", 12), fg="white", bg="#282C34")
        self.name_label.pack()
        self.name_entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.name_entry.pack(pady=5)

        self.phone_label = tk.Label(root, text="Phone:", font=("Arial", 12), fg="white", bg="#282C34")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.phone_entry.pack(pady=5)

        self.email_label = tk.Label(root, text="Email:", font=("Arial", 12), fg="white", bg="#282C34")
        self.email_label.pack()
        self.email_entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.email_entry.pack(pady=5)

        self.address_label = tk.Label(root, text="Address:", font=("Arial", 12), fg="white", bg="#282C34")
        self.address_label.pack()
        self.address_entry = tk.Entry(root, font=("Arial", 12), width=30)
        self.address_entry.pack(pady=5)

        # Buttons
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact, bg="#61AFEF", fg="white", font=("Arial", 12), width=18)
        self.add_button.pack(pady=5)

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact, bg="#98C379", fg="white", font=("Arial", 12), width=18)
        self.search_button.pack(pady=5)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact, bg="#E5C07B", fg="white", font=("Arial", 12), width=18)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact, bg="#E06C75", fg="white", font=("Arial", 12), width=18)
        self.delete_button.pack(pady=5)

        # Contact List Display
        self.contact_listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=8)
        self.contact_listbox.pack(pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts[phone] = {"Name": name, "Email": email, "Address": address}
            self.refresh_contact_list()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Error", "Name and Phone are required!")

    def refresh_contact_list(self):
        self.contact_listbox.delete(0, tk.END)
        for phone, details in self.contacts.items():
            self.contact_listbox.insert(tk.END, f"{details['Name']} - {phone}")

    def search_contact(self):
        query = simpledialog.askstring("Search", "Enter Name or Phone:")
        if query:
            found = False
            for phone, details in self.contacts.items():
                if query in details["Name"] or query in phone:
                    messagebox.showinfo("Contact Found", f"Name: {details['Name']}\nPhone: {phone}\nEmail: {details['Email']}\nAddress: {details['Address']}")
                    found = True
                    break
            if not found:
                messagebox.showwarning("Not Found", "No matching contact found!")

    def update_contact(self):
        query = simpledialog.askstring("Update", "Enter Phone Number of Contact to Update:")
        if query in self.contacts:
            new_name = simpledialog.askstring("Update", "Enter New Name:", initialvalue=self.contacts[query]["Name"])
            new_email = simpledialog.askstring("Update", "Enter New Email:", initialvalue=self.contacts[query]["Email"])
            new_address = simpledialog.askstring("Update", "Enter New Address:", initialvalue=self.contacts[query]["Address"])

            if new_name:
                self.contacts[query] = {"Name": new_name, "Email": new_email, "Address": new_address}
                self.refresh_contact_list()
                messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showwarning("Error", "Contact not found!")

    def delete_contact(self):
        query = simpledialog.askstring("Delete", "Enter Phone Number of Contact to Delete:")
        if query in self.contacts:
            del self.contacts[query]
            self.refresh_contact_list()
            messagebox.showinfo("Deleted", "Contact deleted successfully!")
        else:
            messagebox.showwarning("Error", "Contact not found!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
