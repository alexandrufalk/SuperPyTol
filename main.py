import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from Modules.summary import create_gui
from Modules.case import case_gui, create_histogram, generate_histogram, create_histogram2,pdf, pdf1, case_table,create_vertical_table, statistical_calculation
from Modules.canvas_drw import draw_line,referenceValue
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
    root.title("Matplotlib Histogram in Tkinter")
    style = Style()

    

     # Create a canvas to hold the frame (to make it scrollable)
    canvas_root = tk.Canvas(root)
    canvas_root.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

   # Create a scrollbar
    scrollbarv = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas_root.yview)
    scrollbarv.pack(side=tk.RIGHT, fill=tk.Y)

    scrollbarh = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas_root.xview)
    scrollbarh.pack(side=tk.BOTTOM, fill=tk.X)

   

    # Create a frame to contain the content
    content_frame = tk.Frame(canvas_root)
    

     # Apply a style to the window
    style.theme_use('darkly')

    

    create_gui(content_frame)

    statistical_frame=ttk.Frame(content_frame)
    statistical_frame.pack()

    #first chart
    window_height = content_frame.winfo_screenheight()  # Get the screen height
    canvas_height = int(0.2* window_height)  # Calculate the canvas height


    # Create the canvas with the calculated height
    canvas = tk.Canvas(statistical_frame,height=250,width=500)
    canvas.pack(side = 'left')

  

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

    case_table(content_frame,dataCaseDimFiltered)

    
    # Statistical Tabel
    statistical_calc=statistical_calculation(dataCaseDimFiltered)
    create_vertical_table(statistical_frame, statistical_calc)
    

    plot_button = ttk.Button(statistical_frame, text="Plot PDF", command=lambda: pdf(data))
    plot_button.pack()

    myCanvas = tk.Canvas(root, bg="white", height=600, width=1000)

    # Add a button to get the canvas width
    get_width_button = tk.Button(root, text="Get Canvas Width", command=lambda:draw_line(dataCaseDimFiltered,referenceValue1,myCanvas))
    get_width_button.pack()

    myCanvas.pack()

    button = ttk.Button(content_frame, text="Exit", command=content_frame.quit)
    button.pack(side='left')

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
    












