
from os import path
from models import Student, SemesterRecord
from typing import Dict, List

students: Dict[int, Student] = {}

def path_id(id: int):
    return path.join("db", str(id) + ".txt")

def get_hours_from_course_id(course_id) -> int:
    
    return int(course_id[5])

def read_file(id: int) -> Student:
    
    semesters = {}
        
    with open( path_id(id) , "r") as f:
        
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
                
            # print("student_id : " + str(id))
            # print("sem : " + str(sem_dict))
            
    return Student(id, semesters=semesters)
    
def write_student(std: Student):
    ''' update student file '''
    
    with open( path_id(std.id) , "w") as f:
        for sem in std.semesters.keys():
            
            line = sem + " ; "
            
            for c_id in std.semesters[sem].marks.keys():
                line += c_id + " " + str(std.semesters[sem].marks[c_id][1]) + ","
                
            f.write(line[:-1] + "\n")

def read_files():

    from os import walk, path

    filenames = next(walk("db"), (None, None, []))[2]
    
    for filename in filenames:
        
        id = Student.is_valid_id(filename.split(".")[0])
        
        if id is None:
            continue
        
        students[id] = read_file(id)
        
        
        
    # for st in students:
    #     print(st)
        
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
    
    if id is None or not Student.is_valid_id(id):
        print("! invalid input")
        return
    
    if id in students:
        raise KeyError("ID is not unique")
    
    students[id] = Student(id, {})
    
    write_student(students[id])
    
    
# 2
def add_semester():
    
    id = is_number(input("Enter Student ID: "))
    
    if id is None or not Student.is_valid_id(id):
        print("! invalid input")
        return
    
    if id not in students:
        raise KeyError("Student with this ID was not found")
    
    year_sem = input("Enter Year/Semester: ")
    
    print("How many courses were completed in this semester : ")
    count = is_number(input())
    
    if not count or count < 1:
        print("! invalid input")
        return
    
    sem_dict = {}
    
    for i in range(count):
        
        course_id = input("Enter Course ID:").strip()
        
        if not course_id or len(course_id) < 7 or (course_id[:4] != "ENEE" and course_id[:4] != "ENCS") :
            print("! invalid input")
            return
        
        mark = is_number(input("Enter Mark:"))
        
        if not mark:
            print("! invalid input")
            return
        
        hours = get_hours_from_course_id(course_id)
        
        sem_dict[course_id] = (mark, hours)
        
    students[id].semesters[year_sem] = SemesterRecord(year_sem=year_sem, courses_dict=sem_dict)
    
    write_student(students[id])
    
    
# 3
def update_mark():
    
    id = is_number(input("Enter Student ID: "))
    
    if id is None or not Student.is_valid_id(id):
        print("! invalid input")
        return
    
    if id not in students:
        raise KeyError("Student with this ID was not found")
    
    course_id = input("Enter Course ID:").strip()
        
    if not course_id or len(course_id) < 7 or (course_id[:4] != "ENEE" and course_id[:4] != "ENCS") :
        print("! invalid input")
        return
    
    for sem in students[id].semesters.values():
        
        if course_id in sem.marks:
            
            mark = is_number(input("Enter Mark:"))
        
            if not mark:
                print("! invalid input")
                return
            
            sem.marks[course_id][1] = mark
            write_student(students[id])
            return
        
    print("Course not found")