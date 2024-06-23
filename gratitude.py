label1 = Label(old_entries_var, height=3, width=70, text="Here are your journal entries:")
    label1.place(x=75, y=y_pos)

    y_pos += 50

    for key, value in user_journal_entries.items():
        label2 = Label(old_entries_var, height=3, width=70,
                       text=str(list(user_journal_entries.keys()).index(key) + 1) + ". " + key)
        label2.place(x=75, y=y_pos)

        y_pos += 50

        label3 = Label(old_entries_var, height=3, width=70, text='Date: ' + value[0] + '\nTime: ' + value[1])
        label3.place(x=75, y=y_pos)

        y_pos += 50

        label4 = Label(old_entries_var, width=70, text='Entry: ' + value[2] + '\n', wraplength=250)
        label4.place(x=75, y=y_pos)

        y_pos += 100
