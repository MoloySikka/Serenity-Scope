from tkinter import *
from center import center
from PIL import Image, ImageTk

# Open image
original_image = Image.open('serene-logo.png')
# Resize the image to fit within 100x100 pixels
resized_image = original_image.resize((100, 100), Image.LANCZOS)
logo_img = ImageTk.PhotoImage(resized_image)


# noinspection PyGlobalUndefined
def signin_page():
    global signin_page_var, username
    signin_page_var = Toplevel()
    signin_page_var.title("Signin Page")
    signin_page_var.geometry("800x800")
    signin_page_var.config(bg='#BBDEE7')
    signin_page_var.iconbitmap('serene-logo.ico')
    center(signin_page_var)

    label = Label(signin_page_var, height=100, width=100, image=logo_img)
    label.place(x=350, y=50)

    frame = Frame(signin_page_var, width=350, height=350, background='white')
    frame.place(x=225, y=225)

    heading = Label(frame, text='Sign in', background='white', foreground='black', font=("Arial", 24))
    heading.place(x=100, y=10)

    username = Entry(frame, width=25, background='white', foreground='black', border=0, font=("Arial", 11))
    username.place(x=30, y=80)
    username.insert(0, 'Username')

    Frame(frame, width=295, height=2, background='black').place(x=25, y=107)

    password = Entry(frame, width=25, background='white', foreground='black', border=0, font=("Arial", 11))
    password.place(x=30, y=150)
    password.insert(0, 'Password')

    Frame(frame, width=295, height=2, background='black').place(x=25, y=177)

    sign_in_button = Button(frame, width=25, pady=8, text='Sign in', background='black', foreground='white',
                            border=0, command=home_page)
    sign_in_button.place(x=35, y=210)

    label2 = Label(frame, text="Don't have an account?", background='white', foreground='black', height=100,
                   width=100, font=("Arial", 11))
    label2.place(x=75, y=270)

    sign_up_button = Button(frame, width=6, text='Sign up', background='white', foreground='black', border=0,
                            cursor="hand2", command=signup_page)
    sign_up_button.place(x=215, y=270)

    signin_page_var.attributes('-topmost', True)
    signin_page_var.attributes('-topmost', False)


# noinspection PyGlobalUndefined
def signup_page():
    signin_page_var.withdraw()
    global signup_page_var
    signup_page_var = Toplevel()
    signup_page_var.title("Signup Page")
    signup_page_var.geometry("800x800")
    signup_page_var.config(bg='#BBDEE7')
    signup_page_var.iconbitmap('serene-logo.ico')
    center(signup_page_var)


# noinspection PyGlobalUndefined
def home_page():
    signin_page_var.withdraw()
    global home_page_var
    home_page_var = Toplevel()
    home_page_var.title("Home Page")
    home_page_var.geometry("800x800")
    home_page_var.config(bg='#BBDEE7')
    home_page_var.iconbitmap('serene-logo.ico')
    center(home_page_var)


def on_leave(e):
    name = username.get()
