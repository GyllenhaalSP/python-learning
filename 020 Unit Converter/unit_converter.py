"""
 By GyllenhaalSP ago. 2022 @ https://github.com/GyllenhaalSP.
"""
from tkinter import Tk, Label, Button, Entry, mainloop

FONT = ('Courier', 10, 'normal')


def convert():
    """
    It converts!
    """
    labels[3].config(text=round(float(num_box.get()) * 1.609))


window = Tk()
window.title("Unit Converter - Miles to KM")

labels = [Label(font=FONT, padx=33, pady=5) for _ in range(4)]

button = Button(text='Calculate', command=convert)
button.grid(column=1, row=3)

num_box = Entry(width=15, justify='right')
num_box.grid(column=1, row=0)
num_box.insert(0, "")
num_box.focus()

labels[0].config(text='equals')
labels[1].config(text='Miles')
labels[2].config(text='KM')
labels[3].config(text='0')

labels[0].grid(column=0, row=1)
labels[1].grid(column=2, row=0)
labels[2].grid(column=2, row=1)
labels[3].grid(column=1, row=1)

mainloop()
