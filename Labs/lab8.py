import doctest
from typing import List, Tuple 

# represents a person's information as
# (name, age) where age is string representing a whole number 

Person = Tuple[str, str]

NAME = 0
AGE = 1 


def file_to_person_list(filename: str) -> List[Person]:
    """
    This function takes a name of a file as an argument. It reads the lines
    of text from the file that contains on each line a person's name and age as
    a whole number seperated by a space. The function creates and returns a list 
    of tuples, where each tuple contains a person's name and age as described 
    in the Person type alias. 
    
    EXAMPLE:
    
    >>> file_person_list('lab8-name-age.txt')
    [('Lynden', '6'), ('Tian', '27'), ('Daljit', '18'), ('Jose', '53'), ('Jingwen', '17'), ('Rajan', '65')]
    
    """
    
    file_handle = open(filename, 'r')
    
    list_people_info = []
    
    for line in file_handle:
        line = line.rstrip('\n')
        contents = line.split(' ') 
        contents = tuple(contents)
        list_people_info.append(contents)
        
    file_handle.close()
    
    return list_people_info
        
        
def get_average_age(people: List[Person]) -> int:
    """
    This function takes a list of person information tuples and calculates and
    returns the avaerage of all ages in the list as a whole number rounded down.
    
    Precondition: List of tuples is not empty.
    
    EXAMPLE:
    
    >>> get_average_age([('Jose', '53'), ('Rajan', '65'), ('DudeMan', '66')])
    61
    
    >>> get_average_age([('Jose', '53'), ('Rajan', '65')])
    59
    
    """
    
    count = 0
    age = 0
    
    for person in people:
        
        age += int(person[AGE])
        count+=1
        
    average_age = int(age/count)
    
    return average_age
        
        
def get_above_age(people: List[Person], threshold: int) -> List[Person]:
    """
    This function takes a list of person information tuples and a threshold age.
    The function creates and returns a list of person information tuples
    that have an age older than the threshold age. 
    
    >>> get_above_age([], 52)
    []

    >>> get_above_age([('Jose', '53'), ('Rajan', '65')], 64)
    [('Rajan', '65')]
    
    >>> get_above_age([('Jose', '53'), ('Rajan', '65')], 52)
    [('Jose', '53'), ('Rajan', '65')]
    
    """
    people_above_age = []
    
    for person in people:
        if int(person[AGE]) > threshold:
            people_above_age.append(person)
        
    return people_above_age


def to_file(people: List[Person], filename: str) -> None:
    """
    This function takes a list of person information tuples and the name of a
    file as arguments and writes the name and age from each tuple on its own
    line with the name and age sperated by commas. 
    
    >>> to_file([('Jose', '53'), ('Rajan', '65')], 'sample.txt')
    """
    
    file_handle = open(filename, 'w') 
    
    for person in people:
        file_handle.write(person[NAME] + ',' + person[AGE] + '\n')
        
    file_handle.close()
    
    
def write_names_above_avg_age(input_file_name: str, output_file_name: str) -> None:
    """
    This function takes the name of an input file and the name of an output file
    as arguments. 
    
    The function reads all the names and ages from the input file
    and writes to the output file those names and ages above the average of all
    ages of people in the input file. 
    
    The function calls functions previous written in this file as helpers. 
    
    Precondition: The input file contains on each line a person's name and age
    as a whole number seperated by a space. 
    
    EXAMPLE:
    
    >>> write_names_above_avg_age('lab8-name-age.txt', 'sample.txt')
    """
    

    people_info = file_to_person_list(input_file_name)
    
    average_age_people = get_average_age(people_info)
    
    people_above_average = get_above_age(people_info, average_age_people)
      
    file_people_above_avg_age = to_file(people_above_average, output_file_name)
    
    