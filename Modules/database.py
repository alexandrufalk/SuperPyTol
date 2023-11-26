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
    selected_project = tk.StringVar()

     
    # Toplevel object which will 
    # be treated as a new window
    newWindow = tk.Toplevel(root)
    
    # sets the title of the
    # Toplevel widget
    newWindow.title("Database")
    
    # sets the geometry of toplevel
    newWindow.geometry("1000x400")

    
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
    project_templates_combobox = ttk.Combobox(inner_frame, values=project_names, textvariable=selected_project)

    # Display the roject Template label and Project Templat
    project_templates_label.grid(row=3, column=0, padx=20, pady=10)
    project_templates_combobox.grid(row=4, column=0, padx=20, pady=10)

    def test_template(event):
        value=selected_project.get()
        filtered_projects= [item for item in projects if item['ProjectName'] == value]
        print("filtered database data:",filtered_projects[0]['DatabaseDim'])
        database_table(inner_frame,filtered_projects[0]['DatabaseDim'])



    project_templates_combobox.bind("<<ComboboxSelected>>",test_template)


    # template_table(inner_frame, data)
def database_table(window,data):
    print("database table")

    def on_item_click(event):
        selected_item = table_frame_template._tree.focus()  # Get the selected item
        item_text = table_frame_template._tree.item(selected_item, "values")  # Get the values of the selected item
        print("Item clicked:", item_text)
    
    
    table_frame_template= tk.Frame(window)
    table_frame_template.grid(row=5,column=0,padx=10,pady=10)

    # Initialize the _tree attribute when creating the table_frame_template
    table_frame_template._tree = ttk.Treeview(table_frame_template, columns=("Index", "Name", "Description","Unique Identifier","Drw. nr.","Nominal Value","Upper Tolerance","Lower Tolerance"),show='headings')
    # table_frame_template._tree['width'] = 350  # Adjust the width as needed

    table_frame_template._tree.heading("#1", text="Index")
    table_frame_template._tree.heading("#2", text="Name")
    table_frame_template._tree.heading("#3", text="Description")
    table_frame_template._tree.heading("#4", text="Unique Identifier")
    table_frame_template._tree.heading("#5", text="Drw. nr.")
    table_frame_template._tree.heading("#6", text="Nominal Value")
    table_frame_template._tree.heading("#7", text="Upper Tolerance")
    table_frame_template._tree.heading("#8", text="Lower Tolerance")
   
   
    table_frame_template._tree.column("#1", width=50,anchor='center')
    table_frame_template._tree.column("#2", width=100,anchor='center')
    table_frame_template._tree.column("#3", width=100,anchor='center')
    table_frame_template._tree.column("#4", width=100,anchor='center')
    table_frame_template._tree.column("#5", width=100,anchor='center')
    table_frame_template._tree.column("#6", width=100,anchor='center')
    table_frame_template._tree.column("#7", width=100,anchor='center')
    table_frame_template._tree.column("#8", width=100,anchor='center')
  
  
  

    table_frame_template._tree.pack()

    # Populate the table with data
    if data:
        for item in data:
            table_frame_template._tree.insert("", "end", values=(
                item['ID'], item['Name'], item['Description'], item['UniqueIdentifier'], item["DrwNr"], item["NominalValue"], item["UpperTolerance"], item["LowerTolerance"]
            ))

    # Bind the click event to the Treeview
    table_frame_template._tree.bind("<<TreeviewSelect>>", on_item_click)

    return table_frame_template
