#! /usr/bin/python3
from tkinter import *
import math

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
NO_OF_REPS = 0
timer = None


def start_fun():
    global NO_OF_REPS
    NO_OF_REPS += 1

    if NO_OF_REPS % 8 == 0 :
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=RED)
    elif  NO_OF_REPS % 2 == 0 :
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


def reset_fun():
    window.after_cancel(timer)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")


def count_down(count):
    count_min = count//60 # or math.floor( count/60)
    count_sec = count%60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_fun()
        marks = ""
        no_of_session = math.floor(NO_OF_REPS/2)

        for _ in range(no_of_session):
            marks += "✔"

        check_label.config(text=marks)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 80), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)

canvas = Canvas(width=394, height=428, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato2.png")
canvas.create_image(CANVAS_CENTER_X, CANVAS_CENTER_Y, image=tomato_img)

timer_text = canvas.create_text(CANVAS_CENTER_X, CANVAS_CENTER_Y+50, text="00:00", fill="white", font=(FONT_NAME, 45, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="start", command=start_fun)
start_button.grid(row=2, column=0)

check_label = Label(bg=YELLOW, fg=GREEN, font = (FONT_NAME, 20, "bold"))
check_label.grid(row=3, column=1)

rest_button = Button(text="Reset", command=reset_fun)
rest_button.grid(row=2, column=2)



window.mainloop()
