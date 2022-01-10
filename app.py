from utils import read_files

##########################################

def admin():
    read_files()
    pass

def student():
    pass

##########################################

user_type = int(input("Enter 1 for admin login, 2 for student: "))

if user_type == 1:
    admin()
else:
    student()
