from tkinter import *

reps = 0
timer = None


def reset_timer():
    global reps
    # noinspection PyTypeChecker
    window.after_cancel(timer)
    title.config(text="Timer")
    timer_label.config(text="00:00")
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

    timer_label.config(text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        window.attributes("-topmost", True)
        window.attributes("-topmost", False)
        start_timer()


window = Tk()
window.config(bg='#BBDEE7')
window.geometry('800x800')
window.resizable(False, False)
window.iconbitmap("serene-icon.ico")

window.title("Meditate")

# Timer text label replacing the canvas
timer_label = Label(window, text="00:00", font=('Courier', 35, 'bold'))

# Timer title label
title = Label(window, text='meditate', font=('KG Keep Your Head Up', 55, 'normal'), bg='#BBDEE7')

# Buttons
start_button = Button(window, text='Start', command=start_timer, padx=20, pady=20)
reset_button = Button(window, text='Reset', command=reset_timer, padx=20, pady=20)

# Placing
title.pack()
title.update()
title_width = title.winfo_width()
x = (800 - title_width  ) // 2
title.place(x=x, y=180)

timer_label.place()
start_button.place()
reset_button.place()

window.mainloop()
