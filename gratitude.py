from tkinter import *
from center import center

import pickle
from datetime import datetime

try:
    with open("user_journal_entries.dat", "rb") as f:
        user_journal_entries = pickle.load(f)
except FileNotFoundError:
    with open('user_journal_entries.dat', 'wb') as f:
        user_journal_entries = {}
        pickle.dump({}, f)

COLOURS = {'grey': '#f7f7f7', 'fr blue': '#0479D8', 'pic blue': '#55AEE1', 'mauve': '#D6CDEA', 'l blue': '#A6E3E9',
           'l mauve': '#D0D9E4', 'l brick': '#D9ABA2', 'brick': '#E27D60'}

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
    user_journal_entries.update(
        {question: [datetime.now().strftime("%B %d, %Y"), datetime.now().strftime("%H:%M:%S"), entry]})
    with open('user_journal_entries.dat', 'wb') as f_:
        pickle.dump(user_journal_entries, f_)
    gratitude_var.withdraw()


# noinspection PyGlobalUndefined
def gratitude():
    global gratitude_var
    gratitude_var = Toplevel()
    gratitude_var.title("Gratitude Journaling Page")
    gratitude_var.geometry("800x800")
    gratitude_var.config(bg=COLOURS['mauve'])
    gratitude_var.iconbitmap('serene-logo.ico')
    center(gratitude_var)

    label1 = Label(gratitude_var, height=3, width=30, text="Gratitude Journaling", bg=COLOURS['mauve'],
                   font=('Basic', 30, 'normal'), fg=COLOURS['brick'])
    label1.place(x=165, y=50)

    label2 = Label(gratitude_var, height=3, text='- ' + journal_questions[len(list(user_journal_entries.keys()))],
                   bg=COLOURS['mauve'], font=('Basic', 20, 'normal'), fg=COLOURS['fr blue'])
    label2.place(x=25, y=150)

    inputtxt = Text(gratitude_var, height=15, width=47, bg="#8DEBB0", bd=0, font=('Harlow Solid Italic', 20))
    inputtxt.place(x=100, y=230)

    submit_btn = Button(gratitude_var, width=8, pady=8, text='Submit', background=COLOURS['l brick'],
                        border=0,
                        command=lambda: add_entry(journal_questions[len(list(user_journal_entries.keys()))],
                                                  inputtxt.get('1.0', END)), font=('Romeo', 10))
    submit_btn.place(x=360, y=750)

    old_entries_btn = Button(gratitude_var, pady=8, text='View old entries', background=COLOURS['l brick'],
                             border=0, command=old_entries, font=('Romeo', 10))
    old_entries_btn.place(x=685, y=15)


# noinspection PyGlobalUndefined
def old_entries():
    global old_entries_var, key
    old_entries_var = Toplevel()
    old_entries_var.title("Gratitude Journaling Old Entries")
    old_entries_var.geometry("800x800")
    old_entries_var.config(bg=COLOURS['mauve'])
    old_entries_var.iconbitmap('serene-logo.ico')
    center(old_entries_var)

    key = 0

    def show_entry():
        y_pos = 50

        label1 = Label(old_entries_var, height=3, width=80, text="Here are your journal entries:",
                       bg=COLOURS['mauve'], font=('Segoe UI', 10, 'bold'))
        label1.place(x=75, y=y_pos)

        y_pos += 50

        quest = [i for i in user_journal_entries][key]
        val = user_journal_entries.values()
        value = [i for i in val][key]

        label2 = Label(old_entries_var, height=3, width=90, bg=COLOURS['mauve'],
                       text=str(list(user_journal_entries.keys()).index(quest) + 1) + ". " + quest)
        label2.place(x=75, y=y_pos)

        y_pos += 50

        label3 = Label(old_entries_var, height=3, width=90, bg=COLOURS['mauve'],
                       text='Date: ' + value[0] + '\nTime: ' + value[1])
        label3.place(x=75, y=y_pos)

        y_pos += 50

        label4 = Label(old_entries_var, width=90, bg=COLOURS['mauve'], text='Entry:\n' + value[2] + '\n', wraplength=250)
        label4.place(x=75, y=y_pos)

        y_pos += 100

    # noinspection PyGlobalUndefined
    def back():
        global key
        if not key == 0:
            key -= 1
            show_entry()

    # noinspection PyGlobalUndefined
    def next():
        global key
        if not key == len(user_journal_entries) - 1:
            key += 1
            show_entry()

    back_btn = Button(old_entries_var, width=8, pady=8, text='Back', background=COLOURS['l brick'],
                      border=0, command=back)
    back_btn.place(x=100, y=750)

    next_btn = Button(old_entries_var, width=8, pady=8, text='Next', background=COLOURS['l brick'],
                      border=0, command=next)
    next_btn.place(x=650, y=750)

    show_entry()
