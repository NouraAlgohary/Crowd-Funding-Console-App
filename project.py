import json 
import os
import user_functions as uf
import project_functions as pf
import user_project_functions as upf
from datetime import datetime
from pathlib import Path
user_path = "F:\\Career\\ITP\\C2 - Python\\Crowd Funding console app\\users_data.json"
project_path = "F:\\Career\\ITP\\C2 - Python\\Crowd Funding console app\\projects_data.json"

def CreateProject(user_id):
    num = pf.GetProjectNo()
    title = pf.GetTitle()
    details = input('Enter Some Details: ')
    target = int(input("What's your Total Target(EGP)? "))
    st_date = datetime.now().date().strftime("%d-%m-%Y")
    end_date = pf.GetEndDate()

    new_project = {"no":num, "title": title, "details": details, "target": target, 
                   "st_date":st_date, "end_date":end_date, "user_id":user_id}
    
    print(new_project)

    pf.StoreNewProject(new_project)
    print("----------------------------------------------------------")
    print(f"Congrats you have just started {title}!")
    print("----------------------------------------------------------")


##//////////////////////////////////////
def ViewProjects(user_id):
        projectNo_list = upf.FindProjectsForUser(user_id)

        if len(projectNo_list) == 0:
            print("No Projects Found! \n")
        else:
            pf.FindProjectsUsingNo(projectNo_list)
 
##//////////////////////////////////////
def DeleteProject(user_id):
    ViewProjects(user_id)
    title = input('Ptoject Title to edit: \n')

    allproject_list = []
    file = open(project_path)
    for line in file:
        Dict = json.loads(line)
        allproject_list.append(Dict)

    for index, project in enumerate(allproject_list):
        if project['title'] == title and user_id == project["user_id"]:
            allproject_list.remove(project)
            projects = open(project_path, "w")
            for pro in allproject_list:
                json.dump(pro, projects)
                projects.write("\n")
            projects.close()

            print(f"{title} Project Deleted\n")
            return project["no"]

    print("Project Not Found!\n")

##//////////////////////////////////////
def EditProject(user_id):
    ViewProjects(user_id)
    title = input('Ptoject Title: \n')

    pf.EditProjectDetails(title, user_id)

##//////////////////////////////////////
def SearchForProject():
    while True:
        date_string = input("Enter Date (dd-mm-YYYY): ")
        try:
            path = Path(project_path)
            date_format = datetime.strptime(date_string, '%d-%m-%Y')
            # print(date_format)
            if path.stat().st_size == 0:
                print("No Projects Found! \n")
            else:
                list = []
                projects_list = open(path)
                for line in projects_list:
                    project = json.loads(line)
                    print(project['end_date'], "  ", date_format.strftime("%d-%m-%Y"))
                    if project['end_date'] == date_format.strftime("%d-%m-%Y"):
                        print(project)
                        
                        return project
                
                print("Project Not Found! \n")
                return 
        except ValueError:
            print("Invalid Date, please enter in the format dd-mm-YYYY.\n")