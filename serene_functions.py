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

COLOURS = {'grey': '#f7f7f7', 'fr blue': '#0479D8', 'pic blue': '#55AEE1', 'mauve': '#D6CDEA', 'l blue': '#A6E3E9',
           'l mauve': '#D0D9E4', 'l brick': '#D9ABA2', 'brick': '#E27D60'}


def survey_gap():
    survey()


def gratitude_gap():
    gratitude()


def be_happy():
    webbrowser.open('https://www.youtube.com/watch?v=iik25wqIuFo')


def meditate_gap():
    meditate()


# Open images
original_image_1 = Image.open('serene-logo.png')
original_image_2 = Image.open('log-out.png')
# Resize the images to fit
resized_image_1 = original_image_1.resize((100, 100), Image.LANCZOS)
resized_image_2 = original_image_2.resize((40, 40), Image.LANCZOS)

# global constants
LOGO_IMG = ImageTk.PhotoImage(resized_image_1)
LOGOUT_IMG = ImageTk.PhotoImage(resized_image_2)
DB_NAME = 'serenity_scope'
USER_NAME = ''
BG_COLOR = COLOURS['mauve']
BG_ALT = COLOURS['l mauve']

# MySQL config starts
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='MlysqlSka999%'
)

cursor = db.cursor()

cursor.execute('show databases')

if (DB_NAME,) not in cursor.fetchall():
    cursor.execute(f'create database {DB_NAME};')
    cursor.execute(f'use {DB_NAME};')
    cursor_prompt = ("create table user_data(user_id int(3), user_name varchar(20) collate utf8mb4_bin, "
                     "user_pin int(6));")
    cursor.execute(cursor_prompt)
    db.commit()
else:
    cursor.execute(f'use {DB_NAME}')


# MySQL config ends


# noinspection PyGlobalUndefined
def signin_page():
    global signin_page_var, username, pin
    signin_page_var = Toplevel()
    signin_page_var.title("Signin Page")
    signin_page_var.geometry("800x800")
    signin_page_var.config(bg=BG_COLOR)
    signin_page_var.iconbitmap('serene-logo.ico')
    signin_page_var.resizable(False, False)
    center(signin_page_var)

    label = Label(signin_page_var, height=100, width=100, image=LOGO_IMG)
    label.place(x=350, y=50)

    frame = Frame(signin_page_var, width=350, height=350, background='white')
    frame.place(x=225, y=225)

    heading = Label(frame, text='Sign in', background='white', foreground='black', font=("Romeo", 24))
    heading.place(x=100, y=10)

    username = Entry(frame, width=25, background='white', foreground='black', border=0, font=("Romeo", 11))
    username.place(x=30, y=80)
    username.insert(0, 'Username')

    Frame(frame, width=295, height=2, background='black').place(x=25, y=107)

    pin = Entry(frame, width=25, background='white', foreground='black', border=0, font=("Romeo", 11))
    pin.place(x=30, y=150)
    pin.insert(0, '6-digit PIN')

    Frame(frame, width=295, height=2, background='black').place(x=25, y=177)

    signin_button = Button(frame, width=25, pady=8, text='Sign in', background='black', foreground='white',
                           border=0, command=signin)
    signin_button.place(x=35, y=210)

    signup_button = Button(frame, width=6, text='Sign up', background='white', foreground='black', border=0,
                           cursor="hand2", command=signup_page)
    signup_button.place(x=250, y=270)

    try:
        signup_page_var.withdraw()
    except NameError:
        pass
    signin_page_var.attributes('-topmost', True)
    signin_page_var.attributes('-topmost', False)


# noinspection PyGlobalUndefined
def signup_page():
    global signup_page_var, username, pin
    signup_page_var = Toplevel()
    signup_page_var.title("Signup Page")
    signup_page_var.geometry("800x800")
    signup_page_var.config(bg=BG_COLOR)
    signup_page_var.iconbitmap('serene-logo.ico')
    signup_page_var.resizable(False, False)
    center(signup_page_var)

    label = Label(signup_page_var, height=100, width=100, image=LOGO_IMG)
    label.place(x=350, y=50)

    frame = Frame(signup_page_var, width=350, height=350, background='white')
    frame.place(x=225, y=225)

    heading = Label(frame, text='Sign up', background='white', foreground='black', font=("Romeo", 24))
    heading.place(x=100, y=10)

    username = Entry(frame, width=25, background='white', foreground='black', border=0, font=("Romeo", 11))
    username.place(x=30, y=80)
    username.insert(0, 'Username')

    Frame(frame, width=295, height=2, background='black').place(x=25, y=107)

    pin = Entry(frame, width=25, background='white', foreground='black', border=0, font=("Romeo", 11))
    pin.place(x=30, y=150)
    pin.insert(0, '6-digit PIN')

    Frame(frame, width=295, height=2, background='black').place(x=25, y=177)

    signup_button = Button(frame, width=25, pady=8, text='Sign up', background='black', foreground='white',
                           border=0, command=signup)
    signup_button.place(x=35, y=210)

    signin_button = Button(frame, width=6, text='Sign in', background='white', foreground='black', border=0,
                           cursor="hand2", command=signin_page)
    signin_button.place(x=250, y=270)

    signin_page_var.withdraw()
    signup_page_var.attributes('-topmost', True)
    signup_page_var.attributes('-topmost', False)


# noinspection PyGlobalUndefined
def home_page():
    signin_page_var.withdraw()
    global home_page_var
    home_page_var = Toplevel()
    home_page_var.title("Home Page")
    home_page_var.geometry("800x800")
    home_page_var.config(bg=BG_COLOR)
    home_page_var.iconbitmap('serene-logo.ico')
    home_page_var.resizable(False, False)
    center(home_page_var)

    left_eye = Frame(home_page_var, width=150, height=150, background='white')
    left_eye.place(x=150, y=150)

    survey_button = Button(left_eye, padx=35, pady=65, text='Take our survey',
                           border=0, command=survey_gap, font=('Romeo', 10, 'normal'),
                           activebackground=COLOURS['fr blue'], activeforeground='white', foreground='black',
                           background=COLOURS['pic blue'])
    survey_button.pack(fill=BOTH, expand=True)

    right_eye = Frame(home_page_var, width=150, height=150, background='white')
    right_eye.place(x=500, y=150)

    journal = Button(right_eye, padx=39, pady=65, text='Write an entry',
                     border=0, command=gratitude_gap, activebackground=COLOURS['fr blue'], activeforeground='white',
                     font=('Romeo', 10, 'normal'), foreground='black',
                     background=COLOURS['pic blue'])
    journal.pack(fill=BOTH, expand=True)

    nose = Frame(home_page_var, width=80, height=80, background='white')
    nose.place(x=360, y=375)

    be_happy_btn = Button(nose, padx=13, pady=30, text='Be happy',
                          border=0, command=be_happy, activebackground=COLOURS['fr blue'], activeforeground='white',
                          font=('Romeo', 10, 'normal'), foreground='black',
                          background=COLOURS['pic blue'])
    be_happy_btn.pack(fill=BOTH, expand=True)

    mouth = Frame(home_page_var, width=350, height=150, background='white')
    mouth.place(x=225, y=525)

    meditate_button = Button(mouth, padx=123, pady=65, text='Meditate', activebackground=COLOURS['fr blue'],
                             activeforeground='white', foreground='black',
                             font=('Romeo', 20, 'normal'), background=COLOURS['pic blue'],
                             border=0, command=meditate_gap)
    meditate_button.pack(fill=BOTH, expand=True)

    sign_out = Frame(home_page_var, width=40, height=40, background='white')
    sign_out.place(x=15, y=35)

    sign_out_btn = Button(sign_out, width=40, height=40, background=BG_COLOR, image=LOGOUT_IMG,
                          activebackground=BG_ALT, border=0, command=signout)
    sign_out_btn.pack(fill=BOTH, expand=True)

    username_label = Label(home_page_var, text=USER_NAME, background=BG_COLOR, font=('Arial', 10, 'bold'))
    username_label.place(x=12, y=10)


def signout():
    home_page_var.withdraw()
    signin_page_var.deiconify()
    pin.delete(0, END)
    pin.insert(0, '6-digit PIN')


def signup():
    """Adds user to the database"""

    user_name = username.get()
    input_pin = pin.get()

    cursor.execute('select * from user_data')
    user_data = cursor.fetchall()
    user_list = [i[1] for i in user_data]

    if user_name not in user_list:
        cursor.execute('select * from user_data order by user_id desc limit 1;')
        try:
            user_id = cursor.fetchall()[0][0] + 1  # Set user id after incrementing from last user
        except IndexError:
            user_id = 1

        cursor.execute(f"insert into user_data values({user_id}, '{user_name}', '{input_pin}');")  # add data
        message = f"""You have signed up to SerenityScope successfully!
        User ID: {user_id}  (You won't need this)
        User Name: {user_name}  (Remember this)
        6-digit PIN: {input_pin} (And this)
        """
        messagebox.showinfo(title='Signed Up!', message=message)

    else:
        messagebox.showerror(title='Already Exists!', message=f"A user with the username {user_name} already exists!")

    db.commit()
    signup_page_var.withdraw()
    signin_page_var.deiconify()


def signin():
    global USER_NAME

    user_name = username.get()
    input_pin = int(pin.get())

    cursor.execute('select * from user_data')
    user_data = cursor.fetchall()
    user_list = [i[1] for i in user_data]

    if user_name in user_list:
        cursor.execute(f"select user_pin from user_data where user_name = '{user_name}'")
        user_pin = cursor.fetchall()[0][0]
        if user_pin == input_pin:
            USER_NAME = user_name
            home_page()
        else:
            messagebox.showerror('Incorrect 6-digit PIN!', 'The 6-digit PIN you have entered is incorrect.')
    else:
        messagebox.showerror('Does Not Exist!', f"A user with the username {user_name} does not exist!")

    db.commit()
