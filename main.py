from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Copied to Clipboard!", message="Password copied to clipboard.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_to_save = website_entry.get()
    email_to_save = email_entry.get()
    password_to_save = password_entry.get()

    if len(website_to_save) == 0 or len(password_to_save) == 0:
        messagebox.showwarning(title="Oops!", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website_to_save, message=f"These are the details entered: "
                                                                      f"\nEmail: {email_to_save} "
                                                                      f"\nPassword: {password_to_save} "
                                                                      f"\nIs it ok to save?")

        if is_ok:
            with open("password_file.txt", "a") as password_file:
                password_file.write(f"{website_to_save} | {email_to_save} | {password_to_save}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

# Create Image Canvas
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Create Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Create Entries
website_entry = Entry(width=58)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=58)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "testusername")

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

# Create Buttons
generate_pw_button = Button(text="Generate Password", width=20, command=generate_password)
generate_pw_button.grid(column=2, row=3)

add_button = Button(text='Add', width=50, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
