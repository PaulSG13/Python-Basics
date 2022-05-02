import doctest

def is_factor(n1: int, n2: int) -> bool:
    """
    returns true if n1 is a factor of n2, false otherwise
    Preconditions: n1 > 0
    
    >>> is_factor(3, 9)
    True
    
    >>> is_factor(9, 3)
    False
    
    >>> is_factor(3, 10)
    False
    
    >>> is_factor(6, 12)
    True
    
    >>> is_factor(6, 13)
    False
    
    >>> is_factor(7, 7)
    True
    
    """
    return (n2 % n1 == 0)

def num_factors(n: int) -> int:
    """
    This function takes an integer as an argument and returns the number of
    factors of the integer.
    
    Precondition: The integer passed as an arguement is greater than 0
    
    EXAMPLE:
    
    >>> num_factors(12)
    6
    
    >>> num_factors(10)
    4
    
    >>> num_factors(20)
    6
    
    >>> num_factors(1)
    1
    
    >>> num_factors(5)
    2
    
    >>> num_factors(100)
    9
    
    """
    
    count = 0
    
    for num in range(1, n+1):
        
        if is_factor(num, n) == True:
            count += 1
            
    return count

       
def is_prime(n: int) -> bool:
    """
    This function takes an integer as an argument and determines whether 
    or not it is a prime number.
    
    The function assumes a prime number is a positive integer that only has 2 
    factors, 1 and itself.
    
    The function calls the num_factors function previously defined in this
    file.
    
    Precondition: The integer passed as an argument is greater than 
    or equal to 2.
    
    EXAMPLE:
    
    >>> is_prime(7)
    True
    
    >>> is_prime(2)
    True
    
    >>> is_prime(10)
    False
    
    >>> is_prime(100)
    False
    
    >>> is_prime(47)
    True
    
    >>> is_prime(97)
    True
    
    """
    
    if num_factors(n) == 2:
        return True
    
    else:
        return False
    
    
def count_primes_in_range(min_range: int, max_range: int) -> int:
    """
    This function calculates and returns the number of prime numbers found in
    the range starting at the integer min_range, going up to and including 
    the integer max_range.
    
    Preconditions: The first integer argument is greater than or equal to 2,
    the second integer argument is greater than or equal to the first argument.
    
    EXAMPLE:
    
    >>> count_primes_in_range(7, 13)
    3
    
    >>> count_primes_in_range(2, 100)
    25
    
    >>> count_primes_in_range(3, 10)
    3
    
    >>> count_primes_in_range(2, 2)
    1
    
    >>> count_primes_in_range(13, 13)
    1
    
    """
    
    count = 0
    
    for num in range(min_range, max_range+1):
        
        if num_factors(num) == 2:
            count += 1
            
    return count


def print_multiples(num1: int, num2: int) -> None:
    """
    This function takes two integers as arguments. It prints the multiples of
    the first integer and determines how many multiples to print by the 
    value of the second integer.
    
    Precondition: Both integers arguments are greater than or equal to 1.
    
    EXAMPLE:
    
    >>> print_multiples(5, 10)
       5   10   15   20   25   30   35   40   45   50 
       
    >>> print_multiples(452, 8)
     452  904 1356 1808 2260 2712 3164 3616 
     
    >>> print_multiples(1, 10)
       1    2    3    4    5    6    7    8    9   10 
       
    >>> print_multiples(10, 1)
      10 
      
    >>> print_multiples(25, 2)
      25   50 
      
    """
    
    for num in range(num1, num1*num2+1):
        
        if is_factor(num1, num) == True:
            
            print(format(num, '4d'), end=' ')
            
            
def print_multiplication_table(width: int, height: int) -> None:
    """
    This function takes two integer arguments denoting the width and height of 
    a multiplication table. 
    
    The function then prints out a multiplication table with integers 
    width by height dimensions.
    
    The function calls the print_multiples function.
    
    Precondition: Both integer arguments are greater than or equal to 1. 
    
    EXAMPLE:
    
    >>> print_multiplication_table(8, 3)
       1    2    3    4    5    6    7    8 
       2    4    6    8   10   12   14   16 
       3    6    9   12   15   18   21   24 
       
    >>> print_multiplication_table(4, 6)
       1    2    3    4 
       2    4    6    8 
       3    6    9   12 
       4    8   12   16 
       5   10   15   20 
       6   12   18   24 
       
    >>> print_multiplication_table(1, 1)
       1 
    
    >>> print_multiplication_table(1, 10)
       1 
       2 
       3 
       4 
       5 
       6 
       7 
       8 
       9 
      10 
       
    >>> print_multiplication_table(10, 1)
       1    2    3    4    5    6    7    8    9   10 

    """
    
    for height_table in range(1, height+1):
        
        if height_table == 1:
            pass
        else:
            print()
            
        for width_table in range(1, 2):
            
            print_multiples(width_table*height_table, width)
            
            