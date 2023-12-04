import json
import os
import user_functions as uf
import project_functions as pf
from datetime import datetime
from pathlib import Path
user_path = "F:\\Career\\ITP\\C2 - Python\\Crowd Funding console app\\users_data.json"
project_path = "F:\\Career\\ITP\\C2 - Python\\Crowd Funding console app\\projects_data.json"

# def AddProjectToUser(user_id, PNum):
#     temp_list = []
#     user_found = False
#     with open(user_path, 'r') as file:
#         for line in file:
#             Dict = json.loads(line)
#             if Dict["id"] == user_id:
#                 Dict['PNum'].append(PNum)
#                 user_found = True
#             temp_list.append(Dict)

#     if not user_found:
#         raise ValueError(f"User with id {user_id} not found")

#     with open(user_path, 'w') as f:
#         for user in temp_list:
#             f.write(json.dumps(user) + '\n')

def FindProjectsForUser(user_id):
    path = Path(project_path)
    if not os.path.exists(project_path) or path.stat().st_size == 0:
            return []
    else:
        user_projects  = []
        allproject_list = []
        with open(project_path, 'r') as file:
            for line in file:
                Dict = json.loads(line)
                allproject_list.append(Dict)

        for index, project in enumerate(allproject_list):
            if user_id == project["user_id"]:
                print(project)
                user_projects.append(project)
    
    return user_projects

def DeleteProjectFromUserList(user_id, project_no):
    user_list  = []
    with open(user_path, 'r') as file:
        for line in file:
            Dict = json.loads(line)
            user_list.append(Dict)

    for index, user in enumerate(user_list):
        if user_id == user["id"]:
            print(user["PNum"])
            user["PNum"].remove(project_no)
            users = open(user_path, "w")
            json.dump(user, users)
            users.write("\n")
            users.close()
            return
