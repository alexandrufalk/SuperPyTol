import tkinter as tk
from tkinter import ttk
from RequestsModules.my_requests import httpGetAllProjects, httpAddNewCaseDim, httpDeleteCaseDim
from functools import reduce
import math
import statistics
import re
import random
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from scipy.stats import norm
import mpldatacursor  # Import mpldatacursor library


table_frame_case = None  # Initialize table_frame_case_case as a global variable

def case_gui(projectId, caseId, ViewDatabase ):
    print("Case GUI")
    databaseProjects=httpGetAllProjects()

    if projectId < 1 or projectId > len(databaseProjects):
        print("Invalid projectId")
        return
    
    project = databaseProjects[projectId - 1]
    
    if caseId < 1 or caseId > len(project["DataCase"]):
        print("Invalid caseId")
        return
    
    dataCase = project["DataCase"][caseId - 1]
    dataCaseDimFiltered = dataCase.get("CaseData", [])  # Use .get() to handle missing keys gracefully

    if not dataCaseDimFiltered:
        print("CaseData not found or empty")
        return

    # Worst case nominal
    worstCaseNominal,worstCaseTolerance=worst_case_calculation(dataCaseDimFiltered)
    
    

    print("worstCaseTolerance:",worstCaseTolerance)

    def calculate_standard_deviation(dataCaseDimFiltered):
        standard_deviations = [
            
                math.pow(
                    ((n["UpperTolerance"] - n["LowerTolerance"]) /
                    (6 * float(re.sub(r"[^\d.]", "", n["DistributionType"])))),
                    2
                )
            
      
            for n in dataCaseDimFiltered
        ]

        for n in dataCaseDimFiltered:
            numeric_part =math.pow((n["UpperTolerance"] - n["LowerTolerance"])/(6 * float(re.sub(r"[^\d.]", "", n["DistributionType"]))),2)
            print("numeric_part:",numeric_part)
        
        print("standard_deviation 1:",standard_deviations)

        standard_deviation = round(math.sqrt(sum(standard_deviations)), 2)

        return standard_deviation
    
    standard_deviation = calculate_standard_deviation(dataCaseDimFiltered)
    print("Standard Deviation:", standard_deviation)

    def boxMullerTransform(mu, sigma):
        # Generate two random numbers uniformly distributed between 0 and 1
        u1 = random.random()
        u2 = random.random()

        # Apply the Box-Muller transform to generate two normally distributed random numbers
        z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        z1 = math.sqrt(-2 * math.log(u1)) * math.sin(2 * math.pi * u2)

        # Apply mean (mu) and standard deviation (sigma) transformations
        x0 = mu + z0 * sigma
        x1 = mu + z1 * sigma

        return x0, x1

   

    result = boxMullerTransform(worstCaseNominal, standard_deviation)
    # print("Random numbers generated:", result)

    samplenum=100000
    genNum = []


    for n in range(0,samplenum):
        genNum.append(round(boxMullerTransform(worstCaseNominal, standard_deviation)[0],2))

    # print("genNum:",genNum)


    # # Create a histogram
    # plt.hist(genNum, bins=10, color='blue', edgecolor='black')

    # # Customize the plot
    # plt.title('Histogram Example')
    # plt.xlabel('Values')
    # plt.ylabel('Frequency')

    # # Display the histogram
    # plt.show()

    return genNum,dataCaseDimFiltered 

def worst_case_calculation(dataCaseDimFiltered):
    
    # Worst case nominal
    worstCaseNominal = sum(
        (n["NominalValue"] + (n["LowerTolerance"] + n["UpperTolerance"]) / 2)
        if n["Sign"] == "+"
        else -(n["NominalValue"] + (n["LowerTolerance"] + n["UpperTolerance"]) / 2)
        for n in dataCaseDimFiltered
)
    # Round to three decimal places
    worstCaseNominal = round(worstCaseNominal, 3)

    print("worstCaseNominal:",worstCaseNominal)

    #worst case tolerance

    worstCaseTolerance=sum((n["UpperTolerance"]-n["LowerTolerance"])/2 for n in dataCaseDimFiltered ) 

    worstCaseTolerance=round(worstCaseTolerance,3)

    print("worstCaseTolerance:",worstCaseTolerance)
    return worstCaseNominal,worstCaseTolerance


def statistical_calculation(dataCaseDimFiltered):
    worstCaseNominal,worstCaseTolerance=worst_case_calculation(dataCaseDimFiltered)
    cpk=1.67
    genNum=case_gui(6,1,True)[0]
    mean=statistics.mean(genNum)
    stddev=statistics.stdev(genNum)
    statisticalTol = 6 * stddev * cpk
    Pp = (2 * worstCaseTolerance) / (6 * stddev)
    PpkU =(worstCaseNominal + worstCaseTolerance - mean) /(3 * stddev)
    PpkL =(mean- (worstCaseNominal - worstCaseTolerance)) /(3 * stddev)
    Ppk=min(PpkL,PpkU)
    sigmaintv = (2 * worstCaseTolerance) / stddev

    statistical_calc={
      "meanS": mean,
      "UTS": statisticalTol / 2,
      "LTS": -statisticalTol / 2,
      "Samples": 100000,
      "Range": statisticalTol,
      "Pp": Pp,
      "PpK": Ppk,
      "StDev": stddev,
      "SigmaInt": sigmaintv
    }


    return statistical_calc


def create_histogram(data, window):
    # Create a frame to hold the histogram
    histogram_frame = ttk.Frame(window)
    histogram_frame.pack(fill="both", expand=True)

    # Generate the histogram
    fig, ax = generate_histogram(data)

    # Embed the Matplotlib figure in a Tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=histogram_frame)
    canvas.get_tk_widget().pack(fill="both", expand=True)

def generate_histogram(data):
    fig, ax = plt.subplots(figsize=(6, 4))
    fig, ax = plt.subplots(facecolor=(.18, .31, .31))
    ax.hist(data, bins=10, edgecolor='black', alpha=0.7)
    ax.set_xlabel('Values')
    ax.set_ylabel('Frequency')
    ax.set_title('Sample Histogram')
    return fig, ax

def create_histogram2(ax, data, title, x_label, y_label,upp_tol,low_tol):
    ax.hist(data, bins=50,density=True, alpha=0.7,range=(upp_tol,low_tol), color='#46e3c9', edgecolor='black')
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

def pdf(data):
    # Create a new Tkinter window for the PDF plot
    pdf_window = tk.Tk()
    pdf_window.title("PDF Plot")

    
    # Create a density plot (KDE)

    fig = plt.figure(figsize=(8, 6), facecolor='#696a80')  # Set figure background color
    # plt.figure(figsize=(8, 6),facecolor='#696a80')
    plt.title('Probability Density Function (PDF)')
    plt.xlabel('Value')
    plt.ylabel('Density')

    # Convert the list to a NumPy array
    data = np.array(data)

    ax = plt.gca()
    ax.set_facecolor('#2c2d36') # Set plot background color

    # Use seaborn for a smoother KDE plot (optional, you may need to install seaborn)
    # import seaborn as sns
    # sns.kdeplot(data, color='blue', label='KDE')

    # Alternatively, you can use Matplotlib's hist method with density=True
    
    
    plt.hist(data, bins=50, density=True, alpha=0.7, color='#46e3c9', edgecolor='black', label='KDE')

    # If you know the underlying probability distribution, you can overlay it for comparison
    # For example, using a normal distribution as a reference
    mu, std = norm.fit(data)
    x = np.linspace(min(data), max(data), 100)
    pdf = norm.pdf(x, mu, std)
    plt.plot(x, pdf, 'k-', color='#0aedf5', linewidth=2, label='Normal PDF')

    plt.legend()
    plt.show()

    canvas = FigureCanvasTkAgg(fig, master=pdf_window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()


def pdf1(plt,data):
    

    # Create a density plot (KDE)

    # plt.title('Probability Density Function (PDF)')
    # plt.xlabel('Value')
    # plt.ylabel('Density')

    # Convert the list to a NumPy array
    data = np.array(data)

    

    # Use seaborn for a smoother KDE plot (optional, you may need to install seaborn)
    # import seaborn as sns
    # sns.kdeplot(data, color='blue', label='KDE')

    # Alternatively, you can use Matplotlib's hist method with density=True
    
    
    plt.hist(data, bins=50, density=True, alpha=0.7, color='#46e3c9', edgecolor='black', label='KDE')

    # If you know the underlying probability distribution, you can overlay it for comparison
    # For example, using a normal distribution as a reference
    mu, std = norm.fit(data)
    x = np.linspace(min(data), max(data), 100)
    pdf = norm.pdf(x, mu, std)
    plt.plot(x, pdf, color='#0aedf5', linewidth=2, label='Normal PDF')

    plt.legend()
    # plt.show()
    plt.set_title('Probability Density Function (PDF)')
    plt.set_xlabel('Value')
    plt.set_ylabel('Density')

def case_table(window,data):
    print("second table")
    
    
    table_frame_case= tk.Frame(window)
    table_frame_case.pack()

    # Initialize the _tree attribute when creating the table_frame_case
    table_frame_case._tree = ttk.Treeview(table_frame_case, columns=("ID", "Name", "Description", "Nominal Value", "Upper Tolerance","Lower Tolerance","Sign","Distribution Type","Tolerance Type"),show='headings')

    table_frame_case._tree.heading("#1", text="ID")
    table_frame_case._tree.heading("#2", text="Name")
    table_frame_case._tree.heading("#3", text="Description")
    table_frame_case._tree.heading("#4", text="Nominal Value")
    table_frame_case._tree.heading("#5", text="Upper Tolerance")
    table_frame_case._tree.heading("#6", text="Lower Tolerance")
    table_frame_case._tree.heading("#7", text="Sign")
    table_frame_case._tree.heading("#8", text="Distribution Type")
    table_frame_case._tree.heading("#9", text="Tolerance Type")
    # table_frame_case._tree.heading("#10", text="Influence %")
    # table_frame_case._tree.heading("#11", text="Formula")
    # table_frame_case._tree.heading("#12", text="Remove")

    table_frame_case._tree.column("#1", width=50,anchor='center')
    table_frame_case._tree.column("#2", width=100,anchor='center')
    table_frame_case._tree.column("#3", width=200,anchor='center')
    table_frame_case._tree.column("#4", width=100,anchor='center')
    table_frame_case._tree.column("#5", width=100,anchor='center')
    table_frame_case._tree.column("#6", width=100,anchor='center')
    table_frame_case._tree.column("#7", width=100,anchor='center')
    table_frame_case._tree.column("#8", width=100,anchor='center')
    table_frame_case._tree.column("#9", width=100,anchor='center')
    # table_frame_case._tree.column("#10", width=100)
    # table_frame_case._tree.column("#11", width=100)
    # table_frame_case._tree.column("#12", width=100)

    table_frame_case._tree.pack()

    # Populate the table with data
    if data:
        for item in data:
            table_frame_case._tree.insert("", "end", values=(
                item['ID'], item['Name'], item['Description'], item['NominalValue'],
                item['UpperTolerance'], item['LowerTolerance'], item['Sign'],
                item['DistributionType'], item['ToleranceType'], item['Color']
            ))

    return table_frame_case
    
    

def update_table_case(data):
    print("update table case is running")
    global table_frame_case
    

    if table_frame_case is not None:
        # Remove existing table rows
        for item in table_frame_case._tree.get_children():
            table_frame_case._tree.delete(item)

        # Insert data into the table
        for item in data:
            table_frame_case._tree.insert("", "end", values=(item["ID"], item["Name"], item["Description"], item["Nominal Value"], item["Upper Tolerance"], item["Lower Tolerance"], item["Sign"], item["Distribution Type"], item["Tolerance Type"]))


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
