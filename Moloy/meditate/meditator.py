from tkinter import *
from tkinter import messagebox
import pygame

try:
    pygame.mixer.init()
except pygame.error:
    messagebox.showerror('No Speakers!', 'An audio output device is required for SerenityScope.')


reps = 0
timer = None
started = False
BG_COLOR = '#BBDEE7'
BUTTON_PRESSED = '#A6E3E9'
meditate_min = 10
tranquil = pygame.mixer.Sound("Glance_Out_A_Casement_Window.mp3")
binaural = pygame.mixer.Sound("binaural-beats.mp3")


def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    _x = win.winfo_screenwidth() // 2 - win_width // 2
    _y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, _x, _y))
    win.deiconify()


def end_timer():
    global reps, started
    end_audio()
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

        meditate_sec = meditate_min * 60
        play_audio()

        count_down(meditate_sec)


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
    if audio_to_play.get() == 0:
        tranquil.play(loops=-1)
    elif audio_to_play.get() == 1:
        binaural.play(loops=-1)
    pygame.mixer.music.set_volume(50 / 100)


def end_audio():
    pygame.mixer.stop()


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
end_button = Button(window, text='End', command=end_timer, padx=20, pady=20, bg=BG_COLOR,
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

end_button.pack()
end_button.update()
end_width = end_button.winfo_width()
end_height = end_button.winfo_height()
x = ((800 - end_width) // 4) * 3
end_button.place(x=x, y=600)

audio_to_play = IntVar()
options = ['Tranquil Music', 'Binaural Beats (40 Hz)', 'No audio']

radio_button_tranquil = Radiobutton(window, text=options[0], variable=audio_to_play, value=0, bg=BG_COLOR,
                                    activebackground=BUTTON_PRESSED)
radio_button_tranquil.pack()
radio_button_tranquil.place(x=0, y=720)

radio_button_binaural = Radiobutton(window, text=options[1], variable=audio_to_play, value=1, bg=BG_COLOR,
                                    activebackground=BUTTON_PRESSED)
radio_button_tranquil.update()
radio_height = radio_button_tranquil.winfo_height()
radio_button_binaural.pack()
radio_button_binaural.place(x=0, y=720 + radio_height)

radio_button_none = Radiobutton(window, text=options[2], variable=audio_to_play, value=2, bg=BG_COLOR,
                                activebackground=BUTTON_PRESSED)
radio_button_none.pack()
radio_button_none.place(x=0, y=720 + 2 * radio_height)

center(window)
window.mainloop()
