#Using tkinter add filter ,lambda and other advance concept to display once click on the button


import tkinter as tk

def filterEvenNumbers():
    numbers = [1,2,3,4,5,6,7,8,9,10]

    evenNumbers = list(filter(lambda x: x % 2 == 0, numbers))

    evenResult.config(text = f"Even Numbers: {evenNumbers}")

    #print("Even Number", evenNumbers)

def filterOddNumbers():
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    oddNumbers = list(filter(lambda x: x % 2 != 0, numbers))

    oddResult.config(text = f"Odd Numbers: {oddNumbers}")


root = tk.Tk()
root.title("Filter Numbers using lambda")


filterEvenButton = tk.Button(root, text = "Filter Even Button", command = filterEvenNumbers)
filterEvenButton.grid(row = 0, column = 0, padx = 10, pady = 10)

filterOddButton = tk.Button(root, text = "Filter Odd Button", command = filterOddNumbers)
filterOddButton.grid(row = 0, column = 1, padx = 10, pady = 10)

evenResult = tk.Label(root, text = "Even Numbers: ")
evenResult.grid(row = 1, column = 0, padx = 10, pady = 10)

oddResult = tk.Label(root, text = "Even Numbers: ")
oddResult.grid(row = 1, column = 1, padx = 10, pady = 10)

root.mainloop()









