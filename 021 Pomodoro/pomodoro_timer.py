"""
 By GyllenhaalSP ago. 2022 @ https://github.com/GyllenhaalSP.
"""
from tkinter import Tk, PhotoImage, Label, Button, Canvas
from math import ceil, floor

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#cfe8a9"
YELLOW = "#fffde3"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
CHECKMARK = '\U0001F5F8'
repetitions = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    """
    Resets the timer.
    """
    window.after_cancel(timer)
    title_label.config(text='POMODORO\nTIMER', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'bold'))
    canvas.itemconfig(timer_text, text='00:00')
    checkmark.config(text="")
    global repetitions
    repetitions = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    """
    Starts the timer.
    """
    global repetitions
    repetitions += 1

    work_in_seconds = WORK_MIN * 60
    short_break_in_seconds = SHORT_BREAK_MIN * 60
    long_break_in_seconds = LONG_BREAK_MIN * 60

    if repetitions % 2 == 1:
        countdown(work_in_seconds)
        title_label.config(text="WORK", fg=RED)
    elif repetitions % 8 == 0:
        countdown(long_break_in_seconds)
        title_label.config(text="LONG BREAK", fg=GREEN)
    else:
        countdown(short_break_in_seconds)
        title_label.config(text="BREAK", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    """
    Acts as the countdown timer.
    """
    count_min = floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f'{"0" if count_min < 10 else ""}{count_min}:'
                                       f'{"0" if count_sec < 10 else ""}{count_sec if count_sec != 0 else "0"}')

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start()
        marks = "".join(CHECKMARK for _ in range(ceil(repetitions / 2)))
        checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=25, bg=YELLOW)

bg_img = PhotoImage(file='tomato.png')
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=bg_img)
timer_text = canvas.create_text(100, 140, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)

title_label = Label(text='POMODORO\nTIMER', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'bold'))
title_label.grid(column=1, row=0)
checkmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'bold'))
checkmark.grid(column=1, row=2)

commence = Button(text="Start", command=start, font=(FONT_NAME, 20, 'bold'), highlightthickness=0)
restart = Button(text="Reset", command=reset, font=(FONT_NAME, 20, 'bold'), highlightthickness=0)
commence.grid(column=0, row=2)
restart.grid(column=2, row=2)

window.mainloop()
