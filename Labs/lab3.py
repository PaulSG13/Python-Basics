import doctest

GST = 0.05

PST = 0.10

def get_longer(phrase1: str, phrase2: str) -> str:
    """
    This function takes two strings as arugments. It returns the longer string
    of the two. 
    
    If both strings are equal in length, only the first string 
    passed will be returned.
    
    EXAMPLE:
    
    >>> get_longer('Cairo', 'Cairo is in Egypt')
    'Cairo is in Egypt'
    
    >>> get_longer('Hello World!', 'hi')
    'Hello World!'
    
    >>> get_longer('Cairo', 'Hello')
    'Cairo'
    
    >>> get_longer('', 'dog')
    'dog'
    
    >>> get_longer('', '')
    ''
    
    """
    if len(phrase2) > len(phrase1):
        return phrase2
    else:
        return phrase1
    
    
def get_tax(food_cost: float, alcohol_cost: float) -> float:
    """
    This function calculates and returns the tax owed on food and alcohol
    purchases.
    
    It takes two floating-point numbers as arguments and returns a 
    floating-point number. 
    
    Precondition: Amount of money owed for food >= 0 and alcohol >= 0
    
    EXAMPLE:
    
    >>> get_tax(28.75, 45.98)
    8.3345
    
    >>> get_tax(30, 45)
    8.25
    
    >>> get_tax(12.6, 5.5)
    1.455
    
    >>> get_tax(33.50, 0)
    1.675
    
    >>> get_tax(0, 11.11)
    1.6665
    
    >>> get_tax(0, 0)
    0.0
    
    """
    food_tax = food_cost * GST 
    
    alcohol_tax = alcohol_cost * GST + alcohol_cost * PST
    
    return food_tax + alcohol_tax

def get_bill_share(food_cost: float, alcohol_cost: float, 
                   num_people: int) -> float:
    """
    This function calclates and returns the amount each person in a group
    owes for food and alcohol, including tax, divided equally among them. 
    
    Precondition: food_cost and alcohol_cost >= 0 and num_people >= 1
    
    EXAMPLE:
    
    >>> get_bill_share(18.93, 0, 2)
    9.93825
    
    >>> get_bill_share(12.6, 5.5, 1)
    19.555
    
    >>> get_bill_share(33, 12, 4)
    12.1125
    
    >>> get_bill_share(0, 2458.50, 10)
    282.7275
    
    """
    
    tax = get_tax(food_cost, alcohol_cost)
    
    total_bill = food_cost + alcohol_cost + tax
    
    return total_bill/num_people

    