
POUNDS_PER_KG = 2.20462

def print_cat():
    """
    This function prints an image of a cat with keyboard characters.
    
    EXAMPLE:
    
    >>> print_cat()
    | /\_/\ |
    | >^c^< |
    |  / \  |
    | (|_|)~|
        
    """
    print('|' + ' /\_/\ ' + '|')
    print('|' + ' >^c^< ' + '|')
    print('|' + '  / \  ' + '|')
    print('|' + ' (|_|)~' + '|')


def print_frog():
    """
    This function prints an image of a frog with keyboard characters.
    
    EXAMPLE:
    
    >>> print_frog()
    |  @ @  |
    | (---) |
    |( > < )|
    |""   ""|
    
    """
    print('|' + '  @ @  ' + '|')
    print('|' + ' (---) ' + '|')
    print('|' + '( > < )' + '|')
    print('|' + '""   ""' + '|')


def print_spacer():
    """
    This function prints a spacer with the use of keyboard characters.
    It can be used inbetween images in order to seperate them or on its own.
    
    EXAMPLE:
    
    >>> print_spacer()
    /-------\
        
    """
    print('/'+ '-'*7 + '\\')


def print_logo():
    """
    This function prints an image of a frog, cat, frog and cat again using 
    keyboard characters. 
    Each image begins with the spacer '/-------\'.
    To denote the end of the set of images, 2 spacers are printed.
    
    EXAMPLE:
    
    >>> print_logo()
    /-------\
    |  @ @  |
    | (---) |
    |( > < )|
    |""   ""|
    /-------\
    | /\_/\ |
    | >^c^< |
    |  / \  |
    | (|_|)~|
    /-------\
    |  @ @  |
    | (---) |
    |( > < )|
    |""   ""|
    /-------\
    | /\_/\ |
    | >^c^< |
    |  / \  |
    | (|_|)~|
    /-------\
    /-------\
    
    """
    print_spacer()
    print_frog()
    
    print_spacer()
    print_cat()
    
    print_spacer()
    print_frog()
    
    print_spacer()
    print_cat()
    
    print_spacer()
    print_spacer()


def kgs_to_lbs(kgs: float):
    """
    This function converts kilograms of floating-point numbers into pounds.
    The conversion rate used in this function is 1kg = 2.20462 lbs.  
    
    EXAMPLE:
    
    >>> kgs_to_lbs(90)
    198.4158 lbs
        
    >>> kgs_to_lbs(177.64)
    391.62869679999994 lbs
    
    """
    pounds = kgs * POUNDS_PER_KG
    print(pounds, 'lbs')

