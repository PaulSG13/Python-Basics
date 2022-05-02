import doctest
from typing import List, Dict, Tuple

NAME_INDEX = 0
AGE_INDEX = 1
PROGRAM_INDEX = 2
GPA_INDEX = 3

# represents a student's academic standing as (name, gpa)
# where 0 <= gpa <= 9
StudentStanding = Tuple[str, float]
NAME = 0
GPA = 1


def get_people_of_age(age_dict: Dict[int, str], target_age: int) -> List[str]:
    """
    returns a list of the names of people found in the given dictionary
    who are target_age years old
    - Dict[age, list of names that age]
    >>> get_people_of_age({}, 22)
    []
    >>> get_people_of_age({29: ['Ali', 'Ty'], 19: ['Deep', 'Ted', 'Siu'], 22: ['Leif']}, 24)
    []
    >>> get_people_of_age({29: ['Ali', 'Ty'], 19: ['Deep', 'Ted', 'Siu'], 22: ['Leif']}, 22)
    ['Leif']
    >>> get_people_of_age({29: ['Ali', 'Ty'], 19: ['Deep', 'Ted', 'Siu'], 22: ['Leif']}, 19)
    ['Deep', 'Siu', 'Ted']
    """
   
    
    for age in age_dict:
        if age == target_age:
            age_dict[age].sort()
            return age_dict[age]
        
    return []  


def get_most_common_age(age_dict: Dict[int, str]) -> List[int]:
    """
    Determines the most common age (or ages) found in the given dictionary
    - Dict[age, list of names that age]
    >>> get_most_common_age({})
    []
    >>> get_most_common_age({29: ['Ali', 'Ty'], 19: ['Deep', 'Ted', 'Siu'], 22: ['Leif']})
    [19]
    >>> get_most_common_age({29: ['Ali', 'Ty'], 19: ['Deep', 'Ted']})
    [19, 29]
    """
    count = 0 
    
    list_common_ages = []
    
    for age in age_dict:
        if len(age_dict[age]) > count:
            count = len(age_dict[age])
        
        
    for age in age_dict:
        if len(age_dict[age]) == count:
            list_common_ages.append(age)
    
    list_common_ages.sort()
    
    return list_common_ages
    

def populate_dictionaries(filename: str) -> (Dict[int, str],
                                             Dict[str, str],
                                             Dict[str, float]):
    """
    populates and returns dictionaries based on data read from file
    - Dict[age, names that age]
    - Dict[program, names in program]
    - Dict[name, gpa]
    
    Precondition: each line in the file is formatted with name first, 
    followed by age, program, then gpa
    
    >>> populate_dictionaries('empty.csv')
    ({}, {}, {})
    >>> populate_dictionaries('student_data.csv')
    ({29: ['Ali', 'Ty', 'Erin', 'Sara', 'Rob'], 24: ['Yi', 'Paul', 'Juan', 'Luke', 'Lars', 'Mary', 'Toby', 'Omar'], 19: ['Deep', 'Ted', 'Soma', 'Siu', 'John'], 18: ['Sam', 'Tua', 'Niko', 'Luca', 'Inge'], 21: ['Ivan', 'Jose', 'Arav', 'Hans'], 22: ['Lee', 'Leif', 'Alia', 'Mia', 'Lina'], 26: ['Alex', 'Mika', 'Kwan', 'Sofi', 'Erik', 'Jane', 'Max'], 28: ['Mike', 'Leia', 'Kleo'], 27: ['Kai', 'Tina'], 20: ['May', 'Arya', 'Gigi'], 23: ['Toni'], 25: ['Matt', 'Veer']}, {'Geography': ['Ali', 'Sam', 'Lee', 'Leif', 'May', 'Luke', 'Matt', 'Sara', 'Toby', 'Inge', 'Max', 'Lina'], 'Economics': ['Yi', 'Ivan', 'Mike', 'Jose', 'Juan', 'Kwan', 'Soma', 'Lars', 'Alia', 'Erin', 'Mary', 'Siu', 'Leia', 'Veer', 'Luca', 'John', 'Hans', 'Omar'], 'Astronomy': ['Deep', 'Mika', 'Tua', 'Kai', 'Ted', 'Tina', 'Niko', 'Toni', 'Sofi', 'Arav', 'Erik', 'Rob', 'Jane', 'Gigi', 'Kleo'], 'Philosophy': ['Alex', 'Ty', 'Paul', 'Arya', 'Mia']}, {'Ali': 7.4, 'Yi': 6.8, 'Deep': 7.5, 'Sam': 6.9, 'Ivan': 8.5, 'Lee': 8.6, 'Alex': 8.5, 'Mike': 7.0, 'Mika': 6.5, 'Jose': 5.1, 'Tua': 5.4, 'Kai': 8.6, 'Ted': 8.8, 'Leif': 5.6, 'Ty': 5.0, 'Paul': 5.9, 'Juan': 5.4, 'Tina': 7.6, 'May': 5.9, 'Kwan': 7.2, 'Luke': 8.7, 'Soma': 6.2, 'Niko': 7.9, 'Lars': 8.3, 'Alia': 8.7, 'Erin': 6.3, 'Toni': 8.4, 'Matt': 5.2, 'Sofi': 7.3, 'Mary': 6.6, 'Siu': 8.4, 'Arya': 8.6, 'Sara': 8.5, 'Toby': 7.0, 'Arav': 5.5, 'Leia': 5.0, 'Veer': 7.8, 'Erik': 5.4, 'Luca': 5.8, 'Inge': 5.7, 'Rob': 5.1, 'Jane': 7.6, 'John': 5.9, 'Gigi': 5.5, 'Hans': 6.5, 'Mia': 6.4, 'Max': 5.7, 'Kleo': 8.6, 'Omar': 7.1, 'Lina': 6.2})
    
    # Now that populate_dictionaries is implemented,
    # you can use it with the functions you completed above
    >>> age_dict, program_dict, gpa_dict = populate_dictionaries('student_data.csv')
    >>> get_people_of_age(age_dict, 19)
    ['Deep', 'John', 'Siu', 'Soma', 'Ted']
    >>> get_most_common_age(age_dict)
    [24]
    """
    file_handle = open(filename, 'r') 
    
    
    ages_and_names = {}
    program_and_names = {}
    names_and_gpa = {}
    

    for line in file_handle:
        
        line = line.strip()
        
        items = line.split(',')
        
        names = items[NAME_INDEX]

        ages = int(items[AGE_INDEX])
        
        program = items[PROGRAM_INDEX]
        
        gpa = float(items[GPA_INDEX])
        
        if ages in ages_and_names:
            ages_and_names[ages].append(names)
            
        else:
            ages_and_names[ages] = []
            ages_and_names[ages].append(names)
       
        if program in program_and_names:
            program_and_names[program].append(names)
            
        else:
            program_and_names[program] = []
            program_and_names[program].append(names)
            
        names_and_gpa[names] = gpa
            
    file_handle.close()
    
    return ages_and_names, program_and_names, names_and_gpa
    
    



def get_with_program_and_age(filename: str, target_program:str, target_age: int) -> List[StudentStanding]:
    """
    creates a returns a list of StudentStanding tuples based on the people in 
    the file named filename who are in target_program with age target_age
    
    Precondition: each line in the file is formatted with name first, 
    followed by age, program, then gpa
    >>> get_with_program_and_age('empty.csv', 'Geography', 24)
    []
    
    >>> get_with_program_and_age('student_data.csv', 'Cryptography', 24)
    []
    
    >>> get_with_program_and_age('student_data.csv', 'Geography', 240)
    []
    
    >>> get_with_program_and_age('student_data.csv', 'Geography', 24)
    [('Luke', 8.7), ('Toby', 7.0)]
    
    >>> get_with_program_and_age('student_data.csv', 'Economics', 21)
    [('Hans', 6.5), ('Ivan', 8.5), ('Jose', 5.1)]
    """
   
    list_of_names = []
    
    list_name_gpa = []
    
    age_dict, program_dict, gpa_dict = populate_dictionaries(filename)
    
    people_of_age = get_people_of_age(age_dict, target_age)
    
    for program in program_dict:
        if target_program == program:
            for names in program_dict[program]:
                if names in people_of_age:
                    list_of_names.append(names)
                   
    
    for names in list_of_names:
        if names in gpa_dict:
            name_gpa = names, gpa_dict[names]
            list_name_gpa.append(name_gpa)
    
    list_name_gpa.sort()
    
           
    return list_name_gpa
                        
                    



def avg_gpa_in_program_and_age(filename: str, target_program:str, target_age: int) -> float:
    """
    calculate and return the average gpa of all students in the file
    who are in target_program with age target_age
    
    Precondition: each line in the file is formatted with name first, 
    followed by age, program, then gpa
    
    >>> avg_gpa_in_program_and_age('empty.csv', 'Geography', 24)
    0
    
    >>> avg_gpa_in_program_and_age('student_data.csv', 'Space-Talk', 24)
    0
    
    >>> avg_gpa_in_program_and_age('empty.csv', 'Geography', 240)
    0

    >>> avg_gpa_in_program_and_age('student_data.csv', 'Geography', 24)
    7.85
    >>> avg_gpa_in_program_and_age('student_data.csv', 'Economics', 21)
    6.7
    """
    
    
    names_and_programs = get_with_program_and_age(filename, target_program, target_age)
    
    gpa_average = 0
    
    count = 0
    
    for student in names_and_programs:
        count+= 1
        gpa_average += student[GPA]
        
    if count == 0:
        return 0
    
    gpa_average = gpa_average/count    
        
    return gpa_average