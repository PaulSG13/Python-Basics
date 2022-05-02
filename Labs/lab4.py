
import doctest


def compute_harmonic_series(n: int) -> float:

    """
    This function computes the sum of the harmonic series to the nth number.
    
    It takes an integer as an argument and computes the sum to the number n,
    returning the total sum as a floating-point number.
    
    Precondition: n >= 0
    
    EXAMPLE:
    
    >>> compute_harmonic_series(0)
    0.0
    
    >>> compute_harmonic_series(2)
    1.5
    
    >>> compute_harmonic_series(5)
    2.283333333333333
    
    >>> compute_harmonic_series(100)
    5.187377517639621
    
    """
    
    i = 1
    count = 0.0
    for i in range(1, n+1):
        count = count + 1/i 
    return count
      
     
def get_fibonacci_sequence(n: int) -> str:
   
    """
    This function takes an integer, n, as an argument and returns a string
    containing the first n values in the Fibonacci sequence seperated by commas.
    
    Precondition: n >= 0
    
    EXAMPLE:
    
    >>> get_fibonacci_sequence(1)
    '0'
    
    >>> get_fibonacci_sequence(3)
    '0,1,1'
    
    >>> get_fibonacci_sequence(0)
    ''
    
    >>> get_fibonacci_sequence(6)
    '0,1,1,2,3,5'
    
    >>> get_fibonacci_sequence(21)
    '0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765'
    
    
    """
    x = 0
    y = 1
    fib_series = '0,1'    
    
    if n == 0:
        return ''
    
    elif n == 1:
        return '0'
    
    if n > 2:
        for i in range(0, n-2):
            num = x + y
            fib_series = fib_series + ',' + str(num)
            x = y
            y = num
       
    return fib_series


def print_pattern(height: int, width: int, string1: str, string2: str) -> None:
    """
    This function takes 2 integers representing height and width and 2 strings
    representing characters to be printed as arguments.
    
    The function then prints a pattern, with the height denoting how many rows
    will be in the pattern and the width integer denoting how many times
    the two strings will be printed in each row. 
    
    Every second line the two strings will switch their order. 
    
    Precondition: height and width are both > 0
    
    EXAMPLE:
    
    >>> print_pattern(4, 3, '!@', '$$$')
    !@$$$!@$$$!@$$$
    $$$!@$$$!@$$$!@
    !@$$$!@$$$!@$$$
    $$$!@$$$!@$$$!@
    
    >>> print_pattern(1, 3, '!@', '$$$')
    !@$$$!@$$$!@$$$
    
    >>> print_pattern(2, 2, 'PG', '13')
    PG13PG13
    13PG13PG
    
    >>> print_pattern(1, 1, '!@', '$$$')
    !@$$$
    
    >>> print_pattern(11, 2, '!@', '$$$')
    !@$$$!@$$$
    $$$!@$$$!@
    !@$$$!@$$$
    $$$!@$$$!@
    !@$$$!@$$$
    $$$!@$$$!@
    !@$$$!@$$$
    $$$!@$$$!@
    !@$$$!@$$$
    $$$!@$$$!@
    !@$$$!@$$$
    >>> print_pattern(1, 1, '', '')
    
    >>> print_pattern(2, 2, '', '')
    <BLANKLINE>
    
    >>> print_pattern(3, 3, '', '')
    <BLANKLINE>
    <BLANKLINE>
    
    >>> print_pattern(1, 1, 'a', 'b')
    ab
    """
    
    
    pattern = string1 + string2
    
    for height in range(1, height+1):
        
        if height == 1:
            pass
        else:
            print()
            
        for width in range(1, width+1): 
            
            if height % 2 == 0:
                pattern = string2 + string1
                print(pattern, end='')
            else:
                pattern = string1 + string2
                print(pattern, end='')
            
    