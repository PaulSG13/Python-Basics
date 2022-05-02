import doctest



def print_name_age_v1() -> None:
    """
    This function prompts a user to enter their name then prompts the user to
    enter their age. 
    It then prints 'hello' followed by the name and category of age.
    """
    
    
    prompt_name = 'What is your name? '
    user_response_name = input(prompt_name)
    
    prompt_age = 'How old are you? '
    user_response_age = int(input(prompt_age))
    
    if user_response_age < 18:
        print('hello', user_response_name, 'child')
        
    elif user_response_age >= 18 and  user_response_age < 65:
        print('hello', user_response_name, 'adult')
        
    else:
        print('hello', user_response_name, 'senoir')
        
def print_name_age_v2() -> None:
    """
    This function prompts a user to enter their name then prompts the user to
    enter their age. 
    It then prints 'hello' followed by the name and category of age.
    If the user enters an invalid age it prints the name and 'you are lying
    about your age'.
    
    """
    
    prompt_name = 'What is your name? '
    user_response_name = input(prompt_name)
    
    
    
    prompt_age = 'How old are you? '
    user_response_age = input(prompt_age)
    
    
    if not user_response_age.isdigit():
        print('hello', user_response_name, 'you are lying about your age.')
        return
    
    user_response_age_as_int = int(user_response_age)
    
    if user_response_age_as_int < 18:
        print('hello', user_response_name, 'child')
        
    elif user_response_age_as_int >= 18 and  user_response_age < 65:
        print('hello', user_response_name, 'adult')
        
    else:
        print('hello', user_response_name, 'senoir')     
    
    
def get_num(min_value: int) -> int:
    """
    This function repeatedly asks the user to enter a number until the user
    enters a valid integer greater than or equal to the argument. 
    It then returns the valid entry as an integer.
    
    Precondition: min_value will be >= 0
    
    """
    
    prompt = 'Please enter a valid integer: '
    
    user_response = input(prompt)
    
    while not user_response.isdigit() or int(user_response) < min_value:
        user_response = input(prompt)
        
    response_as_int = int(user_response)
    return response_as_int
        
        
def print_name_age_v3() -> None:
    """
    This function prompts a user to enter their name then prompts the user to
    enter their age. 
    It then prints 'hello' followed by the name and category of age.
    If the user enters an invalid age it will continue to ask the user for
    a number until they enter a number that is a valid age.
    
    """
    
    prompt_name = 'What is your name? '
    user_response_name = input(prompt_name)
    
    prompt_age = 'How old are you? '
    user_response_age = input(prompt_age)
    
    
    if not user_response_age.isdigit():
        user_response_age = get_num(0)
    
    user_response_age = int(user_response_age)
    
    if user_response_age >= 0 and user_response_age < 18:
        print('hello', user_response_name, 'child')
        
    elif user_response_age >= 18 and  user_response_age < 65:
        print('hello', user_response_name, 'adult')
        
    else:
        print('hello', user_response_name, 'senoir')    
        
    