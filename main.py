from tkinter import *

PINK = "#F2A29B"
RED = "#F1583F"
GREEN = "#379B46"
YELLOW = "#f7f5dd"
WHITE = "#fff"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# TIMER - RESET
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    reps = 0
    pom_label.config(text="Timer", fg=GREEN)


# TIMER - START
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        pom_label.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        pom_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        pom_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# COUNTDOWN
def count_down(count):
    global timer
    count_min = int(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=str(count_min) + ":" + str(count_sec))
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(int(reps / 2)):
            marks += "✔️"
        check_mark.config(text=marks)


# Tk WINDOW SETUP

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100)
window.config(bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill=WHITE, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

pom_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
pom_label.grid(column=1, row=0)

start = Button(text="Start", bg=WHITE, font=("Arial", 12), command=start_timer, highlightthickness=0)
start.grid(column=0, row=2)

reset = Button(text="Reset", bg=WHITE, font=("Arial", 12), command=reset_timer, highlightthickness=0)
reset.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()
