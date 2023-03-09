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
import json
import queue
import datetime
import threading
from tkinter import *
import mysql.connector
from textblob import TextBlob
from tkinter import messagebox
import speech_recognition as sr


with open('data\\database-credentials.json') as f:
    config_data = json.load(f)

    # Access the values from the dictionary
    database_host = config_data['database_host']
    database_user = config_data['database_user']
    database_pass = config_data['database_password']
    database_name = config_data['database_name']

mydb = mysql.connector.connect(
  host = database_host,
  user = database_user,
  password = database_pass,
  database = database_name
)

mycursor = mydb.cursor()

# create global variables to store text information
stall_no = ""
employee_id = ""
employee_name = ""


def database_updater(dataText, output):
    global stall_no, employee_id, employee_name
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    time = datetime.datetime.now().strftime('%H:%M:%S')

    # create SQL query
    sql_code_insert = "INSERT INTO audio_data (date, time, stall_no, employee_id, employee_name, transcription, prediction) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    data_val = (date, time, stall_no, employee_id, employee_name, dataText, output)

    # execute query and commit changes
    mycursor.execute(sql_code_insert, data_val)
    mydb.commit()


def sentiment_analyzer(log_text, dataText):

    blob = TextBlob(dataText)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0:
        sentiment_label = "Positive"

    elif sentiment_score < 0:
        sentiment_label = "Negative"

    else:
        sentiment_label = "Neutral"

    print(f"\n{dataText} \n \n")
    log_text.insert(END, f"\n{dataText}" + "\n \n")
    log_text.see("end")

    print(f"{sentiment_label} \n \n")

    database_updater(dataText, sentiment_label)

    if sentiment_label == "Positive":

        log_text.insert(END, f"Output: {sentiment_label}" + "\n \n", "blue")
        log_text.tag_config("blue", foreground="blue")
        log_text.see("end")

    elif sentiment_label == "Neutral":
        log_text.insert(END, f"Output: {sentiment_label}" + "\n \n", "orange")
        log_text.tag_config("orange", foreground="orange")
        log_text.see("end")
    
    elif sentiment_label == "Negative":
        log_text.insert(END, f"Output: {sentiment_label}" + "\n \n", "red")
        log_text.tag_config("red", foreground="red")
        log_text.see("end")


def audio_listener(log_text):
    while True:
        recorder = sr.Recognizer()
        with sr.Microphone() as source:

            print("Listening...\n")
            log_text.insert(END, "Listening...\n")
            log_text.see("end")

            recorder.pause_threshold = 1
            audio = recorder.listen(source, phrase_time_limit=10)

            try:
                text = recorder.recognize_google(audio)

                print("Recognizing...\n")
                log_text.insert(END, "Recognizing...\n")
                log_text.see("end")
                
                dataText = format(text)

                sentiment_analyzer(log_text, dataText)

            except:
                pass


def open_analyzer():
    global stall_no
    global employee_id
    global employee_name

    stall_no = stall_entry.get()
    employee_id = employee_id_entry.get()
    employee_name = employee_name_entry.get()

    if stall_no != "" and employee_id != "" and employee_name != "":
        root.destroy()

        analyzer_window = Tk()
        analyzer_window.title("AI Customer Audio Analyzer")

        window_width = 600
        window_height = 400
        screen_width = analyzer_window.winfo_screenwidth()
        screen_height = analyzer_window.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))
        analyzer_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        heading_label = Label(analyzer_window, text="AI Customer Audio Analyzer", font=("Helvetica", 16), pady=10)
        heading_label.pack()

        log_text = Text(analyzer_window, width=40, height=10)
        log_text.place(x=100, y=100)

        exit_button = Button(analyzer_window, text="Stop", font=("Helvetica", 16), command=analyzer_window.destroy)
        exit_button.place(x=200, y=300, width=200, height=50)

        audio_listener_function = threading.Thread(target=audio_listener, args=(log_text,), daemon=True)
        audio_listener_function.start()

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
