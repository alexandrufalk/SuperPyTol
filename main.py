import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
import keyboard
import threading
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from hotreload import Loader
from RequestsModules.my_requests import httpGetAllProjects

class Handler(FileSystemEventHandler):

    def __init__(self, gui_started_event):
        self.gui_started_event = gui_started_event
        self.gui_started = False

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(".py"):
            # Code file was modified; recreate the GUI
            if self.gui_started:
                self.gui_started_event.set()  # Signal to close the previous GUI
            print("Code file modified. Reloading GUI...")
      

def enter_data():
    accepted = accept_var.get()
    
    if accepted=="Accepted":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            
            # Course info
            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()
            
            print("First name: ", firstname, "Last name: ", lastname)
            print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
            print("# Courses: ", numcourses, "# Semesters: ", numsemesters)
            print("Registration status", registration_status)
            print("------------------------------------------")
        else:
            tk.messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        tk.messagebox.showwarning(title= "Error", message="You have not accepted the terms")

# Function to open a new window with entry fields
def open_new_window():
    new_window = tk.Toplevel()
    new_window.title("New Window")

    first_name_label = ttk.Label(new_window, text="First Name:")
    first_name_label.pack()
    first_name_entry = ttk.Entry(new_window)
    first_name_entry.pack()

    last_name_label = ttk.Label(new_window, text="Last Name:")
    last_name_label.pack()
    last_name_entry = ttk.Entry(new_window)
    last_name_entry.pack()

    # Button to fetch data from the server and save to a file
    fetch_data_button = ttk.Button(new_window, text="Fetch Data and Save", command=fetch_data_and_save)
    fetch_data_button.pack()

def fetch_data_and_save():
    API_URL = "http://localhost:5001/v1/databaseproject"
    try:
        response = requests.get(API_URL)
        data = response.text  # Assuming the response is text data

        # Display the fetched data in a messagebox
        messagebox.showinfo("Fetched Data", f"Data from the server: {data}")

        # Save the fetched data to a text file
        with open("fetched_data.txt", "w") as file:
            file.write(data)
            messagebox.showinfo("Data Saved", "Fetched data saved to 'fetched_data.txt'")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch data: {e}")

def refresh_window():
    # Redraw the window
    window.update()
    window.update_idletasks()
    print("Refresh completed.")

def create_gui():
    try:
        window = tk.Tk()
        window.title("SuperPyTol")

        frame = tk.Frame(window)
        frame.pack()

        label = tk.Label(window, text="Click the below button to refresh the window.")
        label.pack()

        button = tk.Button(window, text="Refresh", command=refresh_window)
        button.pack()

        # Saving User Info
        user_info_frame =tk.LabelFrame(frame, text="User Information")
        user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

        first_name_label = tk.Label(user_info_frame, text="First Name")
        first_name_label.grid(row=0, column=0)
        last_name_label = tk.Label(user_info_frame, text="Last Name")
        last_name_label.grid(row=0, column=1)

        first_name_entry = tk.Entry(user_info_frame)
        last_name_entry = tk.Entry(user_info_frame)
        first_name_entry.grid(row=1, column=0)
        last_name_entry.grid(row=1, column=1)

        title_label = tk.Label(user_info_frame, text="Select Project")
        title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
        title_label.grid(row=0, column=2)
        title_combobox.grid(row=1, column=2)

        age_label = tk.Label(user_info_frame, text="Age")
        age_spinbox = tk.Spinbox(user_info_frame, from_=18, to=110)
        age_label.grid(row=2, column=0)
        age_spinbox.grid(row=3, column=0)

        nationality_label = tk.Label(user_info_frame, text="Nationality")
        nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
        nationality_label.grid(row=2, column=1)
        nationality_combobox.grid(row=3, column=1)

        for widget in user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # Saving Course Info
        courses_frame = tk.LabelFrame(frame)
        courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

        registered_label = tk.Label(courses_frame, text="Registration Status")

        reg_status_var = tk.StringVar(value="Not Registered")
        registered_check = tk.Checkbutton(courses_frame, text="Currently Registered",
                                            variable=reg_status_var, onvalue="Registered", offvalue="Not registered")

        registered_label.grid(row=0, column=0)
        registered_check.grid(row=1, column=0)

        numcourses_label = tk.Label(courses_frame, text= "# Completed Courses")
        numcourses_spinbox = tk.Spinbox(courses_frame, from_=0, to='infinity')
        numcourses_label.grid(row=0, column=1)
        numcourses_spinbox.grid(row=1, column=1)

        numsemesters_label = tk.Label(courses_frame, text="# Semesters")
        numsemesters_spinbox = tk.Spinbox(courses_frame, from_=0, to="infinity")
        numsemesters_label.grid(row=0, column=2)
        numsemesters_spinbox.grid(row=1, column=2)

        for widget in courses_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # Accept terms
        terms_frame = tk.LabelFrame(frame, text="Terms & Conditions")
        terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

        accept_var = tk.StringVar(value="Not Accepted")
        terms_check = tk.Checkbutton(terms_frame, text= "I accept the terms and conditions.",
                                        variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
        terms_check.grid(row=0, column=0)

        # Button
        button = tk.Button(frame, text="Enter data", command= enter_data)
        button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

        # Button to open the new window

        open_window_button = ttk.Button(window, text="Open Database test5", command=open_new_window)
        open_window_button.pack()

        def check():
            with open('exec_log.txt', 'r') as exec_c:
                exec_command = exec_c.read()

            if len(exec_command) > 0:
                for widget in window.winfo_children():
                    widget.destroy()
                exec(exec_command)
                with open('exec_log.txt', 'w') as exec_c:
                    pass
                window.update()

            window.after(100, check)

        window.after(100, check)

        window.mainloop()
    except Exception as e:
        print("Error creating GUI:", e)
    

# def start_gui():
#     t = threading.Thread(target=create_gui)
#     t.daemon = True  # Allow the thread to exit when the main program finishes
#     t.start()

def start_gui():
    create_gui()
    root = tk._default_root
    if root is not None:
        root.destroy()

def gui_thread():
    create_gui()

# def main():
#     start_gui()
#     previous_code = None

#     def on_code_change():
#         nonlocal previous_code
#         print("Code changed. Reloading GUI...")
#         previous_code = current_code
#         start_gui()

#     event_handler = CodeChangeHandler(on_code_change)
#     observer = Observer()
#     observer.schedule(event_handler, path=".", recursive=True)
#     observer.start()

#     while True:
#         try:
#             with open(__file__) as f:
#                 current_code = f.read()
#             time.sleep(1)
#         except Exception as e:
#             print(f"Error checking code changes: {e}")
#             break

while True:
    if keyboard.is_pressed("Ctrl+Alt"):
        with open('main.py', 'r') as file:
            file_data = file.read()
            file_data_start_index = file_data.find("'@Start@'")
            file_data_end_index = file_data.find("'@End@'")
            exec_command = file_data[file_data_start_index:file_data_end_index]
            with open('exec_log.txt', 'w') as txt_file:
                txt_file.write(exec_command)











