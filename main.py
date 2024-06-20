from tkinter import *

# UI function imports
from center import center
from ui_functions import signin_page

root = Tk()

root.geometry('800x800')
root.title('Serenity Scope')
root.config(bg='#BBDEE7')
center(root)

# Might have to do the icon for every page individually
root.iconbitmap('serene-logo.ico')

# Animation plays

root.withdraw()

# Show the window by writing signin_page_var.deiconify()


signin_page()

root.mainloop()
