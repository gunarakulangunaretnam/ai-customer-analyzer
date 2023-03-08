'''

 * Date:            25-02-2023
 * Organization:    Deep11
 * Author:          Gunarakulan Gunaretnam
 * Author Email:    gunarakulan@gmail.com
 * Author Likedin:  https://www.linkedin.com/in/gunarakulangunaretnam/
 * Author GitHub:   https://github.com/gunarakulangunaretnam 

  Source Info
  -----------
  This is the audio analyzer script of the AI Customer Analyzer project; it
  can analyze transcripts of customers and classify as positive or negative
  based on what the customers and salesmans are talking.

 '''

from tkinter import *
from tkinter import messagebox
import speech_recognition as sr

# create global variables to store text information
stall_no = ""
employee_id = ""
employee_name = ""


# function to store the text information and open the analyzer window
def open_analyzer():
    # store the text information into global variables
    global stall_no
    global employee_id
    global employee_name


    stall_no = stall_entry.get()
    employee_id = employee_id_entry.get()
    employee_name = employee_name_entry.get()


    if stall_no != "" and employee_id != "" and employee_name != "":

        # close the main window
        root.destroy()

        # create new window
        analyzer_window = Tk()
        analyzer_window.title("AI Customer Audio Analyzer")

        # set window size and position
        window_width = 600
        window_height = 400
        screen_width = analyzer_window.winfo_screenwidth()
        screen_height = analyzer_window.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        analyzer_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        # create label for the heading
        heading_label = Label(analyzer_window, text="AI Customer Audio Analyzer", font=("Helvetica", 16), pady=10)
        heading_label.pack()

        log_text = Text(analyzer_window, width=40, height=10)
        log_text.place(x=100, y=100)

        # create button to exit the window
        exit_button = Button(analyzer_window, text="Stop", font=("Helvetica", 16), command=analyzer_window.destroy)
        exit_button.place(x=200, y=300, width=200, height=50)

        # run the analyzer window event loop
        analyzer_window.mainloop()
    else:
        messagebox.showwarning("Warning", "Please fill all fields.")

# create main window
root = Tk()
root.title("AI Customer Audio Analyzer")

# set window size and position
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

# create label for the heading
heading_label = Label(root, text="AI Customer Audio Analyzer", font=("Helvetica", 16), pady=10)
heading_label.pack()

# create label and entry widget for stall number
stall_label = Label(root, text="Stall No", font=("Helvetica", 12))
stall_label.pack()
stall_entry = Entry(root, width=30)
stall_entry.pack(pady=10)

# create label and entry widget for employee ID
employee_id_label = Label(root, text="Employee ID", font=("Helvetica", 12))
employee_id_label.pack()
employee_id_entry = Entry(root, width=30)
employee_id_entry.pack(pady=10)

# create label and entry widget for employee name
employee_name_label = Label(root, text="Employee Name", font=("Helvetica", 12))
employee_name_label.pack()
employee_name_entry = Entry(root, width=30)
employee_name_entry.pack(pady=10)

# create button to start the analysis
start_button = Button(root, text="Start", font=("Helvetica", 16), command=open_analyzer)
start_button.pack(pady=20)


# run the main event loop
root.mainloop()
