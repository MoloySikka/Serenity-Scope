from tkinter import *
import pygame

reps = 0
timer = None
started = False
BG_COLOR = '#BBDEE7'
BUTTON_PRESSED = '#A6E3E9'
pygame.mixer.init()
MEDITATE_MIN = 10


def reset_timer():
    global reps, started
    stop_audio()
    started = False
    # noinspection PyTypeChecker
    window.after_cancel(timer)
    timer_label.config(text="00:00")
    reps = 0


def start_timer():
    global reps, started
    if not started:
        started = True
        reps += 1

        work_sec = MEDITATE_MIN * 60
        play_audio()

        count_down(work_sec)


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


def title_place():
    title.update()
    title_width = title.winfo_width()
    _x = (800 - title_width) // 2
    title.place(x=_x, y=125)


def play_audio():
    pygame.mixer.music.load("binaural-beats.mp3")
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(50 / 100)


def stop_audio():
    pygame.mixer.music.stop()


window = Tk()
window.config(bg=BG_COLOR)
window.geometry('800x800')
window.resizable(False, False)
window.iconbitmap("serene-icon.ico")

window.title("Meditate")

# Timer text label replacing the canvas
timer_label = Label(window, text="00:00", font=("Lovehearts XYZ", 60, 'normal'), bg=BG_COLOR)

# Timer title label
title = Label(window, text='meditate', font=('KG Keep Your Head Up', 55, 'bold'), bg=BG_COLOR)

# Buttons
start_button = Button(window, text='Start', command=start_timer, padx=20, pady=20, bg=BG_COLOR,
                      activebackground=BUTTON_PRESSED)
reset_button = Button(window, text='Reset', command=reset_timer, padx=20, pady=20, bg=BG_COLOR,
                      activebackground=BUTTON_PRESSED)

# Placing
title.pack()
title_place()

timer_label.pack()
timer_label.update()
timer_width = timer_label.winfo_width()
timer_height = timer_label.winfo_height()
x = (800 - timer_width) // 2
timer_label.place(x=x, y=360)

start_button.pack()
start_button.update()
start_width = start_button.winfo_width()
start_height = start_button.winfo_height()
x = (800 - start_width) // 4
start_button.place(x=x, y=600)

reset_button.pack()
reset_button.update()
reset_width = reset_button.winfo_width()
reset_height = reset_button.winfo_height()
x = ((800 - reset_width) // 4) * 3
reset_button.place(x=x, y=600)

window.mainloop()
