from utils import read_files, add_semester, add_new_record, is_number

##########################################

def admin():
    
    while(True):
    
        print("""\n 
|===================|
  \t Menu
|===================|\n
1- Add New Record.
2- Add new semester with student course and grades
3- Update
4- Student statistics
5- Global statistics
6- Searching
7- Exit\n
Enter Command Number: 
            """)
        
        cmd = is_number(input())
        if cmd == 1:
            
            try:
                add_new_record()
            except KeyError:
                print("\nID is not unique")
        elif cmd == 2:
            try:
                add_semester()
            except KeyError:
                print("\nID not found")
        elif cmd == 3:
            pass
        elif cmd == 4:
            pass
        elif cmd == 5:
            pass
        elif cmd == 6:
            pass
        else:
            break
        

def student():
    pass

##########################################

user_type = int(input("\n\nEnter 1 for admin login, 2 for student: "))

read_files()

if user_type == 1:
    admin()
else:
    student()
