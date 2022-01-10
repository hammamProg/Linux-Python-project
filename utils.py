
from os import path
from models import Student, SemesterRecord
from typing import Dict, List

def path_id(id: int):
    return path.join("db", str(id) + ".txt")

def get_hours_from_course_id(course_id) -> int:
    
    return int(course_id[5])

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

students: Dict[int, Student] = {}

def read_files():

    from os import walk, path

    filenames = next(walk("db"), (None, None, []))[2]
    
    for filename in filenames:
        
        id = Student.is_valid_id(filename.split(".")[0])
        
        if id is None:
            continue
        
        students[id] = read_file(id)
        
        
        
    for st in students:
        print(st)
        
def is_number(s):
    
    try:
        return int(s)
    except ValueError:
        return None
    
####  ####  ####  ####  ####  ####  ####  ####  ####  
################## Admin Commands ##################
####  ####  ####  ####  ####  ####  ####  ####  ####  

# 1
def add_new_record():
    
    id = is_number(input("Enter Student ID: "))
    
    if id is None:
        print("! invalid input")
        return
    
    if id in students:
        raise "ID is not unique"
    
    with open(path_id(id), 'w'): pass