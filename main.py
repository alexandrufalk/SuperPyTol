import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from Modules.summary import create_gui
from Modules.case import case_gui, create_histogram, generate_histogram, create_histogram2,pdf, pdf1, case_table
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

     
def main():
    # app=create_main_window()
    # create_gui(app)
    data,dataCaseDimFiltered=case_gui(6,1,True)
    print("case gui data",data)
    print("case gui datacaseDimFiltted:",dataCaseDimFiltered)
    upp_tol=min(data)
    low_tol=max(data)
    # create_histogram(data,app)
    root = tk.Tk()
    root.title("Matplotlib Histogram in Tkinter")
    style = Style()
    

     # Apply a style to the window
    style.theme_use('darkly')

    

    create_gui(root)

    #first chart
    window_height = root.winfo_screenheight()  # Get the screen height
    canvas_height = int(0.2* window_height)  # Calculate the canvas height


    # Create the canvas with the calculated height
    canvas = tk.Canvas(root,height=250,width=500)
    canvas.pack()
    

    fig = Figure(figsize=(4,4), dpi=100, facecolor='#696a80')
    ax = fig.add_subplot(111)  #subplot(nrows, ncols, index, **kwargs)

   
    canvas_widget =FigureCanvasTkAgg(fig, master=canvas)
    canvas_widget.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # Fill both horizontally and vertically

    # data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]  # Sample data for the histogram
    # Change the background color of the plot area
    
    
    ax.set_facecolor('#2c2d36')
    
    # create_histogram2(ax, data, "Histogram Example", "Value", "Frequency",upp_tol,low_tol)
    pdf1(ax,data)
    ax.set_prop_cycle(color=[style.colors.primary, style.colors.secondary])

    # Additional styling for the Matplotlib plot
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # table cases

    case_table(root,dataCaseDimFiltered)

    # second chart

    # fig1= Figure(figsize=(6, 6), dpi=100, facecolor='#696a80')  # Set figure background color
    # ax1 = fig1.add_subplot(212)

    

    # canvas1 = FigureCanvasTkAgg(fig1, master=root)
    # canvas_widget1 = canvas1.get_tk_widget()
    # canvas_widget1.pack()

    # ax1.set_facecolor('#2c2d36') # Set plot background color

    # pdf1(ax1,data)
    # ax1.set_prop_cycle(color=[style.colors.primary, style.colors.secondary])

    # # Additional styling for the Matplotlib plot
    # ax1.spines["top"].set_visible(False)
    # ax1.spines["right"].set_visible(False)

    # # Adjust spacing between subplots
    # fig.subplots_adjust(hspace=0.1)  # Adjust the value as needed to control the vertical spacing


    plot_button = ttk.Button(root, text="Plot PDF", command=lambda: pdf(data,root))
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
    












