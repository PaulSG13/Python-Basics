import doctest
from typing import List

def find_longest(los: List[str]) -> str:
    """
    returns the longest string found in the given list of strings.
    If two strings have the same length, the one that was found
    first in the list (closest to the front) is returned
    >>> find_longest([])
    ''
    >>> find_longest(['AT'])
    'AT'
    >>> find_longest(['AT', 'CGA', 'TGAC', 'TGACC'])
    'TGACC'
    >>> find_longest(['GTCCA', 'ACTG', 'GAC', 'AT'])
    'GTCCA'
    >>> find_longest(['CA', 'TGCA', 'TCA', 'GTAC'])
    'TGCA'
    """
    # TODO: Complete this method
    
    if len(los) == 0:
        return ''
    
    longest_length = 0
    
    for index in range(len(los)):
        if len(los[index]) > longest_length:
            longest_length = len(los[index])
            
    for nucleic_acid in los:
        if len(nucleic_acid) == longest_length:
            return nucleic_acid
        
    
    # Is this possible?
    
    """
    longest_string = max(los, key=len)
    
    return longest_string
            
    """
    


def get_frequency(los: List[str], to_find: str) -> int:
    """
    returns a count of the number of times to_find is found
    in the given list of strings
    >>> get_frequency([], 'AC')
    0
    >>> get_frequency(['AC', 'TAC', 'GAC', 'AC', 'GTAC'], 'AC')
    2
    >>> get_frequency(['ACTG', 'TGA', 'TTGA', 'TGGGGA', 'TGAC'], 'TGA')
    1
    >>> get_frequency(['GA', 'AAG', 'AGG', 'AGT', 'CAG'], 'AG')
    0
    >>> get_frequency(['AG', 'GA', 'AAG', 'AGG', 'AGT', 'AG', 'AG'], 'AG')
    3
    """
    # TODO: Complete this method
    
    count = 0
    
    for nucleic_acid in los:
        if to_find == nucleic_acid:
            count+= 1
                
    return count
    


def is_mutation(sequence: str) -> bool:
    """
    returns true if the given sequence contains a mutation. Any string with
    at least two of the same character in a row is considered a mutation.
    Returns True if the given string is a mutation, false otherwise.
    
    Precondition: len(sequence) >= 2 and any duplicate characters in the 
    given string will appear right beside one another.
    >>> is_mutation('ACTG')
    False
    >>> is_mutation('ACTGG')
    True
    >>> is_mutation('AACTG')
    True
    >>> is_mutation('ACCCCCTG')
    True
    >>> is_mutation('GA')
    False
    """
    # TODO: Complete this method
    
    for index in range(len(sequence)):
        if sequence[index] == sequence[index-1]:
            return True
        
    return False



def break_mutation(sequence: str) -> str:
    """
    returns a string with all duplicate letters removed from sequence
    
    Any sequence with at least two of the same base in a row is 
    considered a mutation.
    
    Precondition: Any duplicate characters in the given string will
    appear right beside one another.
    >>> break_mutation('GTAC')
    'GTAC'
    >>> break_mutation('GGGTAC')
    'GTAC'
    >>> break_mutation('CGATTT')
    'CGAT'
    >>> break_mutation('AAAACC')
    'AC'
    >>> break_mutation('TTTTTTTTTTAAGGGGGGG')
    'TAG'
    """
    # TODO: Complete this method
    non_mutated_sequence = ''
    
    if not is_mutation(sequence):
        return sequence
    
    if is_mutation(sequence):
        for index in range(len(sequence)):
            if sequence[index] != sequence[index-1]:
                non_mutated_sequence += sequence[index]
                
    return non_mutated_sequence
            


def count_total_mutations(los: List[str]) -> int:
    """ 
    returns a count of the total number of strings in the given 
    list of strings that contain a mutation
    
    Any string with at least two of the same character in a row is 
    considered a mutation.
    
    Precondition: All strings have a length >= 2 and any duplicate characters 
    in a string will appear right beside one another.
    >>> count_total_mutations(['AC', 'CGT', 'TCA', 'ATG', 'GTAC', 'GA'])
    0
    >>> count_total_mutations(['ACTG', 'TGA', 'TTGA', 'TGGGGGAA', 'TGAC'])
    2
    >>> count_total_mutations(['CCAAAATT', 'GGGTT', 'AAAATTGGGCCCC',\
    'GGGTT', 'GTA'])
    4
    """
    # TODO: Complete this method
    
    count = 0
    
    for sequence in los:
        if is_mutation(sequence):
            count += 1
            
    return count



def frequency_incl_mutations(los: List[str], to_find) -> int:
    """
    returns a count of the number of times to_find and mutations of 
    to_find are found in the given list of strings
    
    Any string with at least two of the same character in a row is 
    considered a mutation.
    
    Preconditions: All strings contain at least two characters, 
    All strings contain only characters A, C, T, or G
    Any duplicate letters within a string are beside one another
    
    >>> frequency_incl_mutations(['AC', 'TAC', 'ACG', 'AC', 'GTAC'], 'TA')
    0
    >>> frequency_incl_mutations(['AC', 'TAC', 'ACG', 'AC', 'GTAC'], 'AC')
    2
    >>> frequency_incl_mutations(['TGA', 'TTGA', 'TGGGGAA', 'TGAA'], 'TGA')
    4
    >>> frequency_incl_mutations(['TGAC', 'TGA', 'TTGA', 'TGGGGGAA',\
    'CTGA', 'TGAA'], 'TGA')
    4
    """
    # TODO: Complete this method 
    
    # use count_total_mutations and get_frequency functions
    
    count = 0
    
    count += count_total_mutations(los)
    
    count += get_frequency(los, to_find)
        
    return count


def create_list_from_file(file_name: str) -> List[str]:
    """
    create and return a new list containing all of the strings found
    in the file. 
    
    Precondition: there is a file with the given file_name in the same
    folder as this python file. All strings in file are all separated by a space
    >>> create_list_from_file('data0.txt')
    []
    >>> create_list_from_file('data1.txt')
    ['AC', 'TAC', 'GAC', 'AC', 'GTAC']
    """
    # TODO: Complete this method