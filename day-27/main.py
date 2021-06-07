import tkinter

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

label = tkinter.Label(text="I am a Label", fort=("Arial", 24))
label.pack()



window.mainloop()