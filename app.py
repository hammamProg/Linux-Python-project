from typing import List
from utils import get_hours_from_course_id
from models import Student, SemesterRecord
from os import path

students: List[Student] = []

def read_file(id: int) -> Student:
    
    semesters = {}
        
    with open( path.join("db", str(id) + ".txt") , "r") as f:
        
        for line in f.readlines():
            
            year_sem = line.split(";")[0].strip()
            
            recs = line.split(";")[1].split(",")
            
            sem_dict = {}
            
            
            for r in recs:
                splitted = r.strip().split(" ")
                
                course_id = splitted[0]
                mark = float(splitted[1])
                
                hours = get_hours_from_course_id(course_id)
                
                sem_dict[course_id] = (mark, hours)
                
                semesters[year_sem] = SemesterRecord(year_sem=year_sem, courses_dict=sem_dict)
                
            print("student_id : " + str(id))
            print("sem : " + str(sem_dict))
            
    return Student(id, semesters=semesters)
    

def read_files():

    from os import walk, path

    filenames = next(walk("db"), (None, None, []))[2]
    
    for filename in filenames:
        
        id = Student.is_valid_id(filename.split(".")[0])
        
        if id is None:
            continue
        
        students.append(read_file(id))
        
        
        
    for st in students:
        print(st)
##########################################

def admin():
    read_files()
    pass

def student():
    pass

user_type = int(input("Enter 1 for admin login, 2 for student: "))

if user_type == 1:
    admin()
else:
    student()
