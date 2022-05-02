import doctest
from typing import List


def sum_even_values(loi: List[int]) -> int:
    """
    This function takes a list of integers as an arguement. The function then
    calculates and returns the sum of only the even values in the given list. 
    
    EXAMPLE:
    
    >>> sum_even_values([])
    0
    >>> sum_even_values([12, 4, 3, -2])
    14
    
    >>> sum_even_values([-1, -2, -3, -4, -5])
    -6
    
    >>> sum_even_values([2, 4, 6, 8])
    20
    
    >>> sum_even_values([1, 3, 5, 7, 9])
    0
    
    """
    sum_of_ints = 0
    
    for num in loi:
        if num % 2 == 0:
            sum_of_ints += num
            
    return sum_of_ints


def count_above(lon: List[float], thresh_num: float) -> int:
    """
    This function takes a list of numbers and a threshold value as arguements.
    
    The funtion then counts the number of values that are above the threshold
    and returns the count as an integer. 
    
    EXAMPLE:
    
    >>> count_above([], 1)
    0
    
    >>> count_above([1, 2, 3], 4)
    0
    
    >>> count_above([1, 2, 3], 3)
    0
    
    >>> count_above([1, 2, 3], 2)
    1
    
    >>> count_above([1, 2, 3], 1)
    2
    
    >>> count_above([1, 2, 3], 0)
    3
    
    >>> count_above([1.1, 2.2, 3.3], 0)
    3
    
    >>> count_above([1.1, 2.2, 3.3], 1.1)
    2
    
    >>> count_above([1.1, 2.2, 3.3], 2.2)
    1
    
    >>> count_above([1.1, 2.2, 3.3], 3.2)
    1
    
    >>> count_above([1.1, 2.2, 3.3], 3.3)
    0
    
    >>> count_above([1.1, 2.2, 3.3], 3.4)
    0
    
    
    """
    count = 0
    
    for num in lon:
        if num > thresh_num:
            count += 1
            
    return count
            
    
def add1(loi: List[int]) -> List[int]:
    """
    This takes a list of integers as an argument, it then creates a new list
    with every value in the list passed with 1 added to it.
    
    EXAMPLE:
    
    >>> add1([])
    []
    
    >>> add1([1])
    [2]
    
    >>> add1([1, 2, 3, 4, 5])
    [2, 3, 4, 5, 6]
    
    >>> add1([-1, -2, -3, -4])
    [0, -1, -2, -3]
    
    """
    
    new_list = []
    
    for num in loi:
        num += 1
        new_list.append(num)
        
    return new_list


def are_all_even(loi: List[int]) -> bool:
    """
    This function takes a list of integers as an argument and determines whether
    all of the elements in the list are even. 
    
    EXAMPLE:
    
    >>> are_all_even([])
    True
    
    >>> are_all_even([2, 4, 6, 8])
    True
    
    >>> are_all_even([2, 4, 6, 8, 9])
    False
    
    >>> are_all_even([1, 3, 5, 7])
    False
    """
    
    for num in loi:
        if num % 2 != 0:
            return False
        
    return True
            
    