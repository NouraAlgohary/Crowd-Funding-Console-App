import re
import os
import json
from datetime import datetime
from pathlib import Path
data_path = "F:\\Career\\ITP\\C2 - Python\\Crowd Funding console app\\"
user_path =  data_path  + "users_data.json"
project_path = data_path + "projects_data.json"

#ID
def GetUserID():
    # This function assures all ids are unique[PK] 
    # It stores "id" in a json file 
    id_file = os.path.join(data_path, 'ids.json')
    if os.path.exists(id_file):
        with open(id_file, 'r') as f:
            id = json.load(f)
    else:
        id = 0

    id+=1

    os.makedirs(data_path, exist_ok=True)

    with open(id_file, 'w') as f:
        json.dump(id, f)

    return id

# EMAIL
def isValidEmail(email):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if(re.fullmatch(email_regex, email)):
        return True
    else:
        return False

def IsExistEmail(email):
    try:
        with open(data_path + "used_emails.json", 'r') as f:
            used_emails = set(json.load(f))
    except FileNotFoundError:
        used_emails = set()

    if email in used_emails:
        print("This email is used! \n")
        return True
    else:
        used_emails.add(email)
        with open(data_path + "used_emails.json", 'w') as f:
            json.dump(list(used_emails), f)
        return False

def GetEmail(new = 1):
    email = input("Enter Email: ")
    while(not isValidEmail(email) or (new and IsExistEmail(email))):
        print("This email is not valid!")
        email = input("Enter Email: ")

    return email

# Get Name
def GetName(key = "First"):
    name = input(f"Enter {key} Name: ")
    while(not name.isalpha()):
        print(f"This first {key} is not valid!")
        name = input(f"Enter {key} Name: ")
    return name

#PHONE
def IsValidPhone(phone):
    #This function checks if a phone is a valid Egyptian phone number
    phone_number_regex = r'^01[0-2,5]\d{8}$'

    if(re.fullmatch(phone_number_regex, phone)):
        return True
    else:
        return False
    
def GetPhone():
    phone = input("Enter Mobile Phone: ")
    #check mobile phone
    while(not IsValidPhone(phone)):
        print("This phone number is not valid!")
        phone = input("Enter Mobile Phone: ")

    return phone

#PASSWORD
def GetNewPassword(new = 1):
    password = input("Enter Password: ")
    confirm_password = input("Confirm Password: ")
    
    #check password
    while(password != confirm_password):
        print("Not matched\n")
        password = input("Enter Password: ")
        confirm_password = input("Confirm Password: ")

    return password

def GetUserPassword():
    password = input("Enter Password: ")
    while(not password):
        password = input("Enter Password: ")

    return password

def GetData(file_path):
    data_list= []
    with open(file_path, 'r') as file:
        for line in file:
            dict = json.loads(line)
            data_list.append(dict)
    
    return data_list

def DeleteUser(user_id):
    user_list  = []
    with open(user_path, 'r') as file:
        for line in file:
            Dict = json.loads(line)
            user_list.append(Dict)

    for index, user in enumerate(user_list):
        if user_id == user["id"]:
            user_list.remove(user)
            break 

    with open(user_path, 'w') as f:
        json.dump(user_list, f)

def StoreNewData(new_user):
    users_data = open(user_path, "a")
    json.dump(new_user, users_data)
    users_data.write("\n")
    users_data.close()