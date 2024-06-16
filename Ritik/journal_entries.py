import random
from datetime import datetime

journal_questions = [
    "Write about a time when you laughed uncontrollably.",
    "Appreciate a friend who lives far away but is dear to you.",
    "What is the best gift that you have ever received?",
    "Write about a movie that touched your heart, and why.",
    "Write about someone that you really admire.",
    "Appreciate a refreshing walk that you had in nature."]

user_journal_questions = journal_questions.copy()

user_journal_entries = {}


def write_journal_entry():
    num = random.randint(0, len(user_journal_questions) - 1)
    print(user_journal_questions[num])
    entry = input("Start your journal entry from here: ")
    user_journal_entries.update({user_journal_questions[num]: [datetime.now().strftime("%B %d, %Y"),
                                                               datetime.now().strftime("%H:%M:%S"), entry]})
    user_journal_questions.remove(user_journal_questions[num])
    print("\nGreat job on successfully completing your entry!\n")


def print_journal_entries():
    print('Here are your journal entries:\n')
    for key, value in user_journal_entries.items():
        print((list(user_journal_entries.keys()).index(key) + 1), ". ", sep="", end="")
        print(key)
        print('Date:', value[0], '\nTime:', value[1])
        print('Entry: ', value[2], '\n')


write_journal_entry()
print_journal_entries()
