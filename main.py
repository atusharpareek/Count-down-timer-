import tkinter
from plyer import notification
from tkinter import messagebox
from tkinter import *
import time

window = Tk()
window.geometry("300x200")
window.title("Python Countdown timer")

def h_click(event):
       hour_entry.delete(0, 'end')
def m_click(event):
       min_entry.delete(0, 'end')
def s_click(event):
       sec_entry.delete(0, 'end')


def timer():
    # Since we use placeholders, we check if the user entered an integer
    try:
        timer_time = int(hour_entry.get()) * 3600 + int(min_entry.get()) * 60 + int(sec_entry.get())

    except:
        messagebox.showerror(message="Enter Valid Time")
    # The user cannot activate a timer with no time set
    # To update the timer with every decreasing second and display a notification
    if timer_time > 0:
        hour = 0
        min = 0
        sec = 0
        # If minutes is more than 60, it has to be set to the next hour
        while timer_time >= 0:
            min, sec = divmod(timer_time, 60)
            if min > 60:
                hour, min = divmod(min, 60)
            # Set the declared variables with the new values to display
            hours.set(hour)
            mins.set(min)
            secs.set(sec)
            # Sleep for 1 creates a delay of 1 second
            time.sleep(1)
            # Update the changes on the window for every second
            window.update()
            # Decrement the timer value by 1
            timer_time -= 1
        # Create a desktop notification
        notification.notify(
            # Title of the notification,
            title="TIMER ALERT",
            # Notification stays for 30 seconds
            timeout=30,
        )
        # This notification is provided by tkinter with the created app
        messagebox.showinfo(message="Timer Complete!")


title_label_1 = Label(window, text="TIMER PROJECT", font=("Gayathri", 12)).pack()

title_label_2 = Label(window, text="Put 0 in fields not of use", font=("Gayathri", 10)).pack()
# Variables using which the timer is updated in the function
hours = IntVar()
mins = IntVar()
secs = IntVar()

# To read user input for hours, minutes and seconds
hour_entry = Entry(window, width=3, textvariable=hours, font=("Ubuntu Mono", 18))
min_entry = Entry(window, width=3, textvariable=mins, font=("Ubuntu Mono", 18))
sec_entry = Entry(window, width=3, textvariable=secs, font=("Ubuntu Mono", 18))

# Placeholder for the entry widgets
hour_entry.insert(0, 00)
min_entry.insert(0, 00)
sec_entry.insert(0, 00)

# Positioning the entry widgets.
# place() takes an x(from the left) and y(from the top) coordinate
hour_entry.place(x=90, y=50)
min_entry.place(x=140, y=50)
sec_entry.place(x=190, y=50)

# To link the defined placeholder removal functions on mouse click
hour_entry.bind("<1>", h_click)
min_entry.bind("<1>", m_click)
sec_entry.bind("<1>", s_click)

#button to activate the timer function
button = Button(window,text='Activate Timer',font=("Gayathri", 8), command=timer).pack(pady=50)
#Close the window and exit the app
window.mainloop()