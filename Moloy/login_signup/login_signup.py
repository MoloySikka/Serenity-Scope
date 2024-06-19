import mysql.connector
from tkinter import messagebox

DB_NAME = 'serenity_scope'

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
    cursor_prompt = "create table(user_data(user_id int(3), user_name varchar(20), user_pin int(6))"
    db.commit()
else:
    cursor.execute(f'use {DB_NAME}')


def sign_up(user_name, user_pin):
    """Adds user to the database"""
    cursor.execute('select * from user_data')
    user_data = cursor.fetchall()
    user_list = [i[1] for i in user_data]

    if user_name not in user_list:
        cursor.execute('select * from user_data order by user_id desc limit 1;')
        user_id = cursor.fetchall()[0][0] + 1  # Set user id after incrementing from last user

        cursor.execute(f"insert into user_data values({user_id}, '{user_name}', '{user_pin}');")  # add data
        message = f"""You have signed up to SerenityScope successfully!
        User ID: {user_id}  (You won't need this)
        User Name: {user_name}  (Remember this)
        PIN: {user_pin} (And this)
        """
        messagebox.showinfo(title='Signed Up!', message=message)

    else:
        messagebox.showerror(title='Already Exists!', message=f"A user with the username {user_name} already exists!")

    db.commit()


# sign_up('yelyah', '123456')

# Incomplete
# def log_in(user_name, user_pin):
#     cursor.execute('select * from user_data')
#     user_data = cursor.fetchall()
#     user_list = [i[1] for i in user_data]
#
#     if user_name in user_list:
#         cursor.execute('select * from user_data order by user_id desc limit 1;')
#         user_id = cursor.fetchall()[0][0] + 1  # Set user id after incrementing from last user
#
#         cursor.execute(f"insert into user_data values({user_id}, '{user_name}', '{user_pin}');")  # add data
#         message = f"""You have signed up to SerenityScope successfully!
#             User ID: {user_id}  (You won't need this)
#             User Name: {user_name}  (Remember this)
#             PIN: {user_pin} (And this)
#             """
#         messagebox.showinfo(title='Signed Up!', message=message)
#
#     else:
#         messagebox.showerror(title='Does Not Exist!', message=f"A user with the username {user_name} does not exist!")
#
#     db.commit()
