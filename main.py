import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    timer = window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00 ")
    label_timer.config(text="Timer", fg=GREEN)
    label_check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_min=SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60
    if reps % 2 == 1 :
        count_down(work_sec)
        label_timer.config(text="Work")
    elif reps % 8 == 0 :
        count_down(long_break_min)
        label_timer.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_min)
        label_timer.config(text="Short Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark=""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
             mark += "✔"
        label_check.config(text=mark)
    # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
label_timer.grid(row=0, column=1)

canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)

button_start = Button(text="Start", command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", command= reset_timer)
button_reset.grid(row=2, column=2)

label_check = Label(fg=GREEN, font=(FONT_NAME, 15), bg=YELLOW)
label_check.grid(row=4, column=1)

window.mainloop()