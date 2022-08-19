from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_text = website_entry.get()
    email_username_text = email_username_entry.get()
    password_text = password_entry.get()

    if len(website_text) == 0 or len(email_username_text) == 0 or len(password_text) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_text, message=f"These are the detail entered: "
                                                               f"\nEmail: {email_username_text} "
                                                               f"\nPassword: {password_text} "
                                                               f"\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website_text} | {email_username_text} | {password_text}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# Label
# website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
# email/username label
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
# password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


# Entry
# website entry
website_entry = Entry(width=39)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
# email/username entry
email_username_entry = Entry(width=39)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "username@gmail.com")
# password entry
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)


# Button
# generate password button
gen_password_button = Button(text="Generate Password", command=password_generator)
gen_password_button.grid(column=2, row=3)
# add button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()

