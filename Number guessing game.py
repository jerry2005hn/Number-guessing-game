#Number guessing game
from tkinter import *
import random

rNumber=random.randint(1,100)
print(rNumber)
window=Tk()
window.title("Number guessing game")
lbl=Label(window,text="Enter your guessing number: ", font=("Arial Bold", 25))
lbl.grid(column=0, row=0)
window.geometry("1000x1000")
textField=Entry(window,width=20)
textField.grid(column=1, row=0)
textField.focus()
def checkBt():
    if int(textField.get())>rNumber:
        lbl.configure(text="Your guessing number is bigger than the random number")
        pass
    if int(textField.get())<rNumber:
        lbl.configure(text="Your guessing number is smaller than the random number")
        pass
    if int(textField.get())==rNumber:
        lbl.configure(text="You are correct")
  
                  
                 

check=Button(window,text="check",command=checkBt)
check.grid(column=1,row=1)


