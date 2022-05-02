import doctest
from typing import List, Tuple

# represents the flight information for a passenger 
# represented by (departure_city, arrival_city, flight_duration)

FlightInfo = Tuple[str, str, float]

DEPARTURE_CITY = 0
ARRIVAL_CITY = 1
FLIGHT_DURATION = 2


def swap(list1: list, position1: int, position2: int) -> None:
    """
    This function takes a list of values and two integers representing positions
    in the list as arguments. The function then swaps the values in the list at 
    the specified positions. Nothing is returned, the given list is only 
    altered. 
    
    Precondition: Positions given are valid positions within the list, ie, 
    they are in the range of the length of the list.
    
    EXAMPLE:
    
    >>> swap([12, 4, 3, -2], 1, 3)
    >>> swap([12, 4, 3, -2], 0, 3)
    >>> swap([2, 3], 0, 1)
    >>> swap([2, 3, 4], 1, 2)
    """
    
    list1[position1], list1[position2] = list1[position2], list1[position1]
    
          
def index_of_smallest(list1: list) -> int:
    """
    This function takes a list of values as an argument and finds and returns
    the position of the smallest value. If there are duplicate entires of the
    smallest value, the function returns the index of the first occurence. 
    
    If the list is empty, the function returns -1.
    
    EXAMPLE:
    
    >>> index_of_smallest([])
    -1
    
    >>> index_of_smallest([12, 6, 2, 22, -14, 10, -2])
    4
    
    >>> index_of_smallest([12, 6, 2, 22, -14, 10, -2, -2])
    4
    
    >>> index_of_smallest([300204])
    0
    
    >>> index_of_smallest([300204, 1])
    1
    
    index_of_smallest([300204, 1, -30])
    2
    
    """
    
    if len(list1) == 0:
        return -1
    
    smallest_value = min(list1)
        
    for index in range(len(list1)):
        if list1[index] == smallest_value:
            return index
        

def total_duration(flight_info: List[FlightInfo]) -> float:
    """
    This function takes a list of flight information tuples(as described
    in the tuple alias, FlightInfor) and calculates and returns the 
    total duration of all flights in the given list.
    
    EXAMPLE:
    
    >>> total_duration([])
    0
    
    >>> total_duration([('Victoria', 'Mexico City', 5.5), ('Vancouver', 'Toronto', 4)])
    9.5
    
    >>> total_duration([('Victoria', 'Mexico City', 5.5)])
    5.5
    
    >>> total_duration([('Vancouver', 'Toronto', 4)])
    4
    
    
    """
    
    total_flight_time = 0
    
    for info in flight_info:
        total_flight_time += info[FLIGHT_DURATION]
        
    return total_flight_time
        
        
def get_destinations_from(flight_info: List[FlightInfo], departure_city: str) -> List[str]:
    """
    Takes a list of flight information tuples (as described in the type 
    alias FlightInfo) and a departure city. 
    
    The function returns a list of all the unique destinations that are flown
    to from the given departure  city.
    
    EXAMPLE:
    
    >>> get_destinations_from([], 'Victoria')
    []
    
    >>> get_destinations_from([('Victoria', 'Vancouver', 0.75)], 'Victoria')
    ['Vancouver']
    
    >>> get_destinations_from([('Victoria', 'Vancouver', 0.75)], 'Vancouver')
    []
    
    >>> get_destinations_from([('Victoria', 'Vancouver', 0.75), ('Victoria', 'Cairo')], 'Victoria')
    ['Vancouver', 'Cairo']
    
    >>> get_destinations_from([('Victoria', 'Vancouver', 0.75), ('Rome', 'Cairo')], 'Victoria')
    ['Vancouver']
    
    
    """
    
    
    list_destinations = []
    
    for info in flight_info:
        if info[DEPARTURE_CITY] == departure_city:
            if info[ARRIVAL_CITY] not in list_destinations:
                list_destinations.append(info[ARRIVAL_CITY])
        
        
    return list_destinations
    
          
    