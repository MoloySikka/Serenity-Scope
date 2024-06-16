from datetime import datetime

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
                                            "coping mechanisms and a generally upbeat mood and energy level.\nCheck out"
                                            " this app's meditation and journaling features. Meditate every day and "
                                            "complete all journal entries; return to this survey after 50 days to see "
                                            "how you've improved.",
    "Mild symptoms of stress or anxiety": "Scores in this range indicate that the person is experiencing mild symptoms "
                                          "of stress or anxiety. They may experience occasional problems with mood, "
                                          "energy, sleep, concentration, or irritability, but these are manageable."
                                          "\nCheck out this app's meditation and journaling features. Meditate every "
                                          "day"
                                          "and complete all journal entries; return to this survey after 50 days to see"
                                          " how you've improved.",
    "Moderate symptoms of stress or anxiety": "This range indicates moderate stress or anxiety symptoms that may "
                                              "interfere with the individual's daily life and functioning. They may "
                                              "suffer from mood swings, fatigue, sleep disturbances, difficulty "
                                              "concentrating, and increased irritability.\nCheck out this app's "
                                              "meditation and journaling features. Meditate every day and complete all "
                                              "journal entries; return to this survey after 50 days to see how you've "
                                              "improved.",
    "Severe symptoms of stress or anxiety": "Scores in this range indicate severe stress or anxiety symptoms that have "
                                            "a significant impact on the individual's daily functioning and overall "
                                            "well-being. They may experience persistent low mood, chronic fatigue, "
                                            "severe sleep disturbances, difficulty concentrating, "
                                            "frequent irritability, and appetite changes.\nYou may benefit from "
                                            "seeking help from a mental health professional or counsellor to evaluate "
                                            "and implement appropriate interventions.\nCheck out this app's meditation "
                                            "and journaling features. Meditate every day and complete all journal "
                                            "entries; return to this survey after 50 days to see how you've improved.",
    "Very severe symptoms of stress or anxiety": "Individuals who score in this range are likely to suffer from "
                                                 "debilitating stress or anxiety symptoms. They may feel overwhelmed, "
                                                 "hopeless, or incapable of dealing with daily challenges. Symptoms "
                                                 "may include intense and persistent negative emotions, "
                                                 "extreme fatigue, severe sleep disturbances, difficulty "
                                                 "concentrating, frequent irritability or anger outbursts, "
                                                 "and significant appetite changes.\nYou may benefit from seeking help "
                                                 "from a mental health professional or counsellor to evaluate and "
                                                 "implement appropriate interventions.\nCheck out this app's "
                                                 "meditation and journaling features. Meditate every day and complete "
                                                 "all journal entries; return to this survey after 50 days to see how "
                                                 "you've improved."
}

survey_responses = {}


def answer_survey():
    responses = {}
    for key, value in survey_questions.items():
        print('\nQ', (list(survey_questions.keys()).index(key) + 1), ". ", sep="", end="")
        print(key)
        print('A. ', value[0])
        print('B. ', value[1])
        print('C. ', value[2])
        print('D. ', value[3], '\n')
        answer = input("Enter option A, B, C, D: ")
        points = 0
        if answer == 'A':
            points += 1
        elif answer == 'B':
            points = 2
        elif answer == 'C':
            points = 3
        elif answer == 'D':
            points = 4
        else:
            points = 0

        responses.update({key: points})

    survey_responses.update({datetime.now().strftime("%B %d, %Y"): responses})


def interpret_survey():
    for Key, Value in survey_responses.items():
        total_points = 0
        for key, value in Value.items():
            total_points += value

        state = ""
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

        print("\n", state, "\n")

        for key, value in survey_interpretation.items():
            if key == state:
                print(value)


answer_survey()
interpret_survey()
