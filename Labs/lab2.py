import math, doctest

def print_longer(sentence1: str, sentence2: str):
    """
    This function takes two strings as arugments. It prints the longer string
    of the two. If both strings are equal in length, only the first string 
    passed will be printed.
    
    EXAMPLE:
    
    >>> print_longer('Cairo', 'Cairo is in Egypt')
    Cairo is in Egypt
    
    >>> print_longer('Hello World!', 'hi')
    Hello World!
    
    >>> print_longer('Cairo', 'Hello')
    Cairo
    
    >>> print_longer('', 'dog')
    dog
    
    >>> print_longer('', '')
    <BLANKLINE>
    """
    
    if len(sentence2) > len(sentence1):
        print(sentence2)
    else:
        print(sentence1)



def print_real_roots(a: float, b: float, c: float):
   
    """
    This function takes three floating-point numbers as arguments.
    
    Each argument denotes a constant variable in the quadratic equation:
    
    ax^2 + bx + c = 0
    
    The function then calculates and prints the real root(s) from that equation.
    
    If there are no real roots the function will print NO REAL ROOTS
    
    If a = 0 this function will print an error message.
    
    EXAMPLE:
    
    >>> print_real_roots(1, 2, 1)
    -1.000
    
    >>> print_real_roots(1, 0, -16)
    4.000 , -4.000
    
    >>> print_real_roots(3, 4, 5)
    NO REAL ROOTS
    
    >>> print_real_roots(0, 4, 7)
    ERROR
    
    """

    discriminant = b**2 - 4*a*c 

    if a == 0:
        print('ERROR')
    elif discriminant > 0:
        root1 = (((-b) + math.sqrt(discriminant))/(2*a))
        root2 = (((-b) - math.sqrt(discriminant))/(2*a))
        print(format(root1, '.3f'), ',', format(root2, '.3f'))
    elif discriminant == 0:
        root = (-b) / 2*a 
        print(format(root, '.3f'))
    else:
        print('NO REAL ROOTS')
    

def print_zodiac_sign(month: str, day: int):
    """
    This function takes two arguments, one for a month of the year as a string
    and the other for a day in the month as an integer.
    
    The function then prints the name of the zodiac sign associated with that
    date.
    
    Precondition: month and day must be valid dates.
    
    EXAMPLE:
    
    >>> print_zodiac_sign('January', 19)
    Capricorn
    
    >>> print_zodiac_sign('January', 20)
    Aquarius
    
    >>> print_zodiac_sign('February', 18)
    Aquarius
    
    >>> print_zodiac_sign('February', 19)
    Pisces
    
    >>> print_zodiac_sign('March', 20)
    Pisces
    
    >>> print_zodiac_sign('March', 21)
    Aries
    
    >>> print_zodiac_sign('April', 19)
    Aries
    
    >>> print_zodiac_sign('April', 20)
    Taurus
    
    >>> print_zodiac_sign('May', 20)
    Taurus
    
    >>> print_zodiac_sign('May', 21)
    Gemini
    
    >>> print_zodiac_sign('June', 20)
    Gemini
    
    >>> print_zodiac_sign('June', 21)
    Cancer
    
    >>> print_zodiac_sign('July', 22)
    Cancer
    
    >>> print_zodiac_sign('July', 23)
    Leo
    
    >>> print_zodiac_sign('August', 22)
    Leo
    
    >>> print_zodiac_sign('August', 23)
    Virgo
    
    >>> print_zodiac_sign('September', 22)
    Virgo
    
    >>> print_zodiac_sign('September', 23)
    Libra
    
    >>> print_zodiac_sign('October', 22)
    Libra
    
    >>> print_zodiac_sign('October', 23)
    Scorpio
    
    >>> print_zodiac_sign('November', 21)
    Scorpio
    
    >>> print_zodiac_sign('November', 22)
    Sagittarius
    
    >>> print_zodiac_sign('December', 21)
    Sagittarius
    
    >>> print_zodiac_sign('December', 22)
    Capricorn
    
    """
    
    if month == 'January':
        if day < 20:
            zodiac_sign = 'Capricorn'
        else:
            zodiac_sign = 'Aquarius'
            
    elif month == 'February':
        if day < 19:
            zodiac_sign = 'Aquarius'
        else:
            zodiac_sign = 'Pisces'
            
    elif month == 'March':
        if day < 21:
            zodiac_sign = 'Pisces'
        else:
            zodiac_sign = 'Aries'
    
    elif month == 'April':
        if day < 20:
            zodiac_sign = 'Aries'
        else:
            zodiac_sign = 'Taurus'
            
    elif month == 'May':
        if day < 21:
            zodiac_sign = 'Taurus'
        else:
            zodiac_sign = 'Gemini'
            
    elif month == 'June':
        if day < 21:
            zodiac_sign = 'Gemini'
        else:
            zodiac_sign = 'Cancer'
        
    elif month == 'July':
        if day < 23:
            zodiac_sign = 'Cancer'
        else:
            zodiac_sign = 'Leo'
            
    elif month == 'August':
        if day < 23:
            zodiac_sign = 'Leo'
        else:
            zodiac_sign = 'Virgo'
            
    elif month == 'September':
        if day < 23:
            zodiac_sign = 'Virgo'
        else:
            zodiac_sign = 'Libra'
            
    elif month =='October':
        if day < 23:
            zodiac_sign = 'Libra'
        else:
            zodiac_sign = 'Scorpio'
            
    elif month == 'November':
        if day < 22:
            zodiac_sign = 'Scorpio'
        else:
            zodiac_sign = 'Sagittarius'
            
    elif month == 'December':
        if day < 22:
            zodiac_sign = 'Sagittarius'
        else:
            zodiac_sign = 'Capricorn'
        
    print(zodiac_sign)
    
    