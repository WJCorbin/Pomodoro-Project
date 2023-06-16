from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = "None"


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    if reps == 9:
        reset_timer()
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minute_count = math.floor(count / 60)
    if minute_count < 10:
        minute_count = f"0{minute_count}"
    second_count = count % 60
    if second_count < 10:
        second_count = f"0{second_count}"

    canvas.itemconfig(timer_text, text=f"{minute_count}:{second_count}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
background = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=background)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
check_label.grid(column=1, row=3)

window.mainloop()
