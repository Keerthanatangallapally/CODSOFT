import tkinter as tk
import random

# Initialize main window
app = tk.Tk()
app.title("Rock-Paper-Scissors Game")
app.geometry("400x300")

# Labels to display choices and result
user_label = tk.Label(app, text="Your Choice: ")
user_label.pack()

computer_label = tk.Label(app, text="Computer's Choice: ")
computer_label.pack()

result_label = tk.Label(app, text="Result: ")
result_label.pack()

# Choices list for computer
choices = ["Rock", "Paper", "Scissors"]
def rock_button():
    choice = "Rock"
    comp = random.choice(choices)

    # Display choices
    user_label.config(text="Your Choice: " + choice)
    computer_label.config(text="Computer's Choice: " + comp)

    if choice == comp:
        result_label.config(text="Result: game is drawn!")
    elif choice == "Rock" and comp == "Scissors":
        result_label.config(text="Result: You Win!")
    elif choice == "Rock" and comp == "Paper":
        result_label.config(text="Result: You Lose!")

def paper_button():
    choice="Paper"
    comp=random.choice(choices)

    user_label.config(text="Your Choice:" + choice)
    computer_label.config(text="Computer's Choice:" + comp)

    if choice=="Paper" and comp=="Scissors":
       result_label.config(text="Result: You Win!")
    else:
       result_label.config(text="Result: game is drawn!")

def scissor_button():
    choice="Scissors"
    comp=random.choice(choices)

    user_label.config(text="Your Choice:" + choice)
    computer_label.config(text="Computer's Choice:" + comp)

    if choice=="Scissors" and comp=="Rock":
        result_label.config(text="Result: You Win!")
    elif choice=="Scissors" and comp=="Paper":
        result_label.config(text="Result: You Lose!")
    else:
        result_label.config(text="Result: game is drawn! ")

rock_button=tk.Button(app,text="ROCK",command=rock_button)
paper_button=tk.Button(app,text="PAPER",command=paper_button)
scissor_button=tk.Button(app,text="SCISSORS",command=scissor_button)
rock_button.pack()
paper_button.pack()
scissor_button.pack()
app.mainloop()
    


