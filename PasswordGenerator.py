"""
Code written by : @Vansh-Coder on Github
Note : This code is licensed under the MIT License. Happy Coding ! :)
"""

import pyperclip as pc
from string import *
from tkinter import *
from random import shuffle
from secrets import choice
from tkinter import messagebox

generator = Tk()
generator.title('Password Generator')
generator.geometry("400x408")

x = []

def check(var):
    global x
    var = var.get()
    if var not in x and len(var) > 1:
        if var == ascii_lowercase:
            spin_lower.config(state=NORMAL)
        if var == ascii_uppercase:
            spin_upper.config(state=NORMAL)
        if var == digits:
            spin_number.config(state=NORMAL)
        if var == punctuation:
            spin_special.config(state=NORMAL)
        x.append(var)
    elif var == 'l':
        spin_lower.config(state=DISABLED)
        x.remove(ascii_lowercase)
    elif var == 'u':
        spin_upper.config(state=DISABLED)
        x.remove(ascii_uppercase)
    elif var == 'n':
        spin_number.config(state=DISABLED)
        x.remove(digits)
    elif var == 's':
        spin_special.config(state=DISABLED)
        x.remove(punctuation)

def generate():
    global x
    f = True
    current_lower = current_upper = current_number = current_special = 0

    if check_lower.get() != 'l':
        current_lower = spin_lower.get()
        if current_lower.isdigit() is False:
            f = False
            messagebox.showinfo('Minimum characters error !', "Minimum characters should be a valid positive integer. Please try again !")
        elif current_lower == 0:
            current_lower = 1

    if check_upper.get() != 'u':
        current_upper = spin_upper.get()
        if current_upper.isdigit() is False and f is True:
            f = False
            messagebox.showinfo('Minimum characters error !', "Minimum characters should be a valid positive integer. Please try again !")
        elif current_upper == 0:
            current_upper = 1

    if check_number.get() != 'n':
        current_number = spin_number.get()
        if current_number.isdigit() is False and f is True:
            f = False
            messagebox.showinfo('Minimum characters error !', "Minimum characters should be a valid positive integer. Please try again !")
        elif current_number == 0:
            current_number = 1

    if check_special.get() != 's':
        current_special = spin_special.get()
        if current_special.isdigit() is False and f is True:
            f = False
            messagebox.showinfo('Minimum characters error !', "Minimum characters should be a valid positive integer. Please try again !")
        elif current_special == 0:
            current_special = 1

    if len(check_lower.get()) == len(check_upper.get()) == len(check_number.get()) == len(check_special.get()) == 1 and f is True:
        f = False
        messagebox.showinfo('Error !', "Please select at least one requirement to generate a password and try again !")

    if total.get().isdigit() is False and f is True:
        f = False
        messagebox.showinfo('Password length error !', "Password length should be a valid positive integer. Please try again !")

    current_lower, current_upper, current_number, current_special = int(current_lower), int(current_upper), int(current_number), int(current_special)
    min_sum = (current_lower + current_upper + current_number + current_special)

    if f is True and int(total.get()) < min_sum:
        f = False
        messagebox.showinfo('Password length error !', "Password length cannot be smaller than the sum of minimum characters. Please try again !")

    if f is True:
        y = x.copy()
        y = ''.join(y)
        while True:
            z = ''.join(choice(y) for i in range(int(total.get())))
            if sum(i.islower() for i in z) >= current_lower and sum(i.isupper() for i in z) >= current_upper and sum(i.isdigit() for i in z) >= current_number and sum(i.isalnum() for i in z) <= len(z)-current_special:
                z = list(z)
                shuffle(z)
                z = ''.join(z)
                text.delete(1.0, "end")
                text.insert(1.0, z)
                break

def copy():
    current_text = text.get("1.0", "end-1c")
    if len(current_text) > 0:
        pc.copy(current_text)

label_top = Label(generator, text='Select your requirements :', font=("Arial", 12), padx=5, pady=5)
label_min = Label(generator, text='Minimum characters :', font=("Arial", 11), padx=35)

check_lower = StringVar()
check_upper = StringVar()
check_number = StringVar()
check_special = StringVar()

button_lower = Checkbutton(generator, text='Lowercase letters', variable=check_lower, onvalue=ascii_lowercase, offvalue='l', width=16, font=("Arial", 11), anchor=W, command=lambda: check(check_lower))
button_upper = Checkbutton(generator, text='Uppercase letters', variable=check_upper, onvalue=ascii_uppercase, offvalue='u', width=16, font=("Arial", 11), anchor=W, command=lambda: check(check_upper))
button_number = Checkbutton(generator, text='Numbers', variable=check_number, onvalue=digits, offvalue='n', width=16, font=("Arial", 11), anchor=W, command=lambda: check(check_number))
button_special = Checkbutton(generator, text='Special characters', variable=check_special, onvalue=punctuation, offvalue='s', width=16, font=("Arial", 11), anchor=W, command=lambda: check(check_special))

spin_lower = Spinbox(generator, from_=0, to=100, font=('Arial', 12), width=4)
spin_upper = Spinbox(generator, from_=0, to=100, font=('Arial', 12), width=4)
spin_number = Spinbox(generator, from_=0, to=100, font=('Arial', 12), width=4)
spin_special = Spinbox(generator, from_=0, to=100, font=('Arial', 12), width=4)

label_total = Label(generator, text='Enter password Length :', font=("Arial", 11), padx=13, pady=15)
total = Entry(generator, width=12, borderwidth=2, font=("Arial", 10))

button_generate = Button(generator, text='Generate', width=10, fg='#009933', activeforeground='#00802b', activebackground='#cccccc', font=("Arial", 10), command=generate)
button_copy = Button(generator, text='Copy', width=10, activebackground='#cccccc', font=("Arial", 10), command=copy)

label_spacing = Label(generator, font=("Arial", 5))

text = Text(generator, height=8, width=49, padx=3, pady=3, font=("Arial", 11))

label_top.grid(row=0, column=0)
label_min.grid(row=1, column=1)

button_lower.grid(row=2, column=0)
button_upper.grid(row=3, column=0)
button_number.grid(row=4, column=0)
button_special.grid(row=5, column=0)

spin_lower.grid(row=2, column=1)
spin_upper.grid(row=3, column=1)
spin_number.grid(row=4, column=1, pady=2)
spin_special.grid(row=5, column=1, pady=2)

label_total.grid(row=6, column=0, sticky=W)
total.grid(row=6, column=1, pady=18, sticky=W)

button_generate.grid(row=7, column=0)
button_copy.grid(row=7, column=1)

label_spacing.grid(row=8, column=0)

text.grid(row=9, column=0, columnspan=2, sticky=W)

button_lower.deselect()
button_upper.deselect()
button_number.deselect()
button_special.deselect()

spin_lower.config(state=DISABLED)
spin_upper.config(state=DISABLED)
spin_number.config(state=DISABLED)
spin_special.config(state=DISABLED)

generator.resizable(False, False)
generator.mainloop()
