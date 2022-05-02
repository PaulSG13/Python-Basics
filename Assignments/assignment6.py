import doctest
from typing import List


def sum_squares(loi: List[int]) -> int:
    """
    This function takes a list of integers as an argument. The function returns
    the sum of the square of all inteers in the list.
    
    EXAMPLE:
    
    >>> sum_squares([])
    0
    
    >>> sum_squares([7, 0, 1, 3])
    59
    
    >>> sum_squares([3, 3, 3])
    27
    
    >>> sum_squares([-3, -3, -3])
    27
    
    >>> sum_squares([1, 1, 1, 1, 1])
    5
    
    >>> sum_squares([0, 0, 0])
    0
    
    """
    sum_square = 0
    for num in loi:
        num = num * num
        sum_square = sum_square + num
        
    return sum_square


def doubled_list(loi: List[int]) -> List[int]:
    """
    This function takes a list of integers as an argument. The funtion creates
    and returns a new list that contains all of the elements in the original
    list with their values doubled. 
    
    EXAMPLE:
    
    >>> doubled_list([])
    []
    
    >>> doubled_list([1, 1, 1])
    [2, 2, 2]
    
    >>> doubled_list([7, 0, 1, 3])
    [14, 0, 2, 6]
    
    >>> doubled_list([-5, 5, 0])
    [-10, 10, 0]
    
    """
    new_list = []
    
    for num in loi:
        num = num*2
        new_list.append(num)
        
    return new_list
        
    
def count_multiples(loi: List[int], multiple: int) -> int:
    """
    This function takes a list of integers to search through and an integer
    to find the multiples of in the list as arguments. 
    
    The function calculates and returns the number of multiples of the given
    integer in the list. 
    
    EXAMPLE:
    
    >>> count_multiples([], 1)
    0
    
    >>> count_multiples([8, 9, 10, 12, 15], 2)
    3
    
    >>> count_multiples([3, 6, 9, 12], 3)
    4
    
    >>> count_multiples([2, 4, 8, 10], 3)
    0
    
    >>> count_multiples([0], 1)
    1
    
    """
    
    count = 0     
    
    for num in loi:
        if num % multiple == 0:
            count += 1
            
    return count


def sum_positive(loi: List[int]) -> int:
    """
    This function takes a list of integers as an argument and returns the sum 
    of all positive integers found in the list. 
    
    EXAMPLE:
    
    >>> sum_positive([])
    0
    
    >>> sum_positive([0, 0, 0])
    0
    
    >>> sum_positive([-1, -2, -3])
    0
    
    >>> sum_positive([1, 2, 3])
    6
    
    >>> sum_positive([7, 0, -6, 3, -4])
    10
    
    """
    
    sum_positives = 0
    
    for num in loi:
        if num > 0:
            sum_positives += num
            
    return sum_positives
    
    
def list_with_prefix(los: List[str], str_prefix: str) -> List[str]:
    """
    This function takes a list of strings to search through and a prefix string
    to add to the front of each word in the given list as arguments. 
    
    The function creates and returns a new list, where each element in the new
    list has had the prefix string added to the front of the string from the 
    original list.
    
    EXAMPLE:
    
    >>> list_with_prefix([], '')
    []
    
    >>> list_with_prefix([], 're')
    []
    
    >>> list_with_prefix(['fine', 'lay', 'spite', 'tail'], 'de')
    ['define', 'delay', 'despite', 'detail']
    
    >>> list_with_prefix(['do', 'done', 'cooked'], 'over')
    ['overdo', 'overdone', 'overcooked']
    
    >>> list_with_prefix(['fine', 'lay', 'spite', 'tail'], 're')
    ['refine', 'relay', 'respite', 'retail']
    
    >>> list_with_prefix(['fine', 'lay', 'spite', 'tail'], '')
    ['fine', 'lay', 'spite', 'tail']
    
    """
    
    new_list = []
    
    for words in los:
        new_word = str_prefix + words
        new_list.append(new_word)
        
    return new_list
    
    
def all_long_enough(los: List[str], min_str: int) -> bool:
    """
    This funcion takes a list of strings to search through and an integer 
    representing the minimum allowable string length as arguments. 
    
    The function determines if all of the strings in the list meet the minimum
    length requirement. 
    
    EXAMPLE:
    
    >>> all_long_enough([], 1)
    True
    
    >>> all_long_enough([''], 0)
    True
    
    >>> all_long_enough([''], 1)
    False
    
    >>> all_long_enough(['', 'dog', 'cat'], 1)
    False
    
    >>> all_long_enough(['', 'dog', 'cat'], 0)
    True
    
    >>> all_long_enough(['g'], 1)
    True
    
    >>> all_long_enough(['this', 'is', 'so', 'fun'], 2)
    True
    
    >>> all_long_enough(['this', 'is', 'so', 'fun'], 3)
    False
    
    """
    
    for word in los:
        if len(word) < min_str:
            return False
        
    return True


def growing_strings(los: List[str]) -> bool:
    """
    This function takes a list of strings as an argument and determines whether
    the strings are sorted in ascending order according to their length. 
    
    EXAMPLE:
    
    >>> growing_strings([])
    True
    
    >>> growing_strings(['small'])
    True
    
    >>> growing_strings(['big', 'small'])
    True
    
    >>> growing_strings(['small', 'big'])
    False
    
    >>> growing_strings(['tiny', 'same', 'small', 'bigger'])
    True
    
    >>> growing_strings(['big', 'bigger', 'biggest', 'huge'])
    False
    
    >>> growing_strings(['big', 'bigger', 'huge', 'biggest'])
    False
    
    >>> growing_strings(['huge', 'big', 'bigger', 'biggest'])
    False
    
    >>> growing_strings(['big', 'huge', 'bigger', 'biggest'])
    True
    
    """
    count = 0
    
    for word in los:
        if len(word) < count:
            return False
        count = len(word)
        
    return True
        
        