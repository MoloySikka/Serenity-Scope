from tkinter import *
from center import center

survey_questions={
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

def survey():
    global survey_var
    survey_var = Toplevel()
    survey_var.title("Survey Page")
    survey_var.geometry("800x800")
    survey_var.config(bg='#BBDEE7')
    survey_var.iconbitmap('serene-logo.ico')
    center(survey_var)

    y_pos=50
    label1 = Label(survey_var, height=3, width=30, text="Mental Health Survey")
    label1.place(x=275, y=y_pos)
    y_pos+=50

    for key, value in survey_questions.items():
        label1 = Label(survey_var, height=3, width=30, text='\nQ'+ str(list(survey_questions.keys()).index(key) + 1)+". "+key)
        label1.place(x=275, y=y_pos)

        y_pos+=70


        Radiobutton(survey_var, text = value[0], variable =  StringVar(survey_var, "1"), value = 1).place(x=275, y=y_pos)
        y_pos+=30
        Radiobutton(survey_var, text = value[1], variable = StringVar(survey_var, "1"), value = 2).place(x=275, y=y_pos) 
        y_pos+=30
        Radiobutton(survey_var, text = value[2], variable = StringVar(survey_var, "1"), value = 3).place(x=275, y=y_pos)
        y_pos+=30
        Radiobutton(survey_var, text = value[3], variable = StringVar(survey_var, "1"), value = 4).place(x=275, y=y_pos)
        y_pos+=50
