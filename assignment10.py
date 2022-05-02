import doctest
from typing import List, Tuple
from song import Song
from playlist import Playlist


'''
1. Write the get_longer function below.
'''
def get_longer(song1: Song, song2: Song) -> Song:
    """
    This function takes two song instances as arguments. The function returns
    the Song with longer duration. If both songs have the same duration, the 
    song that is represented by the first parameter is returned. 
    
    Precondition: Song instances have a duration represented by a positive
    integer. 
    
    EXAMPLE:
    
    >>> get_longer(Song('Champions', 'Queen', 220), Song('Africa', 'Toto', 295))
    Song('Africa', 'Toto', 295)
    >>> get_longer(Song('Bites the Dust', 'Queen', 295), Song('Africa', 'Toto', 295))
    Song('Bites the Dust', 'Queen', 295)
    >>> get_longer(Song('Wonderwall', 'Oasis', 330), Song('Africa', 'Toto', 295))
    Song('Wonderwall', 'Oasis', 330)
    """
    
    if song2.get_duration() > song1.get_duration():
        return song2
    else:
        return song1 
    
    
    


'''
2. Write the count_with_artist function below.
'''
def count_with_artist(loSongs: List[Song], artist_name: str) -> int:
    """
    This function takes two arguements, a list of Song instances and a string
    represented an artist's name to search for.
    
    The function returns an integer representing the number of songs in the list
    by the given artist.
    
    EXAMPLE:
    
    >>> count_with_artist([Song('Champions', 'Queen', 220), Song('Africa', 'Toto', 295)], 'Blur')
    0
    >>> count_with_artist([Song('Champions', 'Queen', 220), Song('Africa', 'Toto', 295)], 'Queen')
    1
    >>> count_with_artist([Song('Champions', 'Queen', 220), Song('Bites the Dust', 'Queen', 295)], 'Queen')
    2
    >>> count_with_artist([Song('Champions', 'Queen', 220), Song('Bites the Dust', 'Queen', 295), Song('Africa', 'Toto', 295)], 'Queen')
    2
    """
    count = 0 
    
    for songs in loSongs:
        if songs.get_artist() == artist_name:
            count += 1
        
    return count


'''
Questions 3, 4, and 5 are found in playlist.py.
'''
