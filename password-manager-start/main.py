from tkinter import *
from tkinter import messagebox
import random
import pyperclip
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def fill_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    Length = random.randint(10, 20)
    all = letters + numbers + symbols
    random.shuffle(all)
    password = [random.choice(all) for char in range(Length)]
    random.shuffle(password)
    password = "".join(password)
    pwd_entry.insert(0, string=password)
    pwd_entry.clipboard_clear()
    pwd_entry.clipboard_append(pwd_entry.get())
    # window popup to tell the user password has being copied
    messagebox.showinfo(title="Copied to Clipboard!", message="Password copied to clipboard.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # message popup to check if any field are empty
    if len(web_entry.get()) == 0 or len(pwd_entry.get()) == 0:
        messagebox.showwarning(title='Empty field found', message='Hey!\nAll fields need to be filled!')
    else:
        # message popup to confirm data entered
        is_ok = messagebox.askokcancel(title=web_entry.get(),
                                       message=f'These are the details entered\n Email: {email_entry.get()}\n Password: {pwd_entry.get()}\n Is it ok to save?')
        if is_ok:
            with open('data.txt', 'a') as data:
                data.write(
                    f'Website: {web_entry.get()}| Email: {email_entry.get()}| Password: {pwd_entry.get()}' + '\n')
                web_entry.delete(0, 'end')
                pwd_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
# window.minsize(400, 400)
window.title('Password Manager')
window.minsize(400, 400)
window.config(pady=50, padx=50)
# canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
padlock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

# label1
website = Label(text='Website:', font=(FONT_NAME, 20))
website.grid(column=0, row=1)

# web_entry
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2, sticky='ew')
web_entry.focus()

# Email/username
email = Label(text='Email/username:', font=(FONT_NAME, 20))
email.grid(column=0, row=2)

# email_entry
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky='ew')
email_entry.insert(END, 'kodiugos@gmail.com')

# password
pwd = Label(text='Password:', font=(FONT_NAME, 20))
pwd.grid(column=0, row=3)

# password_entry
pwd_entry = Entry(width=25)
pwd_entry.grid(column=1, row=3, sticky='ew')

# button
button = Button(text='Generate password', command=fill_password)
button.grid(row=3, column=2, sticky='ew')

# add button
add = Button(text='Add', width=36, command=save)
add.grid(row=4, column=1, columnspan=2, sticky='ew')

window.mainloop()
