import tkinter as tk
from tkinter import ttk
from RequestsModules.my_requests import httpGetAllProjects



# Function to open a new database window 
def openDatabase(root):

    projects=httpGetAllProjects()


    def extract_project_names(data):
        project_names = [item['ProjectName'] for item in data]
        project_names.append("New Project")
        return project_names
    
    project_names =extract_project_names(projects)

    new_template_name = tk.StringVar()
    selected_template = tk.StringVar()

     
    # Toplevel object which will 
    # be treated as a new window
    newWindow = tk.Toplevel(root)
    
    # sets the title of the
    # Toplevel widget
    newWindow.title("Database")
    
    # sets the geometry of toplevel
    newWindow.geometry("400x400")

    
    inner_frame = ttk.Frame(newWindow)
    inner_frame.grid(row=0, column=0, padx=10, pady=10)

    project_name_label = tk.Label(inner_frame, text="Enter Template Name ")
    project_name_label.grid(row=0, column=0)
   
    project_name_entry = tk.Entry(inner_frame, textvariable=new_template_name)
    project_name_entry.grid(row=1,column=0)

     # Add template buttons
    add_template= ttk.Button(inner_frame, bootstyle="info", text="Template", command=lambda:print(new_template_name.get()))
    add_template.grid(row=0, column=1)


    #Define Project Template label and Project Template
    project_templates_label = tk.Label(inner_frame, text="Select Project ")
    project_templates_combobox = ttk.Combobox(inner_frame, values=project_names, textvariable=selected_template)

    # Display the roject Template label and Project Templat
    project_templates_label.grid(row=3, column=0, padx=20, pady=10)
    project_templates_combobox.grid(row=4, column=0, padx=20, pady=10)

    def test_template(event):
        value=selected_template.get()
        filtered_projects= [item for item in projects if item['ProjectName'] == value]
        print("filtered database data:",filtered_projects[0]['DatabaseDim'])
        # template_table(inner_frame,filtered_template[0]['Data'])



    project_templates_combobox.bind("<<ComboboxSelected>>",test_template)


    # template_table(inner_frame, data)


# create new tk window
