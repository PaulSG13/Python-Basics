import doctest
import random

MIN_DIE = 1
MAX_DIE = 6
GAME_END = 50


def play_pig() -> None:
    """ 
    Simulates a game of Pig. When either the human player or the computer 
    reach GAME_END points, the results of the game should be printed.
    
    During the human player's turn:
    - the user rolls a six-sided die as many times as they wish
    - the score for the player's turn is equal to the sum of all
      rolls of the die
    - if a 1 is ever rolled, the player scores 0 for the round and
      their turn ends immediately
    
    During the computer's turn:
    - the computer always attempts to roll the die exactly three times
    - if a 1 is rolled, the computer scores 0 for the round
    - otherwise, the computer scores the sum of the three die rolls
    
    """    
    
    player_score = 0
    computer_score = 0
    
    while player_score < GAME_END:
        player_score += player_turn()
        computer_score += computer_turn()
        print('Your score:', player_score)
        print('Computer score:', computer_score)
        print()
        if computer_score >= GAME_END:
            break
        
        
    print_results(player_score, computer_score)
            

def print_results(player_score: int, computer_score: int) -> None:
    """
    This function prints the results of the game of Pig.
    
    It can be assumed the scores will be greater than or equal to the 
    GAME_END constant variable, which is assumed is >= 0.
    
    >>> print_results(100, 88)
    You win 100 - 88
    >>> print_results(99, 100)
    The computer wins 100 - 99
    >>> print_results(103, 102)
    You win 103 - 102
    >>> print_results(4, 145)
    The computer wins 145 - 4
    >>> print_results(108, 108)
    It's a tie 108 - 108
    """
    
    if player_score > computer_score:
        print('You win', player_score, '-', computer_score)
    
    elif player_score < computer_score:
        print('The computer wins', computer_score, '-', player_score)
        
    else:
        print('It\'s a tie', player_score, '-', computer_score)


def player_turn() -> int:
    """
    Simulates the players turn in a game of Pig. Returns the score 
    for the player based on the die rolls
    
    The player can choose to roll the die as many times as they wish.
    Their turn score is calculated as the sum of all die rolls. 
    If a 1 is ever rolled, they get a score of 0 for the round and
    their turn ends immediately.
    """
    
    score = 0
    roll = 0
    
    while roll != 1:
            roll = roll_once()
            print('You rolled', roll)  
            
            if roll == 1:
                score = 0  
                
            else:
                score += roll
                user_response = handle_user_input()
                if user_response == False:
                    break

    print('Your score for the round is', score)
    print()
    return score


def handle_user_input() -> bool:
    """
    Handles user input by repeatedly asking if the user wants to roll
    a die until either a 'y' or 'n' are entered. 
    
    Returns True if the user entered y, False if input user entered n
    """
    # TODO: implement this function
    
    prompt = 'Would you like to roll again(y/n)? '
    
    user_response = input(prompt)
    
    while user_response != 'y' or 'n':
        
        if user_response == 'y':
            return True
    
        elif user_response == 'n':
            return False
        
        print('Invalid response, please enter either y or n')
        user_response = input(prompt)
        


def computer_turn() -> int:
    """ 
    Simulates the computer's turn in a round of Pig. Returns the 
    score for the computer's turn based on the die rolls.
    
    The computer always attempts to roll three dice, and takes the 
    sum of the three rolls, unless a 1 is rolled, which results 
    in a score of 0.
    """  
    score = 0
    roll = 0
    num_rolls = 0
    
    while roll != 1 and num_rolls < 3:
        roll = roll_once()
        print('The computer rolled', roll)
        num_rolls += 1
        if roll == 1:
            score = 0
        else: 
            score += roll

    print('The computer\'s score for the round is', score)
    print()
    return score


def roll_once() -> int:
    """ 
    Simulates the roll of a single die and returns the value.
    The value returned will be an integer between MIN_DIE and MAX_DIE
    """
    roll = random.randint(MIN_DIE, MAX_DIE)
    return roll

