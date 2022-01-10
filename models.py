''' Python Classes '''

from typing import Tuple


class SemesterRecord():
    ''' class for saving data of a student in a semester '''
    
    def semester_calc(self) -> Tuple[int, float]:
        ''' returns the GPA of the current semester '''
        
        hours: int = 0
        sum: float = 0.0
        
        for course_id in self.marks.keys():
            hours += self.marks[course_id][0]
            sum += self.marks[course_id][1]
            
        return hours, sum / hours
    
    def __init__(self, year_sem: str, courses_dict: dict[str, Tuple[int, float]]) -> None:
        
        self.year_sem = year_sem
        self.marks = courses_dict
        
        self.hours, self.avg = self.semester_calc()
        
        

class Student():
    ''' Student Class '''
    
    def calc(self) -> Tuple[float, int]:
        ''' calculate avg, sum of hours'''
        
        overall_hours: int = 0
        gpa: float = 0.0
        
        for sem in self.semesters.keys():
            
            points = ( overall_hours * gpa ) + ( self.semesters[sem].hours * self.semesters[sem].avg )
            overall_hours += self.semesters[sem].hours
            gpa = points / overall_hours
        
        return gpa, overall_hours
    
    def __init__(self, id: int, semesters: dict[str, SemesterRecord]) -> None:
        
        self.id = id
        self.semesters = semesters
        # self.gpa , self.hours = self.calc()
        # self.avg_hours_per_sem = self.hours / len(semesters.keys())
        
    def __str__(self) -> str:
        return "[ID:" + str(self.id) + ", gpa:" + str(self.gpa) + ", hours:" + str(self.hours) + ", semesters: " + str(self.semesters) + " ]"
        
    @staticmethod
    def is_valid_id(id_str) -> int:
        
        id = None
        
        try:
            id = int(id_str)
        except ValueError:
            return None
        
        if id > 110000 or id < 1260000:
            return id
        
        return None
        
    
            