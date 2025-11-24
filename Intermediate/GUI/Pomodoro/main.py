'''
# The Pomodoro Technique
1. Decide on the task to be done
2. Set the timer to 25 minutes
3. Work on the task until the timer rings
4. Take a short 5-minute break
5. After four cycles, take a 15–30 minute long break.

# Canvas Widget – Used to layer objects (images/text) on top of each other
'''

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# Work & break durations (in minutes)
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0      # Counts number of Pomodoro sessions completed
timer = None  # Stores reference to the running 'after' timer


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Stops the timer and resets the UI + repetition counter."""
    window.after_cancel(timer)

    # Corrected spelling: itemconfig (not itemconfgi)
    canvas.itemconfig(timer_text, text="00:00")

    title_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")

    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Starts a new Pomodoro cycle based on the repetition count."""
    global reps
    reps += 1

    # Convert minutes to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Every 8 reps → long break
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)

    # Every even rep (2, 4, 6...) → short break
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)

    # Every odd rep (1, 3, 5...) → work session
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Handles countdown behavior and updates the timer display every second."""
    
    # Convert seconds into min:sec format
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Add a leading zero (e.g. 07 instead of 7)
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    # If time still remains, schedule next tick after 1 second
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # When countdown finishes, start next session
        start_timer()

        # Display check marks for each completed work session
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

'''
Example of how `after()` schedules a function call:
def say_something(thing):
    print(thing)
window.after(1000, say_something, "Hello")
'''

# Title label ("Timer", "Work", or "Break")
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# Canvas for tomato image and timer text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)  # Centered image
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Reset button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Check mark label for completed cycles
check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()

# GUI programs run an infinite event loop (mainloop),
# constantly listening for user interactions/events such as button clicks.
