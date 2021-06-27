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


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg=YELLOW)

canvas = Canvas(width=394, height=428, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato2.png")
canvas.create_image(CANVAS_CENTER_X, CANVAS_CENTER_Y, image=tomato_img)
canvas.create_text(CANVAS_CENTER_X, CANVAS_CENTER_Y+40, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

window.mainloop()
