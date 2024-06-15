from tkinter import *

reps = 0
timer = None


def reset_timer():
    global reps
    # noinspection PyTypeChecker
    window.after_cancel(timer)
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    # checks.config(text="")
    reps = 0


def start_timer():
    global reps
    reps += 1

    work_sec = 30 * 60

    count_down(work_sec)
    title.config(text="Work")


def count_down(count):
    global reps, timer

    count_min = count // 60 if count // 60 > 9 else f"0{count // 60}"
    count_sec = count % 60 if count % 60 > 9 else f"0{count % 60}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        window.attributes("-topmost", True)
        window.attributes("-topmost", False)
        start_timer()


window = Tk()
window.geometry('800x800')
window.resizable(False, False)
window.iconbitmap("serene-icon.ico")

window.title("Meditate")

# canvas
canvas = Canvas(width=800, height=600, highlightthickness=0)

# back_serenity = PhotoImage(file='tomato.png')

# canvas.create_image(100, 112, image=back_serenity)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=('Courier', 35, 'bold'))

canvas.grid(column=1, row=1)

# timer
title = Label(text='Timer', font=('Courier', 50, 'bold'))
# title.config(fg=GREEN, bg=YELLOW)

title.grid(column=1, row=0)

# buttons
start_button = Button(text='Start', command=start_timer)
# start_button.config(bg=YELLOW, highlightthickness=0)

start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset_timer)
# reset_button.config(bg=YELLOW, highlightthickness=0)

reset_button.grid(column=2, row=2)

window.mainloop()
