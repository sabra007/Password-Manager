  
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    entry_pass.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # new_dict = {new_key : new_value for item in list}
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    entry_pass.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    
    website = entry_website.get()
    email = entry_email.get()
    password = entry_pass.get()
    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Oops", message="Don't leave empty fields.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open(r"data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")

            entry_website.delete(0, END)
            entry_pass.delete(0, END)
            entry_website.focus()
    
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = Canvas(width=200 , height=200)
lock_image = PhotoImage(file=r"logo.png")
canvas.create_image(100, 100, image=lock_image)

canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1,sticky = E)


label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2, sticky = E)

label_pass = Label(text="Password:")
label_pass.grid(column=0, row=3, sticky = E)

entry_website = Entry(width=40)
entry_website.grid(column=1, row=1, columnspan=2, sticky = W)
entry_website.focus()

entry_email = Entry(width=40)
entry_email.grid(column=1, row=2, columnspan=2, sticky = W)
entry_email.insert(0, "")

entry_pass = Entry(width=29)
entry_pass.grid(column=1, row=3, sticky = W)

button_gen = Button(text="Generate Password", width=15, command = generate_password)
button_gen.grid(column=2, row=3)

button_add = Button(text="Add", width=40, command = save_data)
button_add.grid(column=1, row=4, columnspan=2, sticky = W)

window.mainloop()