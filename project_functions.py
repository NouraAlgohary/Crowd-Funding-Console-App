import json
from pathlib import Path
from datetime import datetime
import user_functions as uf
import user_project_functions as upf
data_path = "F:\\Career\\ITP\\C2 - Python\\Crowd Funding console app\\"
user_path = "F:\\Career\\ITP\\C2 - Python\\Crowd Funding console app\\users_data.json"
project_path = "F:\\Career\\ITP\\C2 - Python\\Crowd Funding console app\\projects_data.json"

def GetProjectNo():
    try:
        with open(data_path + 'PNums.json', 'r') as f:
            no = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        no = 0

    no += 1

    with open(data_path + 'PNums.json', 'w') as f:
        json.dump(no, f)

    return no

#TITLE
def IsExistTitle(title):
    try:
        with open(data_path + 'used_titles.json', 'r') as f:
            used_titles = set(json.load(f))
    except FileNotFoundError:
        used_titles = set()

    if title in used_titles:
        print("This title is used! \n")
        return True
    else:
        used_titles.add(title)
        with open(data_path + 'used_titles.json', 'w') as f:
            json.dump(list(used_titles), f)
        return False

#TITLE
def GetTitle():
    title = input("Enter Project Title: ")
    while(not title.isalpha() or IsExistTitle(title)):
        print("This title is not valid!")
        title = input("Enter Project Title: ")
    
    return title

#END DATE
def GetEndDate():
    while True:
        date_string = input("Enter End Date (dd-mm-yyyy): ")
        print("string:  ", date_string)
        try:
            date_format = datetime.strptime(date_string, "%d-%m-%Y")
            print('date format:  ', date_format)
            # Check if the date is in the future
            if date_format > datetime.now():
                break
            else:
                print("Invalid Date, date is not in the future.\n")
        except ValueError:
            print("Invalid Date, please enter in the format dd-mm-yyyy.\n")
    
    return date_format.strftime("%d-%m-%Y")

def StoreNewProject(new_project):
    projects_data = open(project_path, "a")
    json.dump(new_project, projects_data)
    projects_data.write("\n")
    projects_data.close()
    
def EditProjectDetails(title, user_id):
    project_list= []
    with open(project_path, 'r') as file:
        for line in file:
            Dict = json.loads(line)
            project_list.append(Dict)

    for project in project_list:
        if project['title'] == title and user_id == project["user_id"]:
            print("Project Data: ", project)
            choice = int(input("Edit: \n1.details\n2.target\n3.exit\n"))
            if choice == 1:
                project_list.remove(project)
                project['details'] = input("Enter New Details\n")
                project_list.append(project)
            elif choice == 2:
                project_list.remove(project)
                project['target'] = int(input("Enter new target\n"))
                project_list.append(project)
            elif choice==3:
                exit()
            else:
                print("Not valid! \n")
                EditProjectDetails(title)

            projects = open(project_path, "w")
            for pro in project_list:
                json.dump(pro, projects)
                projects.write("\n")
            projects.close()

            print(f"{title} Project Edited Successfuly!\n")
            break
    else:
        print("Project Not Found! ")

        
def FindProjectsUsingNo(projectNo_list):
    all_projects = []
    user_projects = []

    with open(project_path, 'r') as file:
        for line in file:
            Dict = json.loads(line)
            all_projects.append(Dict)

    for index, project in enumerate(all_projects):
        if project["no"] in projectNo_list:
            print(project)
            user_projects.append(project)     

    return user_projects