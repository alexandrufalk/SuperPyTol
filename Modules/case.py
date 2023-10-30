import tkinter as tk
from tkinter import ttk
from RequestsModules.my_requests import httpGetAllProjects, httpAddNewCaseDim, httpDeleteCaseDim
from functools import reduce




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
