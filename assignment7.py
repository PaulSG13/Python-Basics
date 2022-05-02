import doctest
from typing import List, Tuple

# represents the date with (year, month, day)
# where year >= 1582
# where month is a valid month in the Gregorian calendar  
# where month is also capitalized on initial letter with no abbreviations
# where day is a valid day given the values of the year and month

DateInfo = Tuple[int, str, int]

YEAR = 0 
MONTH = 1
DAY = 2


# represents the flight information for a passenger 
# represented with (departure_city, arrival_city, flight_duration)


FlightInfo = Tuple[str, str, float]

DEPARTURE_CITY = 0
ARRIVAL_CITY = 1
FLIGHT_DURATION = 2


# represents the flight schedules of a specific flight in date format 
# represented by the previous type aliases FlightInfo and DateInfo


FlightSchedule = Tuple[FlightInfo, List[DateInfo]]

FLIGHT_INFO = 0

DEPARTURE_DATES = 1



def return_zodiac_sign(month: str, day: int) -> str:
    """
    This function takes two arguments, one for a month of the year as a string
    and the other for a day in the month as an integer.
    
    The function then returns the name of the zodiac sign associated with that
    date.
    
    Precondition: month and day must be valid dates.
    
    EXAMPLE:
    
    >>> return_zodiac_sign('January', 19)
    'Capricorn'
    
    >>> return_zodiac_sign('January', 20)
    'Aquarius'
    
    >>> return_zodiac_sign('February', 18)
    'Aquarius'
    
    >>> return_zodiac_sign('February', 19)
    'Pisces'
    
    >>> return_zodiac_sign('March', 20)
    'Pisces'
    
    >>> return_zodiac_sign('March', 21)
    'Aries'
    
    >>> return_zodiac_sign('April', 19)
    'Aries'
    
    >>> return_zodiac_sign('April', 20)
    'Taurus'
    
    >>> return_zodiac_sign('May', 20)
    'Taurus'
    
    >>> return_zodiac_sign('May', 21)
    'Gemini'
    
    >>> return_zodiac_sign('June', 20)
    'Gemini'
    
    >>> return_zodiac_sign('June', 21)
    'Cancer'
    
    >>> return_zodiac_sign('July', 22)
    'Cancer'
    
    >>> return_zodiac_sign('July', 23)
    'Leo'
    
    >>> return_zodiac_sign('August', 22)
    'Leo'
    
    >>> return_zodiac_sign('August', 23)
    'Virgo'
    
    >>> return_zodiac_sign('September', 22)
    'Virgo'
    
    >>> return_zodiac_sign('September', 23)
    'Libra'
    
    >>> return_zodiac_sign('October', 22)
    'Libra'
    
    >>> return_zodiac_sign('October', 23)
    'Scorpio'
    
    >>> return_zodiac_sign('November', 21)
    'Scorpio'
    
    >>> return_zodiac_sign('November', 22)
    'Sagittarius'
    
    >>> return_zodiac_sign('December', 21)
    'Sagittarius'
    
    >>> return_zodiac_sign('December', 22)
    'Capricorn'
    
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
        
    return zodiac_sign
    

    
def multiply_by(List1: list, multiplier: int) -> None:
    """
    This function takes a list of elements and an integer multiplier as 
    arguments.
    
    This function multiplies every element in the given list by the given 
    multiplier.
    
    Precondition: The given list contains elements that can be multipied.
    
    EXAMPLE:
    
    >>> multiply_by([], 2)
    >>> multiply_by([1, 2, 3], 2)
    >>> multiply_by([], 1)
    >>> multiply_by(['dog', 'cat'], 2)
    >>> multiply_by(['dog', 'cat', 3, 4.2], 2)
    
    """
    
    for index in range(len(List1)):
        List1[index] *= multiplier
        
           
def double_odd(loi: List[int]) -> None:
    """
    This funtion takes a list of integers as arguments and doubles all of the 
    odd-valued elements in the list. 
    
    EXAMPLE:
    
    >>> double_odd([])
    >>> double_odd([2, 4, 6])
    >>> double_odd([1, 3, 5])
    
    """
    
    # Have to come back to this 
    
    for index in range(len(loi)):
        if loi[index] % 2 != 0:
            loi[index] *= 2
                     
    
def get_zodiac_signs(zodiac_date: DateInfo) -> List[str]:
    """
    This function uses the return_zodiac_sign funtion stated at the beginning 
    of the file as a helper function. 
    
    The function takes a list of date information tuples as specified in 
    DateInfo. The function returns a list of corresponding zodiac signs for the
    dates in the given list. 
    
    The order of the zodiac values corresponds to the order of the date
    information in the given list.
    
    EXAMPLE:
    
    >>> get_zodiac_signs([])
    []
    
    >>> get_zodiac_signs([(1990, 'September', 15), (1829, 'December', 28), (1845, 'August', 27)])
    ['Virgo', 'Capricorn', 'Virgo']
    
    >>> get_zodiac_signs([(2001, 'March', 6), (1829, 'September', 19)])
    ['Pisces', 'Virgo']
    
    >>> get_zodiac_signs([(2001, 'December', 6), (1662, 'October', 19)])
    ['Sagittarius', 'Libra']
    
    >>> get_zodiac_signs([(2001, 'July', 6)])
    ['Cancer']
    

    """
    list_of_zodiacs = []
    
    for dates in zodiac_date:
        zodiac_sign = return_zodiac_sign(dates[MONTH], dates[DAY])
        list_of_zodiacs.append(zodiac_sign)
        
    return list_of_zodiacs



def create_lodates(lomonths: List[str], lodays: List[int], loyears: List[int]) -> List[DateInfo]:
    """
    This function takes a list of month names, list of days as integers
    and a list of years as integers.
    
    The function creates and returns a new list of date information tuples 
    constructed using the values in the given lists. 
    
    Precondition: The givens lists are all of equal length and the values in the 
    given lists combine to make valid dates. 
    
    EXAMPLE:
    
    >>> create_lodates([], [], [])
    []
    
    >>> create_lodates(['January', 'June'], [20, 10], [1987, 2020])
    [(1987, 'January', 20), (2020, 'June', 10)]
    
    >>> create_lodates(['January'], [20], [1987])
    [(1987, 'January', 20)]
    
    >>> create_lodates(['January', 'June', 'March'], [20, 10, 30], [1987, 2020, 2021])
    [(1987, 'January', 20), (2020, 'June', 10), (2021, 'March', 30)]
    
    """
    
    list_of_dates = [] 
    
    for index in range(len(lomonths)):
        DateInfo = (loyears[index], lomonths[index], lodays[index])
        list_of_dates.append(DateInfo)    
        
    return list_of_dates
    
    
    
    
    
def contains_month(lodate_tuples: List[DateInfo], month: str) -> bool:
    """
    This function takes a list of date information tuples (as described in 
    DateInfo at the top of the file) and an additional string argument that 
    specifies a valid month. 
    
    The function determines whether or not the given month is in the list of 
    date information tuples.
    
    Precondition: Second argument in the function is a valid month in the 
    Gregorian calender and the initial letter is capitalized and no 
    abbreviations are used.
    
    EXAMPLE:
    
    >>> contains_month([], 'January')
    False
    
    >>> contains_month([(1987, 'January', 20)], 'January')
    True
    
    >>> contains_month([(1987, 'January', 20)], 'March')
    False
    
    >>> contains_month([(1987, 'January', 20), (2001, 'March', 1998)], 'March')
    True
    
    >>> contains_month([(1987, 'January', 20), (2001, 'March', 1998)], 'April')
    False
    
    """
    
    for info in lodate_tuples:
        for dates in info:
            if dates == month:
                return True
        
    return False


def get_flights_in_month(flight_schedule: List[FlightSchedule], flight_month: str) -> List[FlightInfo]:
    """
    This function takes a list of flight schedule information tuples 
    (as described in the FlightSchedule type alias at the top of this file) 
    and an additional string argument that specifies a valid month. 
    
    The function returns a list of flight information (as described in the 
    FlightInfo alias at the top of this file) of the flights in the given list
    that are scheduled in the given month. 
    
    Precondition: The second argument is a valid month in the Gregorian calendar
    and the initial letter is capitalized and no abbreviations are used. 
    
    EXAMPLE:
    
    >>> flight_van_tor = ('Vancouver', 'Toronto', 4)
    >>> dates_van_tor = [(2020, 'October', 1), (2020, 'October', 12), (2020, 'November', 12), (2020, 'December', 1)]
    >>> flight_schedule_van_tor = (flight_van_tor, dates_van_tor)
    >>> flight_lon_mos = ('London', 'Moscow', 6)
    >>> dates_lon_mos = [(2020, 'October', 21), (2020, 'December', 14), (2021, 'March', 21)]
    >>> flight_schedule_lon_mos = (flight_lon_mos, dates_lon_mos)
    >>> flight_sea_bang = ('Seattle', 'Bangkok', 6)
    >>> dates_sea_bang = [(2020, 'October', 18), (2020, 'November', 6)]
    >>> flight_schedule_sea_bang = (flight_sea_bang, dates_sea_bang)
    >>> list_of_flight_schedules = [flight_schedule_van_tor,flight_schedule_lon_mos,flight_schedule_sea_bang]
    
    
    
    >>> get_flights_in_month(list_of_flight_schedules, 'October')
    [('Vancouver', 'Toronto', 4), ('London', 'Moscow', 6), ('Seattle', 'Bangkok', 6)]
    
    >>> get_flights_in_month(list_of_flight_schedules, 'November')
    [('Vancouver', 'Toronto', 4), ('Seattle', 'Bangkok', 6)]
    
    >>> get_flights_in_month(list_of_flight_schedules, 'December')
    [('Vancouver', 'Toronto', 4), ('London', 'Moscow', 6)]
    
    >>> get_flights_in_month(list_of_flight_schedules, 'March')
    [('London', 'Moscow', 6)]
    
    >>> get_flights_in_month(list_of_flight_schedules, 'June')
    []
    
    >>> get_flights_in_month(list_of_flight_schedules, 'July')
    []
    
    
    """
    
    list_of_flights = []
    
    for flights in flight_schedule:
        for flight_departures in flights[DEPARTURE_DATES]:
            if contains_month(flights[DEPARTURE_DATES], flight_month):
                if flights[FLIGHT_INFO] not in list_of_flights:
                    list_of_flights.append(flights[FLIGHT_INFO])
        
    
    return list_of_flights
    
  