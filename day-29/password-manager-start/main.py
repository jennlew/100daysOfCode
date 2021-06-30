from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    saved = open("data.txt", "a")
    saved.write(f"{website} | {email} | {password}\n")
    saved.close()

    website_input.delete(0, END)
    password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "jen@email.com")

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(row=3, column=1)

password_btn = Button(text="Generate Password")
password_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()