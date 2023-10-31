import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from Modules.summary import create_gui
from Modules.case import case_gui, create_histogram, generate_histogram, create_histogram2,pdf
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

     
def main():
    # app=create_main_window()
    # create_gui(app)
    data=case_gui(6,1,True)
    upp_tol=min(data)
    low_tol=max(data)
    # create_histogram(data,app)
    root = tk.Tk()
    root.title("Matplotlib Histogram in Tkinter")
    style = Style()

     # Apply a style to the window
    style.theme_use('darkly')

    create_gui(root)
    

    fig = Figure(figsize=(6, 4), dpi=100, facecolor='#696a80')
    ax = fig.add_subplot(111)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    # data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]  # Sample data for the histogram
    # Change the background color of the plot area
    
    
    ax.set_facecolor('#2c2d36')
    
    create_histogram2(ax, data, "Histogram Example", "Value", "Frequency",upp_tol,low_tol)
    ax.set_prop_cycle(color=[style.colors.primary, style.colors.secondary])

    # Additional styling for the Matplotlib plot
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    

    plot_button = ttk.Button(root, text="Plot PDF", command=lambda: pdf(data))
    plot_button.pack()

    button = ttk.Button(root, text="Exit", command=root.quit)
    button.pack()


        
    # app.mainloop()
    root.mainloop()
    

    # # Create a ttkbootstrap style
    # style = Style()

    #  # Apply a style to the window
    # style.theme_use('darkly')

    # window = tk.Tk()
    # window.title("SuperPyTol")

    
    # # Create tabs to organize different functionalities
    # tab_control = ttk.Notebook(window)
    # tab1 = ttk.Frame(tab_control)
    # tab2 = ttk.Frame(tab_control)

    # # Tab 1 - GUI
    # tab_control.add(tab1, text="GUI")
    # create_gui(tab1)

    # data=case_gui(6,1,True)
    # print("data main:",data)

    # # Tab 2 - Histogram
    # tab_control.add(tab2, text="Histogram")
    # create_histogram(data,tab2)

    # # # Tab 3 - Table
    # # tab3 = ttk.Frame(tab_control)
    # # tab_control.add(tab3, text="Table")
    # # create_table1(tab3)

    # tab_control.pack(fill="both", expand=True)

    # window.mainloop()

if __name__ == '__main__':
    # selected_project = create_gui()
    # print("Selected Project:", selected_project.get())  # Access it outside of the function
    # print("Selected Template:", selected_template.get())  # Access it outside of the function
    main()
    












