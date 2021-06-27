#! /usr/bin/python3
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CANVAS_CENTER_X = 394/2
CANVAS_CENTER_Y = 428/2


def start_fun():
    pass

def rest_fun():
    pass

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)

time_label = Label(text="Timer", font=(FONT_NAME, 80), bg=YELLOW, fg=GREEN)
time_label.grid(row=0, column=1)

canvas = Canvas(width=394, height=428, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato2.png")
canvas.create_image(CANVAS_CENTER_X, CANVAS_CENTER_Y, image=tomato_img)
canvas.create_text(CANVAS_CENTER_X, CANVAS_CENTER_Y+50, text="00:00", fill="white", font=(FONT_NAME, 45, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="start", command=start_fun)
start_button.grid(row=2, column=0)

check_label = Label(text="✔", bg=YELLOW, fg=GREEN, font = (FONT_NAME, 20, "bold"))
check_label.grid(row=3, column=1)

rest_button = Button(text="Reset")
rest_button.grid(row=2, column=2)



window.mainloop()
