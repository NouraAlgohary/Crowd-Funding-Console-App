import json
import user_functions as uf
user_path = "F:\\Career\\ITP\\C2 - Python\\Crowd Funding console app\\users_data.json"
project_path = "F:\\Career\\ITP\\C2 - Python\\Crowd Funding console app\\projects_data.json"

def Register():
    """This function is used to register a new user to the Crowd-Funding platform."""
    id = uf.GetUserID()
    #NAME
    fname = uf.GetName("First")
    lname = uf.GetName("Last")

    #PHONE
    phone = uf.GetPhone()

    #EMAIL
    email = uf.GetEmail()

    #PASSWORD
    password = uf.GetNewPassword()

    """It stores the new user's data and welcomes them to the Crowd-Funding platform."""
    new_user = {"id":id, "first_name": fname, "last_name": lname, "phone": phone, "email":email, "password":password}
    uf.StoreNewData(new_user)
    print("Welcome to Crowd-Funding!\n")


def Login():
    email = uf.GetEmail(0)
    password = uf.GetUserPassword()

    user_id = 0

    user_list  = []
    try:
        with open(user_path, 'r') as file:
            for line in file:
                Dict = json.loads(line)
                user_list.append(Dict)

        for index, user in enumerate(user_list):
            if email == user["email"] and password == user["password"]:
                print("Welcome ", user["first_name"], "!\n")
                user_id = user['id']
                return user_id
    except TypeError:
        with open(user_path, 'r') as file:
            for line in file:
                Dict = json.loads(line)
                user_list.append(Dict)

        for index, user in enumerate(user_list):
            if email == user[index]["email"] and password == user[index]["password"]:
                print("Welcome ", user[index]["first_name"], "!\n")
                user_id = user['id']
                return user_id
    except FileNotFoundError:
        print("Incorrect email or password!\n")
    
    # if not logged:
    print("Incorrect email or password!\n")