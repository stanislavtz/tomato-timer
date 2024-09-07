import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#379B46"
YELLOW = "#f7f5dd"
BACK_GROUND = "#F0CAA3"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15

reps = 0
timer_id = ''


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer_id)
    title_text.config(text="Timer", fg=GREEN)
    my_canvas.itemconfig(timer_text_id, text="00:00")
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    working_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0 and reps > 0:
        check_marks.config(text=f"{check_marks.cget('text') + '✔'}")

    if reps % 8 == 0:
        title_text.config(text="L-Break", fg=RED)
        count_down(long_break_sec)
        check_marks.config(text="")
        reps = 0
    elif reps % 2 == 0:
        title_text.config(text="S-Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_text.config(text="Work Time", fg=GREEN)
        count_down(working_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time):
    minutes = math.floor(time / 60)
    seconds = math.floor(time % 60)

    my_canvas.itemconfig(timer_text_id, text=f"{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")

    if time > -1:
        global timer_id
        timer_id = window.after(1000, count_down, time - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=BACK_GROUND)

title_text = Label(text="Timer", bg=BACK_GROUND, fg=GREEN, font=(FONT_NAME, 28, "bold"))
title_text.grid(column=1, row=0)

my_canvas = Canvas(width=205, height=227, bg=BACK_GROUND, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
my_canvas.create_image(103, 114, image=tomato_img)
timer_text_id = my_canvas.create_text(103, 135, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
my_canvas.grid(column=1, row=1)

start_button = Button(text="Start", bg=YELLOW, font=(FONT_NAME, 12, "italic"), justify="center", highlightthickness=0)
start_button.config(command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW, font=(FONT_NAME, 12, "italic"), justify="center", highlightthickness=0)
reset_button.config(command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=BACK_GROUND, font=(FONT_NAME, 12, "bold"), justify="center", highlightthickness=0)
check_marks.grid(column=1, row=3)

window.mainloop()
