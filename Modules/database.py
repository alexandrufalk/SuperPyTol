import tkinter as tk
from tkinter import ttk
from RequestsModules.my_requests import httpGetAllProjects



# Function to open a new database window 
def open_new_window():
    new_window = tk.Toplevel()
    new_window.title("New Window")

    project_name_label = ttk.Label(new_window, text="First Name:")
    project_name_label.pack()
    project_name_entry = ttk.Entry(new_window)
    project_name_entry.pack()

    last_name_label = ttk.Label(new_window, text="Last Name:")
    last_name_label.pack()
    last_name_entry = ttk.Entry(new_window)
    last_name_entry.pack()

    # Button to fetch data from the server and save to a file
    fetch_data_button = ttk.Button(new_window, text="Fetch Data and Save", command=httpGetAllProjects, style="Secondary.TButton")
    fetch_data_button.pack()
