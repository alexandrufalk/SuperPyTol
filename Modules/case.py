import tkinter as tk
from tkinter import ttk
from RequestsModules.my_requests import httpGetAllProjects, httpAddNewCaseDim, httpDeleteCaseDim
from functools import reduce
import math
import re
import random
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from scipy.stats import norm
import mpldatacursor  # Import mpldatacursor library




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
    print("Random numbers generated:", result)

    samplenum=1000
    genNum = []


    for n in range(0,samplenum):
        genNum.append(round(boxMullerTransform(worstCaseNominal, standard_deviation)[0],2))

    print("genNum:",genNum)


    # # Create a histogram
    # plt.hist(genNum, bins=10, color='blue', edgecolor='black')

    # # Customize the plot
    # plt.title('Histogram Example')
    # plt.xlabel('Values')
    # plt.ylabel('Frequency')

    # # Display the histogram
    # plt.show()

    return genNum


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
    # Create a density plot (KDE)
    plt.figure(figsize=(8, 6))
    plt.title('Probability Density Function (PDF)')
    plt.xlabel('Value')
    plt.ylabel('Density')

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
    plt.plot(x, pdf, 'k-', linewidth=2, label='Normal PDF')

    plt.legend()
    plt.show()




