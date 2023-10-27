import requests
import json

API_URL = "http://localhost:5001/v1/databaseproject"
headers = {"Content-Type": "application/json"}
API_URL_templates = "http://localhost:5001/v1/template";

def httpGetAllProjects():
    try:
        response = requests.get(API_URL)
        data = response.json()  # Use response.json() to parse the JSON data

    except requests.exceptions.RequestException as e:
        print("An error occurred on get all projects:", e)
        data = None  # Set data to None in case of an error
    return data

# test = httpGetAllProjects()

# if test is not None:
#     print("httpGetAllProjects:",test)
# else:
#     print("No data retrieved.")

def httpAddNewProject(project):
    
    try:
        project_json = json.dumps(project)
        response = requests.post(f"{API_URL}/", headers=headers, data=project_json)  # Use the json parameter to send data as JSON
        

    # Handle the response data
        if response.status_code == 200:
            print("Request Add project successful")
            response_data = response.json()
            print(response_data)
        else:
            print("Request Add project failed with status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred at Add Project:", e)

def httpDeleteProject(id):
    try:
        response = requests.delete(f"{API_URL}/{id}")

        if response.status_code == 200:
            print("DELETE project request was successful. Resource deleted.")
        else:
            print(f"DELETE project request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred at delete project: {e}")

def httpAddNewCase(id, addCase):
    try:
        addCase_json = json.dumps(addCase)
        response = requests.post(f"{API_URL}/case/{id}", headers=headers, data=addCase_json)  # Use the json parameter to send data as JSON
        

    # Handle the response data
        if response.status_code == 200:
            print("Request successful addCase")
            response_data = response.json()
            print(response_data)
        else:
            print("Request failed addCase with status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred addCase:", e)



def httpDeleteCase(id, caseId):
    try:
        response = requests.delete(f"{API_URL}/case/{id}/{caseId}")

        if response.status_code == 200:
            print("DELETE case request was successful. Resource deleted.")
        else:
            print(f"DELETE case request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred at delete case: {e}")

# httpDeleteCase(1,3)


def httpAddNewDim(id, newDim):
    try:
        newDim_json = json.dumps(newDim)
        response = requests.post(f"{API_URL}/dim/{id}", headers=headers, data=newDim_json)  # Use the json parameter to send data as JSON
        

    # Handle the response data
        if response.status_code == 200:
            print("Request successful newDim")
            response_data = response.json()
            print(response_data)
        else:
            print("Request failed newDim with status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred newDim:", e)

def httpDeleteDim(id, dimId):
    try:
        response = requests.delete(f"{API_URL}/dim/{id}/{dimId}")

        if response.status_code == 200:
            print("DELETE dim request was successful. Resource deleted.")
        else:
            print(f"DELETE dim request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred at delete dim: {e}")

def httpAddNewCaseDim(id, idCase, newCaseDim):
    try:
        newCaseDim_json = json.dumps(newCaseDim)
        response = requests.post(f"{API_URL}/dimCase/{id}/{idCase}", headers=headers, data=newCaseDim_json)  # Use the json parameter to send data as JSON
        

    # Handle the response data
        if response.status_code == 200:
            print("Request successful newCaseDim")
            response_data = response.json()
            print(response_data)
        else:
            print("Request failed newCaseDim with status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred newCaseDim:", e)

def httpDeleteCaseDim(id, idCase, caseDimID):
    try:
        response = requests.delete(f"{API_URL}/dimCase/{id}/{idCase}/{caseDimID}")

        if response.status_code == 200:
            print("DELETE dimCase request was successful. Resource deleted.")
        else:
            print(f"DELETE dimCase request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred at delete dimCase: {e}")


def httpAddNewImage(id, idDim, file):
    try:
        files = {'img': ('file.jpg', file, 'image/jpeg')}  # Adjust the filename and content type as needed
        url = f"{API_URL}/image/{id}/{idDim}"
        response = requests.post(url, files=files)
        
        if response.status_code == 200:
            print("Request successful add image")
            response_data = response.json()
            print(response_data)
        else:
            print("Request failed add image with status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred add image:", e)

def httpDeleteImg(id, dimId, idImg):
    try:
        response = requests.delete(f"{API_URL}/image/{id}/{dimId}/{idImg}")

        if response.status_code == 200:
            print("DELETE dimCase request was successful. Resource deleted.")
        else:
            print(f"DELETE dimCase request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred at delete dimCase: {e}")


# getting templets


def httpGetAllTemplates():
    try:
        response = requests.get(API_URL_templates)
        data = response.json()  # Use response.json() to parse the JSON data

    except requests.exceptions.RequestException as e:
        print("An error occurred on get all projects:", e)
        data = None  # Set data to None in case of an error
    return data

def httpAddNewTemplate(newTemplate):
    try:
        project_json = json.dumps(newTemplate)
        response = requests.post(f"{API_URL_templates}/", headers=headers, data=project_json)  # Use the json parameter to send data as JSON
        

    # Handle the response data
        if response.status_code == 200:
            print("Request Add new template successful")
            response_data = response.json()
            print(response_data)
        else:
            print("Request Add new template  failed with status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred at Add new template:", e)

def httpDeleteTemplate(id):
    try:
        response = requests.delete(f"{API_URL_templates}/{id}")

        if response.status_code == 200:
            print("DELETE template request was successful. Resource deleted.")
        else:
            print(f"DELETE template request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred at delete template: {e}")

def httpAddDataToTemplate(templateID, newData):
    try:
        addCase_json = json.dumps(newData)
        response = requests.post(f"{API_URL_templates}/{templateID}/data", headers=headers, data=addCase_json)  # Use the json parameter to send data as JSON
        

    # Handle the response data
        if response.status_code == 200:
            print("Request successful template newData")
            response_data = response.json()
            print(response_data)
        else:
            print("Request failed template newData with status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred template newData:", e)

def httpDeleteDataFromTemplate(templateID, dataIndex):
    try:
        response = requests.delete(f"{API_URL_templates}/{templateID}/data/{dataIndex}")

        if response.status_code == 200:
            print("DELETE data template request was successful. Resource deleted.")
        else:
            print(f"DELETE data templete request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred at delete data templete: {e}")