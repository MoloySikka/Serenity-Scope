import pickle
from datetime import datetime
from tkinter import *
from tkinter import messagebox

from center import center

COLOURS = {'grey': '#f7f7f7', 'fr blue': '#0479D8', 'pic blue': '#55AEE1', 'mauve': '#D6CDEA', 'l blue': '#A6E3E9',
           'l mauve': '#D0D9E4', 'l brick': '#D9ABA2', 'brick': '#E27D60'}

with open("user_survey_responses.dat", "rb") as fog:
    user_survey_result = pickle.load(fog)

survey_questions = {
    "How often do you feel anxious or worried?":
        ["Never", "Occasionally", "Frequently", "Constantly"],
    "How would you rate your overall mood recently?":
        ["Very positive", "Mostly positive", "Mostly negative", "Very negative"],
    "Do you often feel tired or lack energy?":
        ["Rarely", "Sometimes", "Often", "Always"],
    "How well are you sleeping at night?":
        ["Very well", "Fairly well", "Not very well", "Not at all"],
    "Do you find it difficult to concentrate on tasks?":
        ["Never", "Occasionally", "Frequently", "Constantly"],
    "How often do you feel irritable or easily angered?":
        ["Rarely", "Sometimes", "Often", "Always"],
    "Have you experienced changes in appetite (eating more or less than usual)?":
        ["No changes", "Slight changes", "Noticeable changes", "Significant changes"],
    "How would you describe your ability to cope with stress?":
        ["Very well", "Moderately well", "Not very well", "Poorly"],
    "Do you often feel hopeless or like things won't get better?":
        ["Rarely", "Sometimes", "Often", "Always"],
    "How satisfied are you with your overall life right now?":
        ["Very satisfied", "Somewhat satisfied", "Somewhat dissatisfied", "Very dissatisfied"]
}

survey_interpretation = {
    "Likely in a good mental health state": "Individuals in this range may experience occasional mild stress or "
                                            "anxiety, "
                                            "but their mental health is most likely stable. They may have effective "
                                            "coping mechanisms and a generally upbeat mood and energy level.\n\nCheck "
                                            "out"
                                            " this app's meditation and journaling features. Meditate every day and "
                                            "complete all journal entries; return to this survey after 50 days to see "
                                            "how you've improved.",
    "Mild symptoms of stress or anxiety": "Scores in this range indicate that the person is experiencing mild symptoms "
                                          "of stress or anxiety. They may experience occasional problems with mood, "
                                          "energy, sleep, concentration, or irritability, but these are manageable."
                                          "\n\nCheck out this app's meditation and journaling features. Meditate every "
                                          "day"
                                          "and complete all journal entries; return to this survey after 50 days to see"
                                          " how you've improved.",
    "Moderate symptoms of stress or anxiety": "This range indicates moderate stress or anxiety symptoms that may "
                                              "interfere with the individual's daily life and functioning. They may "
                                              "suffer from mood swings, fatigue, sleep disturbances, difficulty "
                                              "concentrating, and increased irritability.\n\nCheck out this app's "
                                              "meditation and journaling features. Meditate every day and complete all "
                                              "journal entries; return to this survey after 50 days to see how you've "
                                              "improved.",
    "Severe symptoms of stress or anxiety": "Scores in this range indicate severe stress or anxiety symptoms that have "
                                            "a significant impact on the individual's daily functioning and overall "
                                            "well-being. They may experience persistent low mood, chronic fatigue, "
                                            "severe sleep disturbances, difficulty concentrating, "
                                            "frequent irritability, and appetite changes.\n\nYou may benefit from "
                                            "seeking help from a mental health professional or counsellor to evaluate "
                                            "and implement appropriate interventions.\n\nCheck out this app's "
                                            "meditation"
                                            "and journaling features. Meditate every day and complete all journal "
                                            "entries; return to this survey after 50 days to see how you've improved.",
    "Very severe symptoms of stress or anxiety": "Individuals who score in this range are likely to suffer from "
                                                 "debilitating stress or anxiety symptoms. They may feel overwhelmed, "
                                                 "hopeless, or incapable of dealing with daily challenges. Symptoms "
                                                 "may include intense and persistent negative emotions, "
                                                 "extreme fatigue, severe sleep disturbances, difficulty "
                                                 "concentrating, frequent irritability or anger outbursts, "
                                                 "and significant appetite changes.\n\nYou may benefit from seeking "
                                                 "help"
                                                 "from a mental health professional or counsellor to evaluate and "
                                                 "implement appropriate interventions.\n\nCheck out this app's "
                                                 "meditation and journaling features. Meditate every day and complete "
                                                 "all journal entries; return to this survey after 50 days to see how "
                                                 "you've improved."
}


def calculate(total_points):
    if total_points >= 10 & total_points <= 15:
        state = "Likely in a good mental health state"

    elif total_points >= 16 & total_points <= 20:
        state = "Mild symptoms of stress or anxiety"

    elif total_points >= 21 & total_points <= 25:
        state = "Moderate symptoms of stress or anxiety"

    elif total_points >= 26 & total_points <= 30:
        state = "Severe symptoms of stress or anxiety"

    elif total_points >= 31 & total_points <= 40:
        state = "Very severe symptoms of stress or anxiety"

    a = ''

    for key, value in survey_interpretation.items():
        if key == state:
            a = value

    messagebox.showinfo(state, a)

    f_ = open("user_survey_responses.dat", "ab")
    user_survey_result.update(
        {state: [datetime.now().strftime("%B %d, %Y"), datetime.now().strftime("%H:%M:%S"), a]})
    pickle.dump(user_survey_result, f_)
    f_.close()


# noinspection PyGlobalUndefined
def old_surveys():
    global old_surveys_var
    old_surveys_var = Toplevel()
    old_surveys_var.title("Mental Health Survey Results")
    old_surveys_var.geometry("800x800")
    old_surveys_var.config(bg=COLOURS['l blue'])
    old_surveys_var.iconbitmap('serene-logo.ico')
    center(old_surveys_var)

    y_pos = 0

    label1 = Label(old_surveys_var, height=3, width=70, text="Here are your survey results:", bg=COLOURS['l blue'])
    label1.pack(fill='x')
    label1.place(x=75, y=y_pos)

    y_pos += 50

    for key, value in user_survey_result.items():
        label2 = Label(old_surveys_var, height=3, width=70,
                       text="Result: " + key, bg=COLOURS['l blue'])
        label2.pack(fill='x')
        label2.place(x=75, y=y_pos)

        y_pos += 50

        label3 = Label(old_surveys_var, height=3, width=70, text='Date: ' + value[0] + '\nTime: ' + value[1], bg=COLOURS['l blue'])
        label3.pack(fill='x')
        label3.place(x=75, y=y_pos)

        y_pos += 50

        label4 = Label(old_surveys_var, width=70, text='Detailed Result: ' + value[2] + '\n', wraplength=250, bg=COLOURS['l blue'])
        label4.pack(fill='x')
        label4.place(x=75, y=y_pos)

        y_pos += 100

    next_btn = Button(old_surveys_var, width=8, pady=8, text='Next', background='black', foreground='white',
                      border=0, command=lambda: start_survey(1))
    next_btn.place(x=720, y=750)


# noinspection PyGlobalUndefined
def survey():
    global survey_var
    survey_var = Toplevel()
    survey_var.title("Survey Page")
    survey_var.geometry("800x800")
    survey_var.config(bg=COLOURS['l blue'])
    survey_var.iconbitmap('serene-logo.ico')
    center(survey_var)

    start_survey(0)


def start_survey(sur_num):
    # noinspection PyGlobalUndefined
    global answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10
    for widget in survey_var.winfo_children():
        widget.destroy()

    y_pos = 50
    x_pos = 175

    label = Label(survey_var, height=3, width=30, text="Mental Health Survey", bg=COLOURS['l blue'], font=('Romeo', 15))
    label.place(x=270, y=y_pos)
    y_pos += 50

    old_surveys_btn = Button(survey_var, width=15, pady=8, text='View old surveys', background='black',
                             foreground='white', border=0, command=old_surveys)
    old_surveys_btn.place(x=680, y=15)

    if sur_num == 0:
        label1 = Label(survey_var, height=3, width=50, text='Q1.' + list(survey_questions.keys())[0],
                       bg=COLOURS['l blue'], font=('Romeo', 10))
        label1.place(x=x_pos, y=y_pos)

        y_pos += 70

        answer1 = IntVar()

        Radiobutton(survey_var, text=list(survey_questions.values())[0][0], variable=answer1, value=1,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[0][1], variable=answer1, value=2,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[0][2], variable=answer1, value=3,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[0][3], variable=answer1, value=4,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 50

        label2 = Label(survey_var, height=3, width=50, text='Q2.' + list(survey_questions.keys())[1],
                       bg=COLOURS['l blue'], font=('Romeo', 10))
        label2.place(x=x_pos, y=y_pos)

        y_pos += 70

        answer2 = IntVar()

        Radiobutton(survey_var, text=list(survey_questions.values())[1][0], variable=answer2, value=1,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[1][1], variable=answer2, value=2,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[1][2], variable=answer2, value=3,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[1][3], variable=answer2, value=4,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)

        next_btn = Button(survey_var, width=8, pady=8, text='Next', background='black', foreground='white',
                          border=0, command=lambda: start_survey(1))
        next_btn.place(x=720, y=750)

    elif sur_num == 1:
        label3 = Label(survey_var, height=3, width=50, text='Q3.' + list(survey_questions.keys())[2],
                       bg=COLOURS['l blue'], font=('Romeo', 10))
        label3.place(x=x_pos, y=y_pos)

        y_pos += 70

        answer3 = IntVar()

        Radiobutton(survey_var, text=list(survey_questions.values())[2][0], variable=answer3, value=1,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[2][1], variable=answer3, value=2,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[2][2], variable=answer3, value=3,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[2][3], variable=answer3, value=4,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 50

        label4 = Label(survey_var, height=3, width=50, text='Q4.' + list(survey_questions.keys())[3],
                       bg=COLOURS['l blue'], font=('Romeo', 10))
        label4.place(x=x_pos, y=y_pos)

        y_pos += 70

        answer4 = IntVar()

        Radiobutton(survey_var, text=list(survey_questions.values())[3][0], variable=answer4, value=1,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[3][1], variable=answer4, value=2,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[3][2], variable=answer4, value=3,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[3][3], variable=answer4, value=4,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 50

        back_btn = Button(survey_var, width=8, pady=8, text='Back', background='black', foreground='white',
                          border=0, command=lambda: start_survey(0))
        back_btn.place(x=20, y=750)

        next_btn = Button(survey_var, width=8, pady=8, text='Next', background='black', foreground='white',
                          border=0, command=lambda: start_survey(2))
        next_btn.place(x=720, y=750)

    elif sur_num == 2:
        label5 = Label(survey_var, height=3, width=50, text='Q5.' + list(survey_questions.keys())[4],
                       bg=COLOURS['l blue'], font=('Romeo', 10))
        label5.place(x=x_pos, y=y_pos)

        y_pos += 70

        answer5 = IntVar()

        Radiobutton(survey_var, text=list(survey_questions.values())[4][0], variable=answer5, value=1,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[4][1], variable=answer5, value=2,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[4][2], variable=answer5, value=3,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[4][3], variable=answer5, value=4,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 50

        label6 = Label(survey_var, height=3, width=50, text='Q6.' + list(survey_questions.keys())[5],
                       bg=COLOURS['l blue'], font=('Romeo', 10))
        label6.place(x=x_pos, y=y_pos)

        y_pos += 70

        answer6 = IntVar()

        Radiobutton(survey_var, text=list(survey_questions.values())[5][0], variable=answer6, value=1,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[5][1], variable=answer6, value=2,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[5][2], variable=answer6, value=3,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[5][3], variable=answer6, value=4,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 50

        back_btn = Button(survey_var, width=8, pady=8, text='Back', background='black', foreground='white',
                          border=0, command=lambda: start_survey(1))
        back_btn.place(x=20, y=750)

        next_btn = Button(survey_var, width=8, pady=8, text='Next', background='black', foreground='white',
                          border=0, command=lambda: start_survey(3))
        next_btn.place(x=720, y=750)

    elif sur_num == 3:
        label7 = Label(survey_var, height=3, width=70, text='Q7.' + list(survey_questions.keys())[6],
                       bg=COLOURS['l blue'], font=('Romeo', 10))
        label7.place(x=x_pos, y=y_pos)

        y_pos += 70

        answer7 = IntVar()

        Radiobutton(survey_var, text=list(survey_questions.values())[6][0], variable=answer7, value=1,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[6][1], variable=answer7, value=2,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[6][2], variable=answer7, value=3,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[6][3], variable=answer7, value=4,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 50

        label8 = Label(survey_var, height=3, width=50, text='Q8.' + list(survey_questions.keys())[7],
                       bg=COLOURS['l blue'], font=('Romeo', 10))
        label8.place(x=x_pos, y=y_pos)

        y_pos += 70

        answer8 = IntVar()

        Radiobutton(survey_var, text=list(survey_questions.values())[7][0], variable=answer8, value=1,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[7][1], variable=answer8, value=2,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[7][2], variable=answer8, value=3,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[7][3], variable=answer8, value=4,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 50

        back_btn = Button(survey_var, width=8, pady=8, text='Back', background='black', foreground='white',
                          border=0, command=lambda: start_survey(2))
        back_btn.place(x=20, y=750)

        next_btn = Button(survey_var, width=8, pady=8, text='Next', background='black', foreground='white',
                          border=0, command=lambda: start_survey(4))
        next_btn.place(x=720, y=750)

    elif sur_num == 4:
        label9 = Label(survey_var, height=3, width=50, text='Q9.' + list(survey_questions.keys())[8],
                       bg=COLOURS['l blue'], font=('Romeo', 10))
        label9.place(x=x_pos, y=y_pos)

        y_pos += 70

        answer9 = IntVar()

        Radiobutton(survey_var, text=list(survey_questions.values())[8][0], variable=answer9, value=1,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[8][1], variable=answer9, value=2,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[8][2], variable=answer9, value=3,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[8][3], variable=answer9, value=4,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 50

        label10 = Label(survey_var, height=3, width=50, text='Q10.' + list(survey_questions.keys())[9],
                        bg=COLOURS['l blue'], font=('Romeo', 10))
        label10.place(x=x_pos, y=y_pos)

        y_pos += 70

        answer10 = IntVar()

        Radiobutton(survey_var, text=list(survey_questions.values())[9][0], variable=answer10, value=1,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[9][1], variable=answer10, value=2,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[9][2], variable=answer10, value=3,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 30
        Radiobutton(survey_var, text=list(survey_questions.values())[9][3], variable=answer10, value=4,
                    bg=COLOURS['l blue'], font=('Romeo', 10)).place(x=x_pos,
                                                                    y=y_pos)
        y_pos += 50

        back_btn = Button(survey_var, width=8, pady=8, text='Back', background='black', foreground='white',
                          border=0, command=lambda: start_survey(3))
        back_btn.place(x=20, y=750)

        submit_btn = Button(survey_var, width=8, pady=8, text='Submit', background='black', foreground='white',
                            border=0,
                            command=lambda: calculate(
                                answer1.get() + answer2.get() + answer3.get() + answer4.get() + answer5.get() +
                                answer6.get() + answer7.get() + answer8.get() + answer9.get() + answer10.get()))
        submit_btn.place(x=335, y=750)
