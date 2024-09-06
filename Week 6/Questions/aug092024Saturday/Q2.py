#create a school registeration form

import tkinter as tk
from tkinter import messagebox

def Form():
    name = nameEntry.get()
    age = ageEntry.get()
    sclass = classEntry.get()
    contact = contactEntry.get()
    
    if not name or not age or not sclass or not contact:
        messagebox.showwarning("Input Error", "All fields must be filled out")
        return

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Class: {sclass}")
    print(f"Contact: {contact}")
    
    # Clear the entry fields
    nameEntry.delete(0, tk.END)
    ageEntry.delete(0, tk.END)
    classEntry.delete(0, tk.END)
    contactEntry.delete(0, tk.END)
    
    # Optionally show a confirmation message
    messagebox.showinfo("Registration Details", "Form submitted successfully!")

# Create the main window
root = tk.Tk()
root.title("School Registration Form")

# Create and place labels and entry fields
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Class:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Contact:").grid(row=3, column=0, padx=10, pady=5, sticky="e")

nameEntry = tk.Entry(root)
nameEntry.grid(row=0, column=1, padx=10, pady=5)

ageEntry = tk.Entry(root)
ageEntry.grid(row=1, column=1, padx=10, pady=5)

classEntry = tk.Entry(root)
classEntry.grid(row=2, column=1, padx=10, pady=5)

contactEntry = tk.Entry(root)
contactEntry.grid(row=3, column=1, padx=10, pady=5)

# Create and place the submit button
submitButton = tk.Button(root, text="Submit", command=Form)
submitButton.grid(row=4, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
