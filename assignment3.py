import doctest

BAD_SERVICE_TIP = 0.10

AVERAGE_SERVICE_TIP = 0.15

GOOD_SERVICE_TIP = 0.20

EXCELLENT_SERVICE_TIP = 0.25

LEVEL_0_BRIGHTNESS_BATTERY_LIFE = 1.0

LEVEL_1_BRIGHTNESS_BATTERY_LIFE = 0.90

LEVEL_2_BRIGHTNESS_BATTERY_LIFE = 0.75

LEVEL_3_BRIGHTNESS_BATTERY_LIFE = 0.50

MAXIMUM_BATTERY_LIFE = 15

def box_volume(length: int, width: int, height: int) -> int:
    """
    This function takes three arguments, all being integers representing
    length, width and height.
    
    The function returns the product of all three integers, representing the
    volume of the box in m^3.
    
    Precondition: length, width and height are all > 0
    
    EXAMPLE:
    
    >>> box_volume(1, 2, 3)
    6
    
    >>> box_volume(3, 4, 5)
    60
    
    >>> box_volume(1, 1, 1)
    1
    
    >>> box_volume(200, 33, 5)
    33000
    
    """
    
    box_volume = length * width * height
    
    return box_volume

def is_factor(n1: int, n2: int) -> bool:
    """
    This function takes two integers as arguments and determines whether 
    the first integer is a factor of the second integer.
    
    Returns True if n1 is a factor of n2, and False otherwise.
    
    EXAMPLE:
    
    >>> is_factor(8, 64)
    True
    
    >>> is_factor(12, 35)
    False
    
    >>> is_factor(23, 23)
    True
    
    >>> is_factor(8, 0)
    True
    
    >>> is_factor(0, 8)
    False
    
    """
    if n1 == 0:
        return False
    
    return n2 % n1 == 0
        
def bill_with_tip(dinner_bill: float, service_rating: str) -> float:
    """
    This function takes two arguments, a floating-point number representing
    the bill for dinner and a string representing the level of service.
    
    The level of service determines the percentage of tip added to the bill.
    
    The function then calculates and returns a floating-point value
    representing the final bill, including the tip.
    
    Preconditions: 
    
    Only possible values for service_rating are 'bad', 'average',
    'good' and 'excellent'. 
    
    dinner_bill must be >= 0
    
    EXAMPLE:
    
    >>> bill_with_tip(100.50, 'bad')
    110.55
    
    >>> bill_with_tip(100.50, 'average')
    115.575
    
    >>> bill_with_tip(100.50, 'good')
    120.6
    
    >>> bill_with_tip(100.50, 'excellent')
    125.625
    
    >>> bill_with_tip(66, 'bad')
    72.6
    
    >>> bill_with_tip(66, 'average')
    75.9
    
    >>> bill_with_tip(66, 'good')
    79.2
    
    >>> bill_with_tip(66, 'excellent')
    82.5
    
    >>> bill_with_tip(0, 'excellent')
    0.0
    
    """
    
    if service_rating == 'bad':
        bill_total = dinner_bill + dinner_bill * BAD_SERVICE_TIP
        
    elif service_rating == 'average':
        bill_total = dinner_bill + dinner_bill * AVERAGE_SERVICE_TIP
    
    elif service_rating == 'good':
        bill_total = dinner_bill + dinner_bill * GOOD_SERVICE_TIP
        
    elif service_rating == 'excellent':
        bill_total = dinner_bill + dinner_bill * EXCELLENT_SERVICE_TIP
        
    
    return bill_total

def character_at_index(phrase: str, phrase_index: int) -> str:
    """
    This function takes two arguments, a string and an integer representing
    an index of the string. 
    
    The function returns the character in the string of the given index. 
    
    If the index number is outside of the range of the index of the string
    this function will return ''
    
    EXAMPLE:
    
    >>> character_at_index('Wall Street', 0)
    'W'
    
    >>> character_at_index('Wall Street', 10)
    't'
    
    >>> character_at_index('Wall Street', 4)
    ' '
    
    >>> character_at_index('Wall Street', 13)
    ''
    
    >>> character_at_index('', 0)
    ''
    
    >>> character_at_index('', 12)
    ''
    
    """
    
    if phrase_index >= len(phrase):
        return ''
    
    return phrase[phrase_index]

def same_first_and_last_character(phrase: str) -> bool:
    """
    This function takes a string as an arugument and determines whether the
    string has the same first and last character.
    
    If the string does have the same first and last character, this function
    returns True.
    
    If the string contains no characters or a single character,
    the function also returns True. 
    
    The function returns false if the first and last characters of the string
    are not identicial.
    
    EXAMPLE:
    
    >>> same_first_and_last_character('fluff')
    True
    
    >>> same_first_and_last_character('fluffy')
    False
    
    >>> same_first_and_last_character('')
    True
    
    >>> same_first_and_last_character('F')
    True
    
    >>> same_first_and_last_character('f')
    True
    
    >>> same_first_and_last_character('Ff')
    False
    
    >>> same_first_and_last_character('Mom')
    False
    
    >>> same_first_and_last_character('mom')
    True
    
    """
    
    if phrase == '':
        return True    
    
    elif phrase[0] == phrase[-1]:
        return True
    
    else:
        return False
    
def brightness_modifier(brightness_setting: int) -> float:
    """
    This function takes an integer as an argument representing the brightness 
    level on a mobile phone.
    
    The function returns a floating-point number between 0.5 and 1.0 
    representing the modifier the brightness level has on the lifetime of 
    battery for the device.
    
    Precondition: briightness_setting must be either 0, 1, 2, or 3
    
    EXAMPLE:
    
    >>> brightness_modifier(0)
    1.0
    
    >>> brightness_modifier(1)
    0.9
    
    >>> brightness_modifier(2)
    0.75
    
    >>> brightness_modifier(3)
    0.5
    
    """
    
    if brightness_setting == 0:
        return LEVEL_0_BRIGHTNESS_BATTERY_LIFE
    
    elif brightness_setting == 1:
        return LEVEL_1_BRIGHTNESS_BATTERY_LIFE
    
    elif brightness_setting == 2:
        return LEVEL_2_BRIGHTNESS_BATTERY_LIFE
    
    elif brightness_setting == 3:
        return LEVEL_3_BRIGHTNESS_BATTERY_LIFE
    
    else:
        return print('INVALID BRIGHTNESS SETTING')
    
def hours_remaining(battery_life: int, brightness_level: int,
                    streaming_video: bool) -> float:
    """
    This function takes 2 integers and a boolean value as arguments representing
    the battery life, brightness level and whether or not a  video is streaming 
    on a device.
    
    The function returns a floating-point value representing the total numbers 
    of hours of battery life left on a device.
    
    Precondition: battery_life is an integer between 0 and 100 and 
                  brightness_level is an integer 0, 1, 2, or 3.
                  
    EXAMPLE:
    
    >>> hours_remaining(80, 2, True)
    4.5
    
    >>> hours_remaining(80, 2, False)
    9.0
    
    >>> hours_remaining(100, 0, False)
    15.0
    
    >>> hours_remaining(100, 1, False)
    13.5
    
    >>> hours_remaining(100, 2, False)
    11.25
    
    >>> hours_remaining(100, 3, False)
    7.5
    
    >>> hours_remaining(100, 0, True)
    7.5
    
    >>> hours_remaining(100, 1, True)
    6.75
    
    >>> hours_remaining(100, 2, True)
    5.625
    
    >>> hours_remaining(100, 3, True)
    3.75
    
    >>> hours_remaining(0, 3, True)
    0.0
    
    >>> hours_remaining(0, 3, False)
    0.0
    
    >>> hours_remaining(50, 3, True)
    1.875
    
    >>> hours_remaining(50, 3, False)
    3.75
    
    """
    battery_life = battery_life/100
    
    battery_remaining = MAXIMUM_BATTERY_LIFE * battery_life
    
    battery_after_brightness = battery_remaining * brightness_modifier(
        brightness_level)
    
    if streaming_video == True:
        num_hours_remaining = battery_after_brightness/2
        
    else:
        num_hours_remaining = battery_after_brightness
        
    return num_hours_remaining
    
    