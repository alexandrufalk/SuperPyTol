import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from RequestsModules.my_requests import httpGetAllProjects

      

def enter_data():
    accepted = accept_var.get()
    
    if accepted=="Accepted":
        # User info
        firstname = project_name_entry.get()
        lastname = last_name_entry.get()
        
        if firstname and lastname:
            title = project_combobox.get()
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

    project_name_label = ttk.Label(new_window, text="First Name:")
    project_name_label.pack()
    project_name_entry = ttk.Entry(new_window)
    project_name_entry.pack()

    last_name_label = ttk.Label(new_window, text="Last Name:")
    last_name_label.pack()
    last_name_entry = ttk.Entry(new_window)
    last_name_entry.pack()

    # Button to fetch data from the server and save to a file
    fetch_data_button = ttk.Button(new_window, text="Fetch Data and Save", command=httpGetAllProjects)
    fetch_data_button.pack()


selected_project = None  # Initialize it as None
filtered_summary=[]
table_frame = None  # Initialize table_frame as a global variable

def create_gui():
    global table, table_window  # Declare table as a global variable
    databaseSummary=httpGetAllProjects()

    def extract_project_names(data):
        project_names = [item['ProjectName'] for item in data]
        project_names.append("New Project")
        return project_names
    
    project_names = extract_project_names(databaseSummary)
    print("project_names",project_names)

    try:
        window = tk.Tk()
        window.title("SuperPyTol")

        frame = tk.Frame(window)
        frame.pack()

        label = tk.Label(window, text="Click the below button to refresh the window.")
        label.pack()

        
        # Summary
        # Create a StringVar to store the selected value
        global selected_project  # Declare it as a global variable
        selected_project = tk.StringVar()
        

       
        # Function to update the constant when the Combobox value changes
        
        def update_selected_project(event):
            selected_value = project_combobox.get()
            selected_project.set(project_combobox.get())
            print("Selected Project:", selected_project.get())
            global filtered_summary

            filtered_summary = [item for item in databaseSummary if item['ProjectName'] == selected_value]
            print("filtered_summary.DataCase",filtered_summary[0]["DataCase"])

            if selected_value == "New Project":
                # Display the project_name_label and project_name_entry
                project_name_label.grid(row=0, column=2)
                project_name_entry.grid(row=1, column=2)
                
                
            else:
                
                # Remove the project_name_label and project_name_entry
                project_name_label.grid_remove()
                project_name_entry.grid_remove()
                # Create the table with the sample data
                update_table(filtered_summary[0]["DataCase"])
                
                


        project_info_frame = tk.LabelFrame(frame, text="User Information")
        project_info_frame.grid(row=0, column=0, padx=20, pady=10)

        project_label = tk.Label(project_info_frame, text="Select Project")
        project_label.grid(row=0, column=0)

        project_combobox = ttk.Combobox(project_info_frame, values=project_names, textvariable=selected_project)
        project_combobox.grid(row=1, column=0)

        # Define project_name_label and project_name_entry
        project_name_label = tk.Label(project_info_frame, text="Enter Project Name")
        project_name_entry = tk.Entry(project_info_frame)

        # Button to open the new window
        open_window_button = ttk.Button(window, text="Open Database test5", command=open_new_window)
        open_window_button.pack()

        # Bind the Combobox to the update function
        project_combobox.bind('<<ComboboxSelected>>', update_selected_project)
        # Create the table within the same window
        # Create the table within the same window
        global table_frame
        table_frame = tk.Frame(window)
        table_frame.pack()

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
        window.mainloop()

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


if __name__ == '__main__':
    selected_project = create_gui()
    print("Selected Project:", selected_project.get())  # Access it outside of the function
    












