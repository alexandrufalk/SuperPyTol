import tkinter as tk
from tkinter import ttk

 # Open templates window
def openTemplates(root):

    new_template_name = tk.StringVar()
     
    # Toplevel object which will 
    # be treated as a new window
    newWindow = tk.Toplevel(root)
    
    # sets the title of the
    # Toplevel widget
    newWindow.title("Templates")
    
    # sets the geometry of toplevel
    newWindow.geometry("400x400")

    template_info_frame = tk.LabelFrame(newWindow, text="Templates")
    template_info_frame.grid(row=0, column=0, padx=20, pady=10)

    # Define project_name_label and project_name_entry
    project_name_label = tk.Label(template_info_frame, text="Enter Template Name")
    project_name_entry = tk.Entry(template_info_frame, textvariable=new_template_name)
    
    project_name_label.grid(row=0, column=2, padx=20, pady=10)
    project_name_entry.grid(row=1, column=2, padx=20, pady=10)
    # A Label widget to show in toplevel
    tk.Label(newWindow, text ="Templates").pack()
    button = ttk.Button(newWindow, text="Exit", command=newWindow.destroy)
    button.pack(side='left',padx=10,pady=10)