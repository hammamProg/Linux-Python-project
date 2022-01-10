#  Marks System 

# =============>> Functions <<================
def ask_id(): 
    while True:
        try:
            id = int(input('Please Enter Id of the student: '))
            if id < 110000 or id > 1250000:
                raise ValueError #this will send it to the print message and back to the input option
            break
        except:
            print("That's not a valid input ): please enter the id in range of (1100000 - 1220000)")
    return id
def ask_year():
    year = input('Please Enter the current year as format (2000-2001):  ')
    semester = input('Please Enter \n1) first semester\n2) second semseter:  ')
    return (year+semester)
def add_grade():
    while True:
        try:
            grade = int(input('Please Enter grade: '))
            if grade < 0 or grade > 100:
                raise ValueError #this will send it to the print message and back to the input option
            break
        except:
            print("That's not a valid input ): please enter the grades in range of (0 - 100)")   
    return grade 
def add_new_record_file():
    id = ask_id()
    f = open(str(id), "x")
def add_Courses_grades():
    list_courses = {}
    print('Entering course & grade ... ')
    print('how many courses do you want to insert: ')
    num_courses = int(input())
    i=0
    while i<num_courses:
        print('course name: ')
        course_name = input()
        # Inserting grade by add_grade Function to check if the grade in validate range
        course_grade = add_grade()
        list_courses[course_name]=course_grade
        i+=1
    print(list_courses)
    return list_courses

def write_on_file(id,year_semester,courses_and_grades):
    f = open(str(id),'w')
    s1 = year_semester+' ; '
    for course,grade in courses_and_grades.items():
        s1 = s1+course+' '+str(grade)+', '
    f.write(s1)
    f.close()
def update_on_file(id,course_name,new_grade):
    pass
    
def add_new_semester_with_student_course_and_grades():
    print("Please enter the follwing info: ")
    
    # enter id
    id = ask_id()
    while(True):
        try:
            f = open(str(id),'x')
            break
        except:
            print('(error)This Student is already exist!!')
            id = ask_id()
    # f = open(id, "x")
     
    # enter year and semester
    year_semester = ask_year()
    
    # enter courses and thier grades
    courses_and_grades = add_Courses_grades()
    
    write_on_file(id,year_semester,courses_and_grades)
    
def update():
    print("Please Enter Student ID >> ")
    student_id = ask_id()
    file_content=''
    while(True):
        try:
            f = open(str(student_id),'r')
            file_content=f.read()
            f.close()
            break
        except:
            print('(error)This Student is not exist!!')
            student_id = ask_id()
    f = open(str(student_id),'w')
    
    print('FILE Content ')
    print(file_content)
    
    file_content_splited = file_content.split(';')
    
    print('\n\n\n')
    
    courses= file_content_splited[2]
    courses_split= courses.split(' ')
    
    
    
    
    
    print("Please Enter the course >> ")
    course = input()
    
    
    
    print("New Grade >> ")
    new_grade = add_grade()
      
def student_statics():
    print("Please Enter Student ID >> ")
    student_id = input()
    # print all info about this student as number of taken hourse , remaining course
    

# =============>> EndFunctions <<=============

print("Who are you:")
print("1- Student")
print("2- Admin")
user = input()

# Student
if int(user) == 1:
    pass

# Admin
if int(user) == 2:
    print(""" 
        |===================|
          \t Menu\n
        |===================|
        1- Add New Record.
        2- Add new semester with student course and grades
        3- Update
        4- Student statistics
        5- Global statistics
        6- Searching
          """)
    admin_op = int(input())
    if admin_op == 1:
        add_new_record_file()
    elif admin_op == 2:
        add_new_semester_with_student_course_and_grades()
        pass
    elif admin_op == 3:
        update()
        pass
    
    
    
    
    
#  How to make switch cases in python  |-->> 
    
# def x():
#     return

# switcher = {
#     0: 'x',
#     1: '',
#     2: '',
#     3: ''
# }