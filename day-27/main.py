from tkinter import *

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

label = Label(text="I am a Label", font=("Arial", 24))
label.grid(column= 0, row=0)


def button_clicked():
    print("I got clicked")
    new_input = input.get()
    label.config(text=new_input)


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

input = Entry(width=10)
input.grid(column=3, row=2)
new_button = Button(text="new button")
new_button.grid(column=2, row=0)

window.mainloop()
