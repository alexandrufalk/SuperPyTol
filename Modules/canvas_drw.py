import tkinter as tk
from Modules.case import case_gui

canvasDatabase=case_gui(6,1,True)

def referenceValue(canvasDatabase):
    plusValues = sum(
        n["NominalValue"]
        if n["Sign"] == "+"
        else 0
        for n in canvasDatabase
    )

    minusValues = sum(
        n["NominalValue"]
        if n["Sign"] == "-"
        else 0
        for n in canvasDatabase
    )

    referenceValue = max(plusValues, minusValues)

    return referenceValue


# referenceValue1=referenceValue(canvasDatabase)
    

def draw_line(canvasDatabse,referanceValue,myCanvas):
   
    canvas_width = myCanvas.winfo_width()  # Get the canvas width
    acumCanvas = canvas_width / 2
    ymax=0
    id=1
    for n in canvasDatabse:
        x_value = n["NominalValue"]
        sign = n["Sign"]
        color=n["Color"]
        text=n["UniqueIdentifier"] + "-> " + str(n["NominalValue"]) + "±" + str(n["UpperTolerance"])
        x_ref=(x_value * canvas_width) / (2 * referanceValue) if sign == "+" else -(x_value * canvas_width) / (2 * referanceValue)
        print(x_value,sign,color,x_ref)
        # line1 = myCanvas.create_line(x0, y0, x1, y1, ..., xn, yn, options)
        myCanvas.create_line(acumCanvas, 40*id,acumCanvas+x_ref, 40*id, arrow=tk.LAST,fill=color,width=2)
        # Calculate the coordinates for the text
        text_x = (x_ref+2*acumCanvas)/ 2
        text_y = 40*id-10 # Adjust this value to control the vertical position of the text
        # Add text to the line
        myCanvas.create_text(text_x, text_y, text=text, fill=color)
        myCanvas.create_line(acumCanvas+x_ref, 40*id,acumCanvas+x_ref, 40*id+40,fill='black',width=2)
        print("lin1:",acumCanvas, 40*id, x_ref, 40*id)
        print("line2:",x_ref, 40*id, x_ref, 40*id+40)
        acumCanvas=acumCanvas+x_ref
        print('acumCanvas:',acumCanvas)
        ymax=40*id+40
        id=id+1
    myCanvas.create_line(acumCanvas, ymax, canvas_width/2, ymax, arrow=tk.LAST,width=2,fill='red')
    myCanvas.create_text((acumCanvas+canvas_width/2)/2, ymax-10, text="CL", fill="red")
    myCanvas.create_line(canvas_width/2, ymax, canvas_width/2, 40,fill='red',width=2)
    

    
    
    

# init tk
# root = tk.Tk()

# create canvas
# myCanvas = tk.Canvas(root, bg="white", height=300, width=300)




# draw arcs
# coord = 10, 10, 300, 300
# arc = myCanvas.create_arc(coord, start=0, extent=150, fill="red")
# arv2 = myCanvas.create_arc(coord, start=150, extent=215, fill="green")

# line1 = myCanvas.create_line(x0, y0, x1, y1, ..., xn, yn, options)
# line2 = myCanvas.create_line(x0, y0, x1, y1, ..., xn, yn, options)

# myCanvas.create_line(0, 0, 200, 100, arrow=tk.LAST)  
# add to window and show

# Add a button to get the canvas width
# get_width_button = tk.Button(root, text="Get Canvas Width", command=lambda:draw_line(canvasDatabase,referenceValue1))
# get_width_button.pack()

# myCanvas.pack()
# root.mainloop()