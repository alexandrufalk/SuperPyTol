import tkinter as tk
from tkinter import ttk
from RequestsModules.my_requests import httpGetAllTemplates


table_frame_template = None  # Initialize table_frame_case_case as a global variable

 # Open templates window
def openTemplates(root):

    templates=httpGetAllTemplates()


    def extract_template_names(data):
        project_names = [item['TemplateName'] for item in data]
        project_names.append("New Template")
        return project_names
    
    template_names=extract_template_names(templates)
    




    

    # templateFiltered=templates[templateId-1]



    new_template_name = tk.StringVar()
    selected_template = tk.StringVar()


    

    
     
    # Toplevel object which will 
    # be treated as a new window
    newWindow = tk.Toplevel(root)
    
    # sets the title of the
    # Toplevel widget
    newWindow.title("Templates")
    
    # sets the geometry of toplevel
    newWindow.geometry("400x400")

    # template_info_frame = tk.LabelFrame(newWindow, text="Templates")
    # template_info_frame.pack()
    # template_info_frame.grid(row=0, column=0, padx=20, pady=10)

    
    
    # project_name_label.grid(row=0, column=2, padx=20, pady=10)
    # project_name_entry.grid(row=1, column=2, padx=20, pady=10)
    # # A Label widget to show in toplevel
    # tk.Label(newWindow, text ="Templates").pack()
    # button = ttk.Button(newWindow, text="Exit", command=newWindow.destroy)
    # button.pack(side='left',padx=10,pady=10)
     # Create a frame inside the Toplevel window using grid
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
    project_templates_label = tk.Label(inner_frame, text="Select Project Templates")
    project_templates_combobox = ttk.Combobox(inner_frame, values=template_names, textvariable=selected_template)

    # Display the roject Template label and Project Templat
    project_templates_label.grid(row=3, column=0, padx=20, pady=10)
    project_templates_combobox.grid(row=4, column=0, padx=20, pady=10)

    def test_template(event):
        value=selected_template.get()
        filtered_template = [item for item in templates if item['TemplateName'] == value]
        print("filtered template data:",filtered_template[0]['Data'])
        template_table(inner_frame,filtered_template[0]['Data'])



    project_templates_combobox.bind("<<ComboboxSelected>>",test_template)


    # template_table(inner_frame, data)


def template_table(window,data):
    print("second table")
    
    
    table_frame_template= tk.Frame(window)
    table_frame_template.grid(row=5,column=0,padx=10,pady=10)

    # Initialize the _tree attribute when creating the table_frame_template
    table_frame_template._tree = ttk.Treeview(table_frame_template, columns=("Index", "Component Name", "Color"),show='headings')
    # table_frame_template._tree['width'] = 350  # Adjust the width as needed

    table_frame_template._tree.heading("#1", text="Index")
    table_frame_template._tree.heading("#2", text="Component Name")
    table_frame_template._tree.heading("#3", text="Color")
    # table_frame_template._tree.heading("#4", text="Nominal Value")
    # table_frame_template._tree.heading("#5", text="Upper Tolerance")
    # table_frame_template._tree.heading("#6", text="Lower Tolerance")
    # table_frame_template._tree.heading("#7", text="Sign")
    # table_frame_template._tree.heading("#8", text="Distribution Type")
    # table_frame_template._tree.heading("#9", text="Tolerance Type")
    # table_frame_template._tree.heading("#10", text="Influence %")
    # table_frame_template._tree.heading("#11", text="Formula")
    # table_frame_template._tree.heading("#12", text="Remove")

    # # Show grid lines
    # style = ttk.Style()
    # style.configure("Treeview", rowheight=30, borderwidth=1, relief="solid")

    


   
   
    table_frame_template._tree.column("#1", width=50,anchor='center')
    table_frame_template._tree.column("#2", width=100,anchor='center')
    table_frame_template._tree.column("#3", width=100,anchor='center')
    # table_frame_template._tree.column("#4", width=100)
    # table_frame_template._tree.column("#5", width=100)
    # table_frame_template._tree.column("#6", width=100)
    # table_frame_template._tree.column("#7", width=100)
    # table_frame_template._tree.column("#8", width=100)
    # table_frame_template._tree.column("#9", width=100)
    # table_frame_template._tree.column("#10", width=100)
    # table_frame_template._tree.column("#11", width=100)
    # table_frame_template._tree.column("#12", width=100)

    table_frame_template._tree.pack()

    # Populate the table with data
    if data:
        for item in data:
            table_frame_template._tree.insert("", "end", values=(
                item['Index'], item['ComponentName'], item['Color']
            ))

    return table_frame_template
    
    

def update_table_case(data):
    print("update table template is running")
    global table_frame_template
    

    if table_frame_template is not None:
        # Remove existing table rows
        for item in table_frame_template._tree.get_children():
            table_frame_template._tree.delete(item)

        # Insert data into the table
        for item in data:
            table_frame_template._tree.insert("", "end", values=(item['Index'], item['ComponentName'], item['Color']))


def create_vertical_table(window, data):
    # Create a frame for the vertical table
    frame_vertical_table = tk.Frame(window)
    frame_vertical_table.pack(side='left')

    # Create a Text widget for the table
    table = tk.Text(frame_vertical_table, height=len(data) * 2, width=20)
    table.pack()

    # Insert the data vertically
    for key, value in data.items():
        table.insert(tk.END, f"{key}:\n{value}\n")