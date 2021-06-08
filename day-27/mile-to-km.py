from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=200)
window.config(padx=20, pady=20)

mile_input = Entry(width=7)
mile_input.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_label = Label(text="0")
km_label.grid(column=1, row=1)
km = Label(text="km")
km.grid(column=2, row=1)


def convert_miles():
    miles = mile_input.get()
    kms = float(miles) * 1.60934
    km_label.config(text=kms)


calculate_button = Button(text="Calculate", command=convert_miles)
calculate_button.grid(column=1, row=2)


window.mainloop()
