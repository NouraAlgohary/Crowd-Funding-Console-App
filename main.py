#Import all modules
import user as u
import project as p

def homePagelist(user_id):
    if(user_id == -1):
        return
    choice = int(input('Options \n1.Create Project\n2.View All Projects\n3.Edit Project\n4.Delete Project\n5.Search For Project by title\n6.Search For Project by date\n7.Exit\n'))

    if choice == 1:
        p.CreateProject(user_id)
        homePagelist(user_id)
    elif choice == 2:
        p.ViewProjects(user_id)
        homePagelist(user_id)
    elif choice == 3:
        p.EditProject(user_id)
        homePagelist(user_id)
    elif choice == 4:
        p.DeleteProject(user_id)
        homePagelist(user_id)
    elif choice == 5:
        p.SearchForProject()
        homePagelist(user_id)
    elif choice == 6:
        p.SearchForProject()
        homePagelist(user_id)
    elif choice==7:
        exit()
    else:
        print("Invalid choice! \n")

def menu():
    while(True):
        print("Choose from the list:")
        choice = int(input(" 1.Register\n 2.Login\n 3.Exit\n"))

        if choice == 1:
            u.Register()
        elif choice == 2:
            user_id = u.Login()
            if user_id: 
                homePagelist(user_id)
        elif choice == 3:
            exit()
        else:
            print("Enter a valid number")

if __name__ == '__main__':
    menu()