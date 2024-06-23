from tkinter import *
from center import center
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
import webbrowser

# page imports
from meditator import meditate
from survey import survey
from gratitude import gratitude


def survey_gap():
    survey()
    
def gratitude_gap():
    gratitude()

def be_happy():
    webbrowser.open('https://www.youtube.com/watch?v=iik25wqIuFo')

def meditate_gap():
    meditate()

# Open image
original_image = Image.open('serene-logo.png')
# Resize the image to fit within 100x100 pixels
resized_image = original_image.resize((100, 100), Image.LANCZOS)

# global constants
LOGO_IMG = ImageTk.PhotoImage(resized_image)
DB_NAME = 'serenity_scope'
USER_NAME = ''


# # MySQL starts
# db = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='MlysqlSka999%'
# )
#
# cursor = db.cursor()
#
# cursor.execute('show databases')
#
# if (DB_NAME,) not in cursor.fetchall():
#     cursor.execute(f'create database {DB_NAME};')
#     cursor.execute(f'use {DB_NAME};')
#     cursor_prompt = "create table(user_data(user_id int(3), user_name varchar(20), user_pin int(6))"
#     db.commit()
# else:
#     cursor.execute(f'use {DB_NAME}')
#
#
# # MySQL ends


# noinspection PyGlobalUndefined
def signin_page():
    global signin_page_var, username, pin
    signin_page_var = Toplevel()
    signin_page_var.title("Signin Page")
    signin_page_var.geometry("800x800")
    signin_page_var.config(bg='#BBDEE7')
    signin_page_var.iconbitmap('serene-logo.ico')
    center(signin_page_var)

    label = Label(signin_page_var, height=100, width=100, image=LOGO_IMG)
    label.place(x=350, y=50)

    frame = Frame(signin_page_var, width=350, height=350, background='white')
    frame.place(x=225, y=225)

    heading = Label(frame, text='Sign in', background='white', foreground='black', font=("Arial", 24))
    heading.place(x=100, y=10)

    username = Entry(frame, width=25, background='white', foreground='black', border=0, font=("Arial", 11))
    username.place(x=30, y=80)
    username.insert(0, 'Username')

    Frame(frame, width=295, height=2, background='black').place(x=25, y=107)

    pin = Entry(frame, width=25, background='white', foreground='black', border=0, font=("Arial", 11))
    pin.place(x=30, y=150)
    pin.insert(0, 'PIN')

    Frame(frame, width=295, height=2, background='black').place(x=25, y=177)

    sign_in_button = Button(frame, width=25, pady=8, text='Sign in', background='black', foreground='white',
                            border=0, command=signin)
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

    left_eye = Frame(home_page_var, width=150, height=150, background='white')
    left_eye.place(x=150, y=150)

    survey = Button(left_eye, width=5, pady=8, text='Take our survey', background='black', foreground='white', border=0, command=survey_gap)
    survey.place(x=35, y=35)

    right_eye = Frame(home_page_var, width=150, height=150, background='white')
    right_eye.place(x=500, y=150)

    journal = Button(right_eye, width=2, pady=8, text='Write a entry', background='black', foreground='white', border=0, command=gratitude_gap)
    journal.place(x=35, y=35)

    nose = Frame(home_page_var, width=80, height=80, background='white')
    nose.place(x=360, y=375)

    be_happy_btn = Button(nose, width=2, pady=8, text='Be happy', background='black', foreground='white', border=0, command=be_happy)
    be_happy_btn.place(x=35, y=35)

    mouth = Frame(home_page_var, width=350, height=150, background='white')
    mouth.place(x=225, y=525)

    meditate = Button(mouth, width=2, pady=8, text='Meditate', background='black', foreground='white', border=0, command=meditate_gap)
    meditate.place(x=35, y=35)

    sign_out = Frame(home_page_var, width=25, height=25, background='white')
    sign_out.place(x=750, y=50)

    sign_out_btn = Button(sign_out, width=2, pady=8, text='Sign out', background='black', foreground='white', border=0)
    sign_out_btn.place(x=15, y=15)


def signup(user_name, user_pin):
    """Adds user to the database"""
    # cursor.execute('select * from user_data')
    # user_data = cursor.fetchall()
    # user_list = [i[1] for i in user_data]
    #
    # if user_name not in user_list:
    #     cursor.execute('select * from user_data order by user_id desc limit 1;')
    #     user_id = cursor.fetchall()[0][0] + 1  # Set user id after incrementing from last user
    #
    #     cursor.execute(f"insert into user_data values({user_id}, '{user_name}', '{user_pin}');")  # add data
    #     message = f"""You have signed up to SerenityScope successfully!
    #     User ID: {user_id}  (You won't need this)
    #     User Name: {user_name}  (Remember this)
    #     PIN: {user_pin} (And this)
    #     """
    #     messagebox.showinfo(title='Signed Up!', message=message)
    #
    #
    # else:
    #     messagebox.showerror(title='Already Exists!', message=f"A user with the username {user_name} already exists!")
    #
    # signup('yolomsikka', '123987')

    signup_page_var.withdraw()
    signin_page_var.deiconify()


def signin():
    # global USER_NAME
    #
    # user_name = username.get()
    # input_pin = pin.get()
    #
    # cursor.execute('select * from user_data')
    # user_data = cursor.fetchall()
    # user_list = [i[1] for i in user_data]
    #
    # if user_name in user_list:
    #     user_pin = cursor.execute(f"select user_pin from user_data where user_name = '{user_name}'")
    #     if user_pin == input_pin:
    #         USER_NAME = user_name
    #         home_page()
    #     else:
    #         messagebox.showerror('Incorrect PIN!', 'The PIN you have entered is incorrect.')
    # else:
    #     messagebox.showerror('Does Not Exist!', f"A user with the username {user_name} does not exist!")
    #
    # db.commit()
    home_page()
