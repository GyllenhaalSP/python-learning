"""
 By GyllenhaalSP ago. 2022 @ https://github.com/GyllenhaalSP.
"""
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as msg
import string
from random import shuffle, choice
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    """
    Generates a random password.
    """
    password_entry.delete(0, tk.END)
    shuffle(password := [choice(string.ascii_lowercase) for _ in range(7)] +
                        [choice(string.digits) for _ in range(4)] +
                        [choice(string.punctuation) for _ in range(4)])
    password_entry.insert(0, f'{"".join(password)}')
    pyperclip.copy(f'{"".join(password)}')


def delete():
    """
    Deletes all fields.
    """
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """
    Saves everything.
    """
    if len(website_entry.get()) == 0 or len(username_entry.get()) == 0 or len(password_entry.get()) == 0:
        msg.showwarning(title="ERROR", message="One or more fields are empty.\nPlease do fill all fields.")
        return
    if msg.askokcancel(title=f'{website_entry.get()}', message=f'These are the details entered: \n\n'
                                                               f'Website: {website_entry.get()}\n'
                                                               f'Email: {email_combo.get()}\n'
                                                               f'Username: {username_entry.get()}\n'
                                                               f'Password: {password_entry.get()}\n'
                                                               f'Is it okay to save?'):
        with open('data.txt', 'a', encoding='utf-8') as data:
            data.write(f'{website_entry.get()} | {email_combo.get()} | '
                       f'{username_entry.get()} | {password_entry.get()}\n')

        website_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg='white')

canvas = tk.Canvas(width=246, height=278, bg='white', highlightthickness=0)
logo_img = tk.PhotoImage(file='logo.png')
canvas.create_image(123, 139, image=logo_img)
canvas.grid(column=1, row=0, ipady=15)

website_label = tk.Label(text='Website:', bg='white')
email_label = tk.Label(text='Email:', bg='white')
username_label = tk.Label(text='Username:', bg='white')
password_label = tk.Label(text='Password:', bg='white')

website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
username_label.grid(column=0, row=3)
password_label.grid(column=0, row=4)

website_entry = tk.Entry(width=51)
website_entry.focus()
email_combo = ttk.Combobox(values=['youremail1@gmail.com', 'youremail2@gmail.com'], width=48)
email_combo.set('youremail1@gmail.com')
username_entry = tk.Entry(width=51)
password_entry = tk.Entry(width=32)

website_entry.grid(column=1, row=1, columnspan=2, sticky=tk.W)
email_combo.grid(column=1, row=2, columnspan=2, sticky=tk.W)
username_entry.grid(column=1, row=3, columnspan=2, sticky=tk.W)
password_entry.grid(column=1, row=4, sticky=tk.W)

generate = tk.Button(text='Generate Password', width=15, command=generate, bg='white')
add = tk.Button(text='Add', width=22, command=save, bg='white')
clear = tk.Button(text='Clear', width=21, command=delete, bg='white')

generate.grid(column=1, row=4, sticky=tk.E, columnspan=2)
add.grid(column=1, row=5, sticky=tk.W)
clear.grid(column=1, row=5, sticky=tk.E, columnspan=2)

window.mainloop()
