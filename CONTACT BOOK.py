import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(s,m):
        s.m = m
        s.m.title("Contact Book")
        s.contacts = []

        tk.Label(m,text="Name:").grid(row=0,column=0,sticky="w")
        tk.Label(m,text="Phone:").grid(row=1,column=0,sticky="w")
        s.name_entry = tk.Entry(m)
        s.name_entry.grid(row=0, column=1,padx=5,pady=5)
        s.phone_entry = tk.Entry(m)
        s.phone_entry.grid(row=1,column=1,padx=5,pady=5)

        for i, (text, command) in enumerate([("Add", s.add_contact),("View All", s.view_contacts),("Search",s.search_contact),("Delete", s.delete_contact),("Update", s.update_contact)]):
            tk.Button(m,text=text,command=command).grid(row=i+2,column=0,columnspan=2,pady=5)

    def add_contact(s):
        name, phone = s.name_entry.get(), s.phone_entry.get()
        s.contacts.append((name,phone)) if name and phone else messagebox.showerror("Error", "Name and Phone cannot be empty!")

    def view_contacts(s):
        messagebox.showinfo("Contacts", '\n'.join([f"Name: {contact[0]}, Phone: {contact[1]}" for contact in s.contacts]) if s.contacts else "No contacts found!")

    def search_contact(s):
        name = s.name_entry.get()
        messagebox.showinfo("Contact Found", '\n'.join([f"Name: {contact[0]}, Phone: {contact[1]}" for contact in s.contacts if contact[0].lower() == name.lower()]) or f"No contact found with name '{name}'")

    def delete_contact(s):
        name = s.name_entry.get()
        found = any(contact for contact in s.contacts if contact[0].lower() == name.lower())
        s.contacts = [contact for contact in s.contacts if contact[0].lower() != name.lower()]
        messagebox.showinfo("Success" if found else "Contact Not Found", f"Contact '{name}' {'deleted successfully!' if found else 'not found'}")

    def update_contact(s):
        name, phone = s.name_entry.get(),s.phone_entry.get()
        updated = any(contact for contact in s.contacts if contact[0].lower() == name.lower())
        s.contacts = [(name, phone) if contact[0].lower() == name.lower() else contact for contact in s.contacts]
        messagebox.showinfo("Success" if updated else "Contact Not Found", f"Contact '{name}' {'updated successfully!' if updated else 'not found'}")

def main():
    root = tk.Tk()
    ContactBookApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
