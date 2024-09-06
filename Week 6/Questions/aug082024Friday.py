'''

In a coding class the teacher has taught the kids about the python GUI and has now assigned the following task to the students

1) Create a random name picker from a given list of students

2) should have a button clicking on which a random name should be picked

3) Once the random name is picked the name should be removed from the list so that the name is not repeated and also the removed name
should show in completed section

#create a GUI with two sections one to see the randomly generated name and the other one to see the names that are generated randomly
and which are not suppose to be considered for generating randomly again.

'''

import tkinter as tk
import random

students = ["Saurabh", "Abhimanyu", "Sandesh", "Rahul", "Kohli", "Rohit", "Amit", "Narendra"]

def pick_name():
    if students:
        name = random.choice(students)
        students.remove(name)
        name_var.set(name)
        completed_list.insert(tk.END, name)
    else:
        name_var.set("No more names")

root = tk.Tk()
root.title("Random Name Picker")

name_var = tk.StringVar()

tk.Label(root, textvariable=name_var, font=("Helvetica", 16)).pack(pady=20)

tk.Button(root, text="Pick a Name", command=pick_name).pack(pady=10)

tk.Label(root, text="Completed Names:").pack(pady=10)
completed_list = tk.Listbox(root)
completed_list.pack(padx=20, pady=10)

root.mainloop()









