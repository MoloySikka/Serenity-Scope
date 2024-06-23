from tkinter import *
from center import center
import tkinter as tk

import pickle
from datetime import datetime

# Check if entry question has already been done 
#fog=open("user_journal_entries.dat", "rb")
#user_journal_entries = pickle.load(fog)
#fog.close()


journal_questions = [
"Write about a time when you laughed uncontrollably.",
"Appreciate a friend who lives far away but is dear to you.",
"What is the best gift that you have ever received?",
"Write about a movie that touched your heart, and why.",
"Write about someone that you really admire.",
"Appreciate a refreshing walk that you had in nature.",
"What do you like most about yourself?",
"What do you love most about the time you are living in?",
"Express gratitude for having as much food as you need.",
"Appreciate the vehicles that let you travel long distances.",
"Express gratitude for the facility of ordering food at your doorstep and the people who deliver it.",
"Look around and list 5 things that help you in your day-to-day life.",
"List 5 ways that having a mobile phone makes your life easier.",
"Express gratitude for 5 things that you use daily.",
"Write about an electronic device that you feel grateful to have.",
"What is one thing about the Internet that you admire?",
"What is something that you can do today that people 30 years ago couldn't?",
"Think about the people you don't know who help make your life easier.",
"List 5 things in your bedroom that you are grateful for.",
"Express gratitude for 5 tools that help you save time.",
"What privilege do you enjoy that others might not?",
"Write about a song that you can't help but sing along to.",
"What is your favourite thing to do in your free time?",
"What was the most enjoyable part of your childhood?",
"What aspect of your health do you feel grateful for?",
"Whose company do you like the most?",
"What excites you about the future?",
"Who is the most reliable person in your life?",
"When did something wonderful happen unexpectedly?",
"Appreciate a stranger who was helping someone in need.",
"Write about the most influential people in your life.",
"Write about an achievement that you are most proud of.",
"Write about something that makes you feel lucky.",
"Write about a recent improvement in your lifestyle.",
"Write about something beautiful that moved you to tears.",
"What is the funniest video you've watched recently?",
"Write about a time when you challenged your comfort zone.",
"What is your favourite part about your town or city?",
"What do you like about growing up?",
"Which is your favourite weather, and why?",
"What is the most fascinating thing about life?",
"What is one skill or quality about yourself that you appreciate the most?",
"Express gratitude to yourself and the journey you're having.",
"Write about someone that you idolise, and why.",
"What are you always excited to do?",
"What is your strongest life value?",
"Write about one positive thing that happened today.",
"What is your favourite part of your life?",
"Which recent experience in life taught you a big lesson?",
"What is your most prized possession?"]


def add_entry(question, entry):
    f_=open("user_journal_entries.dat", "ab")
    user_journal_entries.update({question: [datetime.now().strftime("%B %d, %Y"), datetime.now().strftime("%H:%M:%S"), entry]})
    pickle.dump(user_journal_entries, f_)
    f_.close()


def gratitude():
    global gratitude_var
    gratitude_var = Toplevel()
    gratitude_var.title("Gratitude Journaling Page")
    gratitude_var.geometry("800x800")
    gratitude_var.config(bg='#BBDEE7')
    gratitude_var.iconbitmap('serene-logo.ico')
    center(gratitude_var)

    label1 = Label(gratitude_var, height=3, width=30, text="Gratitude Journaling")
    label1.place(x=275, y=50)

    label2 = Label(gratitude_var, height=3, text=journal_questions[len(list(user_journal_entries.keys()))])
    label2.place(x=275, y=150)

    inputtxt = Text(gratitude_var, height = 20, width = 45, bg = "#8DEBB0", bd=0, font=('Gotham Circular',20))
    inputtxt.place(x=100, y=250)

    submit_btn = Button(gratitude_var, width=8, pady=8, text='Submit', background='black', foreground='white', border=0, command=lambda: add_entry(journal_questions[len(list(user_journal_entries.keys()))], inputtxt.get('1.0',tk.END)))
    submit_btn.place(x=335, y=750)

    old_entries_btn = Button(gratitude_var, width=8, pady=8, text='View old entries', background='black', foreground='white', border=0, command=old_entries)
    old_entries_btn.place(x=685, y=15)


def old_entries():
    global old_entries_var
    old_entries_var = Toplevel()
    old_entries_var.title("Gratitude Journaling Old Entries")
    old_entries_var.geometry("800x800")
    old_entries_var.config(bg='#BBDEE7')
    old_entries_var.iconbitmap('serene-logo.ico')
    center(old_entries_var)

    y_pos=50
    
    label1 = Label(old_entries_var, height=3, width=70, text="Here are your journal entries:")
    label1.place(x=75, y=y_pos)

    y_pos+=50

    for key, value in user_journal_entries.items():
        label2 = Label(old_entries_var, height=3, width=70, text=str(list(user_journal_entries.keys()).index(key) + 1) +". "+key)
        label2.place(x=75, y=y_pos)

        y_pos+=50

        label3 = Label(old_entries_var, height=3, width=70, text='Date: '+ value[0]+ '\nTime: '+ value[1])
        label3.place(x=75, y=y_pos)   

        y_pos+=50
        
        label4 = Label(old_entries_var, width=70, text='Entry: '+ value[2]+ '\n', wraplength=250)
        label4.place(x=75, y=y_pos)

        y_pos+=100

        






    
