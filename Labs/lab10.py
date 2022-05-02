import doctest
from typing import List, Tuple
from student import Student 



def main() -> None:
    
    stdnt = Student('V00803658', 99)
    print(stdnt)
    

def get_students(filename: str) -> List[Student]:
    """
    This function takes a name of a file as an arguement. The function then 
    creates and returns a new list of Students from filename where each line
    of file has a student id and grade separated by a comma.
    If the file is empty the function returns an empty list.
    
    EXAMPLE:
    
    >>> get_students('empty.csv')
    []
    >>> get_students('student_data.csv')
    [Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)]
    """
    
    list1 = []
    
    file_handle = open(filename, 'r')
    
    for line in file_handle:
        line = line.strip()
        contents = line.split(',')
        for items in contents:
            if items.isdigit():
                items = int(items)
            else:
                ids = items
        list1.append(Student(ids, items))
        
    file_handle.close()
    
    return list1

def get_classlist(students: List[Student]) -> List[str]:
    """
    This function takes a list of Student instances and creates 
    and returns a new list of just the student ids of all Student instances in the list.
    >>> stdnt1 = Student('V00123456', 89)
    >>> stdnt2 = Student('V00123457', 99)
    >>> stdnt3 = Student('V00123458', 30)
    >>> stdnt4 = Student('V00123459', 78)
    >>> get_classlist([stdnt1, stdnt2, stdnt3, stdnt4])
    ['V00123456', 'V00123457', 'V00123458', 'V00123459']
    >>> get_classlist([])
    []
    """
    list1 = []
    
    for student in students:
        list1.append(student.get_sid())
    return list1
    
    
def count_above(lostudents: List[Student], threshold: int) -> int:
    """
    Takes a list of Student instances and an additional argument as a threshold
    grade. The function returns a count of the number of Student instances in
    the list that have a grade above the given threshold grade.
    
    Precondition: Threshold grade is a positive integer.
    
    EXAMPLE:
    
    >>> stdnt1 = Student('V00123456', 89)
    >>> stdnt2 = Student('V00123457', 99)
    >>> stdnt3 = Student('V00123458', 30)
    >>> stdnt4 = Student('V00123459', 78)
    >>> count_above([stdnt1, stdnt2, stdnt3, stdnt4], 100)
    0
    >>> count_above([stdnt1, stdnt2, stdnt3, stdnt4], 98)
    1
    >>> count_above([stdnt1, stdnt2, stdnt3, stdnt4], 88)
    2
    >>> count_above([stdnt1, stdnt2, stdnt3, stdnt4], 77)
    3
    >>> count_above([stdnt1, stdnt2, stdnt3, stdnt4], 29)
    4
    >>> count_above([stdnt1, stdnt2, stdnt3, stdnt4], 99)
    0
    >>> count_above([stdnt1, stdnt2, stdnt3, stdnt4], 89)
    1
    >>> count_above([stdnt1, stdnt2, stdnt3, stdnt4], 78)
    2
    >>> count_above([stdnt1, stdnt2, stdnt3, stdnt4], 30)
    3
    """
    
    list1 = []
    
    count = 0
    
    for student in lostudents:
        list1.append(student.get_grade())
        
    for grades in list1:
        if grades > threshold:
            count += 1
            
    return count

def get_average_grade(lostudents: List[Student]) -> float:
    """
    Takes a list of Student instances. The function calculates and returns the
    average grade of all Student instances in the list as a floating point 
    number. 
    
    Precondition: The list of Student instances in not empty.
    
    EXAMPLE:
    
    >>> stdnt1 = Student('V00123456', 89)
    >>> stdnt2 = Student('V00123457', 99)
    >>> stdnt3 = Student('V00123458', 30)
    >>> stdnt4 = Student('V00123459', 78)
    >>> get_average_grade([stdnt1, stdnt2, stdnt3, stdnt4])
    74.0
    >>> get_average_grade([stdnt1, stdnt2, stdnt3])
    72.66666666666667
    >>> get_average_grade([stdnt1, stdnt2])
    94.0
    >>> get_average_grade([stdnt1])
    89.0
    """
    list1 = []
    
    average = 0
    
    for student in lostudents:
        list1.append(student.get_grade())
    
    for grades in list1:
        average += grades
        
    average = average/len(list1)
    
    return average

if __name__ == '__main__':
    # the code in here will run if you run this program directly
    # the code in here will NOT run if someone imports this module    
    main()
