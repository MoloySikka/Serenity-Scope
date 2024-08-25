from tkinter import *

# UI function imports
from center import center
root = Tk()
from serene_functions import signin_page

root.geometry('800x800')
root.title('Serenity Scope')
root.config(bg='#BBDEE7')
center(root)

root.iconbitmap('serene-logo.ico')

root.withdraw()

signin_page()

root.mainloop()
