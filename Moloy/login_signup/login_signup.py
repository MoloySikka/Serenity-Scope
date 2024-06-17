import mysql.connector

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
    cursor.execute('select * from user_data order by user_id desc limit 1;')
    user_id = cursor.fetchall()[0][0] + 1  # Set user id after incrementing from last user

    cursor.execute(f"insert into user_data values({user_id}, '{user_name}', '{user_pin}');")  # add data

    db.commit()


sign_up('moloy', '132435')
