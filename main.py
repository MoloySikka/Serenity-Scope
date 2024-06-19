import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
import time

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


root=tk.Tk()

root.geometry('800x800')
root.title('Serenity Scope')
root.config(bg='#BBDEE7')
center(root)

# Might have to do the icon for every page individually
# icon = tk.PhotoImage(file="logo.jpeg")
# root.iconphoto(True, icon)

# Animation plays

root.withdraw()

def on_leave(e):
    name=username.get()


def signin_page():
    global signin_page_var
    signin_page_var = Toplevel()
    signin_page_var.title("Signin Page")
    signin_page_var.geometry("800x800")
    signin_page_var.config(bg='#BBDEE7')
    center(signin_page_var)
    logo_img = tk.PhotoImage(file='logo.png')
    label=tk.Label(signin_page_var, height=100, width=100, image=logo_img)
    label.place(x=350, y=50)

    frame=tk.Frame(signin_page_var, width=350, height=350, background='white')
    frame.place(x=225, y=225)

    heading=tk.Label(frame, text='Sign in', background='white', foreground='black', font=("Arial", 24))
    heading.place(x=100, y=10)

    username = tk.Entry(frame, width=25, background='white', foreground='black', border=0, font=("Arial", 11))
    username.place(x=30, y=80)
    username.insert(0, 'Username')

    tk.Frame(frame, width=295, height=2, background='black').place(x=25, y=107)

    password = tk.Entry(frame, width=25, background='white', foreground='black', border=0, font=("Arial", 11))
    password.place(x=30, y=150)
    password.insert(0, 'Password')

    tk.Frame(frame, width=295, height=2, background='black').place(x=25, y=177)

    tk.Button(frame, width=25, pady=8, text='Sign in', background='black', foreground='white', border=0, command=home_page).place(x=35, y=210)
 
    label2=tk.Label(frame, text="Don't have an account?",background='white', foreground='black', height=100, width=100, font=("Arial", 11))
    label2.place(x=75, y=270)

    tk.Button(frame, width=6, text='Sign up', background='white', foreground='black', border=0, cursor="hand2").place(x=215, y=270)

def signup_page():
    signin_page_var.withdraw()
    global signup_page_var
    signup_page_var = Toplevel()
    signup_page_var.title("Signup Page")
    signup_page_var.geometry("800x800")
    signup_page_var.config(bg='#BBDEE7')
    center(signup_page_var)

def home_page():
    signin_page_var.withdraw()
    global home_page_var
    home_page_var = Toplevel()
    home_page_var.title("Home Page")
    home_page_var.geometry("800x800")
    home_page_var.config(bg='#BBDEE7')
    center(home_page_var)

# Show the window by writing signin_page_var.deiconify()
 

signin_page()

root.mainloop()
