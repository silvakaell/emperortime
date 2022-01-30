from tkinter import *


def emperor_time():
    days = int(minutes_input.get())
    time_lost.config(text=f'{days}')


window = Tk()
window.title("Emperor Time Calculator")
window.config(padx=20, pady=20)

desc_label = Label(text="This is emperor time.\n"
                        "Kurapika's Emperor Time is a Specialization type of Nen ability"
                        " that he can use once his eyes turn scarlet.\n"
                        "Upon activation, Emperor Time allows him to utilize all the other "
                        "Nen types to with the highest order of efficiency.\n", )
# ,
desc_label.grid(column=1, row=7)

minutes_input = Entry()
minutes_input.grid(column=1, row=0)

minutes_label = Label(text='Insert seconds of nen usage: ')
minutes_label.grid(column=0, row=0)

is_equal_label = Label(text="The number of time lost is: ")
is_equal_label.grid(column=0, row=1)

time_lost = Label(text="0")
time_lost.grid(column=1, row=1)

days_label = Label(text="hours")
days_label.grid(column=3, row=1)

calculate_button = Button(text="Calculate", command=emperor_time)
calculate_button.grid(column=1, row=2)

window.mainloop()
