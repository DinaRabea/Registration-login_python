
print("########################## Login ############################")
import os
from pathlib import Path
entered_email=input("Enter your email: ")
entered_password=input("Enter your password: ")

info=os.system
fl = open("validating.txt", 'r')
info = fl.readlines()
for i in info:
   x=i.split(':')
   y=x[3]
   z=x[4]
   while entered_email==y:
      while entered_password==z:
        print("your login done successfully")
        choice=input("(1)Create Project\n(2)View Project\n(3)Delete Project\n(4)Edit\n(5)Exit\n")
        # ####################choice(1) create#########################
        d=x[1]
        if f"{d}" not in os.listdir():
          os.system("mkdir {name}".format(name=d))
          print(f"{d}Project Directory Created")
        else:
          print(f"{d}Project Directory Created")
        while choice == '1':
           os.system("clear")
           project_name=input("Enter project name: ")
           os.system(f"cd {d} && touch {project_name}")
           print("file created successfully")
           title=input("enter the title: ")
           details=input("enter the details: ")
           total_target=input("Enter your budget: ")
           while not total_target.isnumeric():
                print("please enter numbers")
                total_target = input("enter your Target : ")
           else:                
                Target_data = open(f"{d}/{project_name}", 'w')
                Target_data.write(f"Title:{title}\nDetails:{details}\nTotal_Target:{total_target}\n")
                Target_data.close()
                print("Data Saved Successfully")
                choice=input("(1)Create Project\n(2)View Project\n(3)Delete Project\n(4)Edit\n(5)Exit\n")

 # ################################choice(2) list available projects###########################
 
        while choice=='2':
            os.system("clear")
            os.system(f"cd {d} && ls ")
            choice=input("(1)Create Project\n(2)View Project\n(3)Delete Project\n(4)Edit\n(5)Exit\n")
      
    #   #####################################Delet project##########################

        while choice=='3':
            os.system("clear")
            deleted_file=input("Enter the name you want to delete: ")
            while os.system(f"cd {d} && find . -name {deleted_file} "):
                os.system("clear")
                print("there is no project with this name")
                deleted_file=input("Enter the name you want to delete: ")
            else:
                x=os.system(f"cd {d} && rm {deleted_file} ")
                print(f"project {deleted_file} deleted successfully")
                choice=input("(1)Create Project\n(2)View Project\n(3)Delete Project\n(4)Edit\n(5)Exit\n")
                
    # ################################Edit in available project######################

        while choice=='4':
            os.system("clear")
            edit = input("enter name of the prjoect you want to edit : ")
            while not f"{edit}" in os.listdir(f"/home/dell/FullStack_Python/python/{d}"):
                print("this project isn't exist")
                edit = input("enter name of the prjoect you want to edit: ")
            else:
                os.system("clear")
                title=input("enter the title: ")
                details=input("enter the details: ")
                total_target=input("Enter your budget: ")
                while not total_target.isnumeric():
                  print("please enter numbers")
                  total_target = input("enter your Target : ")
                else:                
                  Target_data = open(f"{d}/{edit}", 'w')
                  Target_data.write(f"Title:{title}\nDetails:{details}\nTotal_Target:{total_target}\n")
                  Target_data.close()
                  print("Data Updated Successfully")
                  choice=input("(1)Create Project\n(2)View Project\n(3)Delete Project\n(4)Edit\n(5)Exit\n")


    # ############################### Exit from program##############################

        while choice=='5':
            os.system("clear")
            print("Good Bye :)")
            exit()
    # if email or pssword is not available
   else:
        print("not match user name or password")
        import login
        import  importlib
        importlib.reload(login)
        



fl.close()

