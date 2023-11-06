import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style
from RequestsModules.my_requests import httpGetAllProjects
from RequestsModules.my_requests import httpGetAllTemplates
from Modules.database import open_new_window
from Modules.case import case_gui
from Modules.case import create_histogram

# def enter_data():
#     accepted = accept_var.get()
    
#     if accepted=="Accepted":
#         # User info
#         firstname = project_name_entry.get()
#         lastname = last_name_entry.get()
        
#         if firstname and lastname:
#             title = project_combobox.get()
#             age = age_spinbox.get()
#             nationality = nationality_combobox.get()
            
#             # Course info
#             registration_status = reg_status_var.get()
#             numcourses = numcourses_spinbox.get()
#             numsemesters = numsemesters_spinbox.get()
            
#             print("First name: ", firstname, "Last name: ", lastname)
#             print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
#             print("# Courses: ", numcourses, "# Semesters: ", numsemesters)
#             print("Registration status", registration_status)
#             print("------------------------------------------")
#         else:
#             tk.messagebox.showwarning(title="Error", message="First name and last name are required.")
#     else:
#         tk.messagebox.showwarning(title= "Error", message="You have not accepted the terms")

selected_project = None  # Initialize it as None
filtered_summary=[]
table_frame = None  # Initialize table_frame as a global variable
selected_template=None
new_project_name=None
# view_add_case=False

def save_new_project():
    print('Save new Project:',selected_template.get(),new_project_name.get())






def create_gui(window):
    global table, table_window  # Declare table as a global variable
    databaseSummary=httpGetAllProjects()
    templates=httpGetAllTemplates()

    def extract_project_names(data):
        project_names = [item['ProjectName'] for item in data]
        project_names.append("New Project")
        return project_names
    
    def extract_template_names(data):
        project_names = [item['TemplateName'] for item in data]
        project_names.append("New Template")
        return project_names
    
    
    
    project_names = extract_project_names(databaseSummary)
    template_names=extract_template_names(templates)
    print("project_names",project_names)
    print('template names:',template_names)

    try:
        # window = tk.Tk()
        # window.title("SuperPyTol")


        # # Create a ttkbootstrap style
        # style = Style()

        # # Apply a style to the window
        # style.theme_use('darkly')

        frame = tk.Frame(window)
        frame.pack(pady=5)

        label = tk.Label(window, text="Add Case")
        label.pack(pady=5)

        
        # Summary
        # Create a StringVar to store the selected value
        global selected_project  # Declare it as a global variable
        selected_project = tk.StringVar()

        global selected_template  # Declare it as a global variable
        selected_template = tk.StringVar()

        global new_project_name # Declare it as a global variable
        new_project_name = tk.StringVar()

        global new_case_name # Declare it as a global variable
        new_case_name = tk.StringVar()



        
        

       
        # Function to update the constant when the Combobox value changes
        
        def update_selected_project(event):
            selected_value = project_combobox.get()
            selected_project.set(project_combobox.get())
            print("Selected Project:", selected_project.get())
            global filtered_summary

            

            filtered_summary = [item for item in databaseSummary if item['ProjectName'] == selected_value]
           

            if selected_value == "New Project":
                # Display the project_name_label and project_name_entry
                project_name_label.grid(row=0, column=2, padx=20, pady=10)
                project_name_entry.grid(row=1, column=2, padx=20, pady=10)
                # Display the roject Template label and Project Templat
                project_templates_label.grid(row=0, column=3, padx=20, pady=10)
                project_templates_combobox.grid(row=1, column=3, padx=20, pady=10)
                #Define Save New Project button
                save_new_project_button.grid(row=1, column=4, padx=20, pady=10)
                
     
                
            else:
                print("filtered_summary.DataCase",filtered_summary[0]["DataCase"])
                # Remove the project_name_label and project_name_entry
                project_name_label.grid_remove()
                project_name_entry.grid_remove()
                project_templates_label.grid_remove()
                project_templates_combobox.grid_remove()
                save_new_project_button.grid_remove()
                # Create the table with the sample data
                print("first table data:",filtered_summary[0]["DataCase"])
                update_table(filtered_summary[0]["DataCase"])
                add_new_case_button.grid(row=2, column=0, padx=20, pady=10)
                
                    

                
        def add_new_case():
            print("Add new case")
            new_case_label.grid(row=3, column=0, padx=20, pady=10)
            new_case_entry.grid(row=4, column=0, padx=20, pady=10)
            add_case_button.grid(row=5, column=0, padx=20, pady=10)

        def add_case():
            print("Case added")
            new_case_label.grid_remove()
            new_case_entry.grid_remove()
            add_case_button.grid_remove()
            print("New casename:",new_case_name.get())
                
        def case_gui_test():
            case_gui(6,1,True)        


        project_info_frame = tk.LabelFrame(frame, text="Projects")
        project_info_frame.grid(row=0, column=0, padx=20, pady=10)

        project_label = tk.Label(project_info_frame, text="Select Project")
        project_label.grid(row=0, column=0, padx=20, pady=10)

        project_combobox = ttk.Combobox(project_info_frame, values=project_names, textvariable=selected_project)
        project_combobox.grid(row=1, column=0)

        # Define project_name_label and project_name_entry
        project_name_label = tk.Label(project_info_frame, text="Enter Project Name")
        project_name_entry = tk.Entry(project_info_frame, textvariable=new_project_name)

        #Define Project Template label and Project Template
        project_templates_label = tk.Label(project_info_frame, text="Select Project Templates")
        project_templates_combobox = ttk.Combobox(project_info_frame, values=template_names, textvariable=selected_template)


        save_new_project_button = ttk.Button(project_info_frame, text="Save", command=save_new_project, style="Primary.TButton")

        add_new_case_button = ttk.Button(project_info_frame, text="Add Case", command=add_new_case, style="Primary.TButton")

        add_case_button = ttk.Button(project_info_frame, text="Add", command=add_case, style="Primary.TButton")


        
         # Define new_case_label and new_case_entry
        new_case_label = tk.Label(project_info_frame, text="Enter Case Name")
        new_case_entry = tk.Entry(project_info_frame, textvariable=new_case_name)

    
        # Button to open the new window
        open_window_button = ttk.Button(window, text="Test Case", command=case_gui_test, style="Primary.TButton")
        open_window_button.pack()

        # Bind the Combobox to the update function
        project_combobox.bind('<<ComboboxSelected>>', update_selected_project)
        # Create the table within the same window
        # Create the table within the same window
        global table_frame
        table_frame = tk.Frame(window)
        table_frame.pack(pady=20)

        # Initialize the _tree attribute when creating the table_frame
        table_frame._tree = ttk.Treeview(table_frame, columns=("ID", "CaseName", "Description", "Author", "Date"))

        table_frame._tree.heading("#1", text="ID")
        table_frame._tree.heading("#2", text="CaseName")
        table_frame._tree.heading("#3", text="Description")
        table_frame._tree.heading("#4", text="Author")
        table_frame._tree.heading("#5", text="Date")

        table_frame._tree.column("#1", width=50)
        table_frame._tree.column("#2", width=100)
        table_frame._tree.column("#3", width=200)
        table_frame._tree.column("#4", width=100)
        table_frame._tree.column("#5", width=150)

        table_frame._tree.pack()
        # window.mainloop()
        # window.mainloop()

        return selected_project

    except Exception as e:
        print("Error creating GUI:", e)
    


def update_table(data):
    global table_frame

    if table_frame is not None:
        # Remove existing table rows
        for item in table_frame._tree.get_children():
            table_frame._tree.delete(item)

        # Insert data into the table
        for item in data:
            table_frame._tree.insert("", "end", values=(item["ID"], item["CaseName"], item["Description"], item["Author"], item["Date"]))



