"""
Write a program whose input is two integers and whose output is the two integers swapped.

Ex: If the input is:

3
8
the output is:

8 3
Your program must define and call the following function. swap_values() returns the two values in swapped order.
def swap_values(user_val1, user_val2)
"""

def swap_values(user_val1: int, user_val2: int) -> tuple:
    """Returns given values in swapped order.
    
    Args:
        user_val1 (int): First value given by the user.
        user_val2 (int): Second value given by the user.

    Returns:
        Given values in swapped order.
    """
    return user_val2, user_val1


if __name__ == '__main__': 

    # Get values from standard input
    user_val1 = int(input())
    user_val2 = int(input())

    # Call swap_values function and assign return value to original variables
    user_val1, user_val2 = swap_values(user_val1, user_val2)

    # Print swapped values
    print(user_val1, user_val2)