def print_my_info():
    """
    This function takes no arguments. It prints my name, favourite number 
    and age.
    It then divides my favourite number by my age and prints out the result.

    >>> print_my_info()
    My name is Paul.
    My favourite number is 21
    I am 25 years old.
    Here is some math: 21 / 25 is 0.84

    """
    name = 'Paul'
    fav_number = 21
    age = 25
    result = fav_number/age
    print('My name is', name + '.')
    print('My favourite number is', fav_number)
    print('I am', age, 'years old.')
    print('Here is some math:', fav_number, '/', age, 'is', result)


def print_sum(num1: float, num2: float):
    """
    This function takes two floating point numbers as arguments and prints 
    out their sum.

    >>> print_sum(5.0, 4.0)
    9.0

    >>> print_sum(30.0, 25.0)
    55.0
    
    """
    sum = num1 + num2
    print(sum)



