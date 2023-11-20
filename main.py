import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from Modules.summary import create_gui
from Modules.case import case_gui, create_histogram, generate_histogram, create_histogram2,pdf, pdf1, case_table,create_vertical_table, statistical_calculation
from Modules.canvas_drw import draw_line,referenceValue
from Modules.template import openTemplates
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

     
def main():
    # app=create_main_window()
    # create_gui(app)
    data,dataCaseDimFiltered=case_gui(6,1,True)

    referenceValue1=referenceValue(dataCaseDimFiltered)
    print("referenceValue",referenceValue1)

    
    # print("Test",case_gui(6,1,True)[0])
    # print("case gui data",data)
    # print("case gui datacaseDimFiltted:",dataCaseDimFiltered)
    upp_tol=min(data)
    low_tol=max(data)
    # create_histogram(data,app)
    root = tk.Tk()
    root.geometry('1000x800')
    root.title("SuperPyTol")
    style = Style()
     # Apply a style to the window
    style.theme_use('superhero')

    
    
    

     # Create a canvas to hold the frame (to make it scrollable)
    canvas_root = tk.Canvas(root,width=500)
    canvas_root.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

   # Create a scrollbar
    scrollbarv = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas_root.yview)
    scrollbarv.pack(side=tk.RIGHT, fill=tk.Y)

    scrollbarh = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas_root.xview)
    scrollbarh.pack(side=tk.BOTTOM, fill=tk.X)

   

    # Create a frame to contain the content
    content_frame = tk.Frame(canvas_root,borderwidth=2,relief='solid',padx=10,pady=10)


   

    # summary_frame=ttk.Frame(content_frame)
    # summary_frame.pack(side='left',padx=10, pady=10)

    first_frame=ttk.Frame(content_frame,borderwidth=2,relief='solid')
    first_frame.grid(row=0,column=0,padx=10,pady=10)


    side_nav=ttk.Frame(first_frame,borderwidth=2,relief='solid')
    side_nav.grid(row=0, column=0,padx=10)
    # side_nav_label=ttk.Label(first_frame,text="Side nav")
    # side_nav_label.pack(fill='both',expand='yes')

    summary_frame=ttk.Frame(first_frame,width=300,borderwidth=2,relief='solid')
    summary_frame.grid(row=0,column=1)
    


    

    create_gui(summary_frame)

   

    statistical_frame=ttk.Frame(content_frame,borderwidth=2,relief='solid')
    statistical_frame.grid(row=1,column=0,padx=10,pady=10)


    # Create the canvas with the calculated height
    canvas = tk.Canvas(statistical_frame,height=600, width=300)
    canvas.pack(side='left',padx=10,pady=10)

  

    fig = Figure(figsize=(4,4), dpi=100, facecolor='#696a80')
    ax = fig.add_subplot(111)  #subplot(nrows, ncols, index, **kwargs)

   
    canvas_widget =FigureCanvasTkAgg(fig, master=canvas)
    canvas_widget.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # Fill both horizontally and vertically

    
    ax.set_facecolor('#2c2d36')
    
    # create_histogram2(ax, data, "Histogram Example", "Value", "Frequency",upp_tol,low_tol)
    pdf1(ax,data)
    ax.set_prop_cycle(color=[style.colors.primary, style.colors.secondary])

    # Additional styling for the Matplotlib plot
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    # table cases

    table_frame=ttk.Frame(content_frame)
    table_frame.grid(row=2,column=0)

    case_table(table_frame,dataCaseDimFiltered)

    
    # Statistical Tabel
    statistical_calc=statistical_calculation(dataCaseDimFiltered)
    create_vertical_table(statistical_frame, statistical_calc)

    button_frame=ttk.Frame(statistical_frame)
    button_frame.pack(side='left',padx=10)
    

    plot_button = ttk.Button(button_frame, text="Plot PDF", command=lambda: pdf(data))
    plot_button.pack(pady=10,side='top',padx=10)

    myCanvas = tk.Canvas(statistical_frame, height=600, width=500,background='gray')

    # Add a button to get the canvas width
    get_width_button = tk.Button(button_frame, text="Draw tolerance chain", command=lambda:draw_line(dataCaseDimFiltered,referenceValue1,myCanvas))
    get_width_button.pack(pady=10,side='bottom')

     # Add side buttons
    side_template= ttk.Button(side_nav, bootstyle="info", text="Template", command=lambda:openTemplates(content_frame))
    side_template.pack(padx=10,pady=10)

    
    side_database= ttk.Button(side_nav,bootstyle="success",text="Database", command=lambda:print("Side test database"))
    side_database.pack(padx=10,pady=10)

    side_case= tk.Button(side_nav, text="Case", command=lambda:print("Side test case"))
    side_case.pack(padx=10,pady=10)

    





    myCanvas.pack(side='left',padx=10,pady=10)

    button = ttk.Button(content_frame, text="Exit", command=content_frame.quit)
    button.grid(pady=10)

    # Attach the content_frame to the canvas
    canvas_root.create_window((0, 0), window=content_frame, anchor=tk.NW)

    

    # Configure the scrollbars
    canvas_root.config(yscrollcommand=scrollbarv.set, xscrollcommand=scrollbarh.set)

     # Update the canvas to fit the content
    content_frame.update_idletasks()
    canvas_root.config(scrollregion=canvas_root.bbox("all"))
    




        
    
    root.mainloop()
    

   

if __name__ == '__main__':
    # selected_project = create_gui()
    # print("Selected Project:", selected_project.get())  # Access it outside of the function
    # print("Selected Template:", selected_template.get())  # Access it outside of the function
    main()
    












