import doctest

TIER_1_DENTAL_COST_UNDER_250 = 0

TIER_2_DENTAL_COST_UNDER_250 = 10

TIER_3_DENTAL_COST_UNDER_250 = 25

TIER_1_DENTAL_COVERAGE_250_TO_500 = 400

TIER_2_DENTAL_COVERAGE_250_TO_500 = 300

TIER_3_DENTAL_COVERAGE_250_TO_500 = 200

TIER_1_DENTAL_COVERAGE_OVER_500 = 0.75

TIER_2_DENTAL_COVERAGE_OVER_500 = 0.60

TIER_3_DENTAL_COVERAGE_OVER_500 = 0.40

def print_speeding_results(current_speed: int, speed_limit: int):
    """
    This function determines if the speed of a vehicle is greater than the
    speed limit.
    
    If the vehicle speed is greater than the speed limit, it prints a 
    warning message along with how many km/hr over the speed limit.
    
    If the vehicle speed is below or equal to the speed limit, it prints the 
    vehicle speed in km/hr as well as the current speed limit.
    
    Precondition: both the speed of the vehicle and the speed limit >= 0.
    
    EXAMPLE:
    
    >>> print_speeding_results(50, 100)
    Current speed: 50km/hr, limit: 100km/hr
    
    >>> print_speeding_results(91, 80)
    Speeding! 11km/hr over the speed limit
    
    >>> print_speeding_results(120, 120)
    Current speed: 120km/hr, limit: 120km/hr
    
    
    """
    if current_speed > speed_limit:
        above_limit = current_speed - speed_limit
        print('Speeding! ', above_limit,  'km/hr over the speed limit', sep='')
    else:
        print('Current speed: ', current_speed, 'km/hr,', sep='', end='')
        print(' limit: ', speed_limit, 'km/hr', sep='')


def print_area(length: float, width: float):
    """
    This function takes two floating-point arguments as the length and width of
    a rectangle.
    
    The function then prints the area of the rectangle in cm^2 and rounded 
    to two decimals places.
    
    Precondition: both length and width are >= 0.
    
    EXAMPLE:
    
    >>> print_area(1.1, 1.12)
    The area of the rectangle is 1.23cm^2
    
    >>> print_area(323, 235)
    The area of the rectangle is 75905.00cm^2
    
    """
    area = length * width
    print('The area of the rectangle is ', format(area, '.2f'), 'cm^2', sep='')


def print_average(num1: float, num2: float, num3: float):
    """
    This function takes three floating-point numbers as arguments and prints
    their average rounded to one decimal place. 
    
    EXAMPLE:
    
    >>> print_average(10, 15, 20)
    The average of the three numbers is 15.0
    
    >>> print_average(23, 56, 75)
    The average of the three numbers is 51.3
    
    >>> print_average(26.6, 32.33, 101.1)
    The average of the three numbers is 53.3
    
    >>> print_average(-51, 0, 35)
    The average of the three numbers is -5.3
    
    """
    average = (num1 + num2 + num3)/3
    print('The average of the three numbers is', format(average, '.1f'))


def print_is_factor(n1: int, n2: int):
    """
    This function takes two integers as arguments and determines whether 
    the first integer is a factor of the second integer.
    
    Precondition: n1 > 0 
    
    EXAMPLE:
    
    >>> print_is_factor(8, 64)
    8 is a factor of 64
    
    >>> print_is_factor(12, 35)
    12 is not a factor of 35
    
    >>> print_is_factor(23, 23)
    23 is a factor of 23
    
    >>> print_is_factor(8, 0)
    8 is a factor of 0
    
    """
    if n2 % n1 == 0:
        print(n1, 'is a factor of', n2)
    else:
        print(n1, 'is not a factor of', n2)
        
def print_cost_after_coverage(coverage_tier: int, dental_bill: float):
    """
    This function prints the total cost an employee will pay in dental fees,
    rounded to two decimal places after coverage is applied. 
    
    The function takes two arguments, an integer representing the employee's
    tier of coverage and a floating-point number representing the 
    total cost of the dental visit before coverage is applied. 
    
    Precondition: Tier is either 1, 2, or 3 and the dental bill >= 0
    
    EXAMPLE:
    
    >>> print_cost_after_coverage(1, 249)
    $0.00
    
    >>> print_cost_after_coverage(2, 249)
    $10.00
    
    >>> print_cost_after_coverage(3, 249)
    $25.00
    
    >>> print_cost_after_coverage(1, 250)
    $0.00
    
    >>> print_cost_after_coverage(2, 250)
    $0.00
    
    >>> print_cost_after_coverage(3, 250)
    $50.00
    
    >>> print_cost_after_coverage(1, 500)
    $100.00
    
    >>> print_cost_after_coverage(2, 500)
    $200.00
    
    >>> print_cost_after_coverage(3, 500)
    $300.00
    
    >>> print_cost_after_coverage(1, 1000)
    $250.00
    
    >>> print_cost_after_coverage(2, 1000)
    $400.00
    
    >>> print_cost_after_coverage(3, 1000)
    $600.00
    
    """
    if coverage_tier == 1:
        
        if dental_bill < 250:
            dental_cost = TIER_1_DENTAL_COST_UNDER_250
            print('$', format(dental_cost, '.2f'), sep='')
            
        elif dental_bill >= 250 and dental_bill <= 500:
            dental_cost = dental_bill - TIER_1_DENTAL_COVERAGE_250_TO_500
            if dental_cost < 0:
                dental_cost = 0
            print('$', format(dental_cost, '.2f'), sep='')
            
        else:
            dental_coverage = dental_bill * TIER_1_DENTAL_COVERAGE_OVER_500
            dental_cost = dental_bill - dental_coverage
            print('$', format(dental_cost, '.2f'), sep='')
            
    if coverage_tier == 2:
        
        if dental_bill < 250:
            dental_cost = TIER_2_DENTAL_COST_UNDER_250
            print('$', format(dental_cost, '.2f'), sep='')
            
        elif dental_bill >= 250 and dental_bill <= 500:
            dental_cost = dental_bill - TIER_2_DENTAL_COVERAGE_250_TO_500
            if dental_cost < 0:
                dental_cost = 0
            print('$', format(dental_cost, '.2f'), sep='')  
            
        else:
            dental_coverage = dental_bill * TIER_2_DENTAL_COVERAGE_OVER_500
            dental_cost = dental_bill - dental_coverage
            print('$', format(dental_cost, '.2f'), sep='')   
            
    if coverage_tier == 3:
        
        if dental_bill < 250:
            dental_cost = TIER_3_DENTAL_COST_UNDER_250
            print('$', format(dental_cost, '.2f'), sep='')
            
        elif dental_bill >= 250 and dental_bill <= 500:
            dental_cost = dental_bill - TIER_3_DENTAL_COVERAGE_250_TO_500
            if dental_cost < 0:
                dental_cost = 0
            print('$', format(dental_cost, '.2f'), sep='')
            
        else:
            dental_coverage = dental_bill * TIER_3_DENTAL_COVERAGE_OVER_500
            dental_cost = dental_bill - dental_coverage
            print('$', format(dental_cost, '.2f'), sep='')
            
            