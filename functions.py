import random, string

#this file contains various functions and calls that are called / used to perform various actions  

def random_strings(length_of_string):
    '''
    This function will return A random string of specified length

    Parameters
    ---
    length_of_string : int
        The required length of a string
    '''
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length_of_string))