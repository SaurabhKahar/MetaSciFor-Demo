''' Q. Udemy, an online website to learn coding recently gave a free online course on Basics of Python which included the fundamentals of python, Data Structures, creating basic GUI. At last there was a quiz conducted by Udemy to all and everyone secured good marks and also got the certification. Matthew, who was a part of this course as well, thought if he could create one GUI same as Udemy using Python itself for a quiz but Matthew is not aware about few concepts like how to show a message box and stuff in GUI.
So to help matthew write a code in python that will show the questions, should be able to select any one answer using radio button, and a button to go to the next question and a button to quit from the quiz and a message pop up to show the result once the quiz is done
#import required modules


#read front he json file and show each question and options on the GUI using labels and ask the user to choose one option using radiobutton options check if its right and update the score variable parallely


#finally show the score of the user when all the questions are done answering
'''

import tkinter as tk
from tkinter import messagebox
import json

# Load quiz questions from JSON file
with open('quiz_questions.json', 'r') as file:
    quiz_data = json.load(file)

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")

        self.score = 0
        self.current_question = 0

        self.question_label = tk.Label(root, text="", wraplength=400, justify="left")
        self.question_label.pack(pady=20)

        self.options_var = tk.StringVar()
        self.option_buttons = []

        for _ in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.options_var, value="", wraplength=400, justify="left")
            rb.pack(anchor='w', padx=20, pady=5)
            self.option_buttons.append(rb)

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

        self.quit_button = tk.Button(root, text="Quit", command=self.quit_quiz)
        self.quit_button.pack(pady=10)

        self.show_question()

    def show_question(self):
        question_data = quiz_data[self.current_question]
        self.question_label.config(text=question_data['question'])
        self.options_var.set(None)

        for i, option in enumerate(question_data['options']):
            self.option_buttons[i].config(text=option, value=option)

    def next_question(self):
        if self.options_var.get() == quiz_data[self.current_question]['answer']:
            self.score += 1

        self.current_question += 1

        if self.current_question < len(quiz_data):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"Your score is: {self.score}/{len(quiz_data)}")
        self.root.quit()

    def quit_quiz(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.root.after(0, self.show_thank_you_message)

    def show_thank_you_message(self):
        messagebox.showinfo("Thank You", "Thank you for participating in the quiz!")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
