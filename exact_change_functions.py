"""
Write a program with total change amount as an integer input that outputs the change using the fewest coins,
one coin type per line. The coin types are dollars, quarters, dimes, nickels, and pennies. 
Use singular and plural coin names as appropriate, like 1 penny vs. 2 pennies.

Ex: If the input is:
0 
or less, the output is:
no change
Ex: If the input is:
45
the output is:

1 quarter
2 dimes 
Your program must define and call the following function. The function exact_change() should return num_dollars, num_quarters, num_dimes, num_nickels, and num_pennies.
def exact_change(user_total)
"""

def exact_change(user_total: int) -> None:
    """
    Calculates the exact change in dollars, quarters, dimes, nickels, and cents for a given amount of cents.

    Args:
        user_total (int): The total amount in cents.

    Returns:
        tuple: A tuple containing the number of dollars, quarters, dimes, nickels, and cents.
    """
    cents = user_total
    dollars, cents = divmod(cents, 100)
    quarters, cents = divmod(cents, 25)
    dimes, cents = divmod(cents, 10)
    nickels, cents = divmod(cents, 5)
    return dollars, quarters, dimes, nickels, cents


if __name__ == '__main__':
    
    # Get number of cents from standard input
    input_cents = int(input())

    # Use conditional logic to determine what is printed to standard output
    if input_cents <= 0:
        print('no change')
    else:
        num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_cents)
        if num_dollars > 0:
            print(f'{num_dollars} dollars' if num_dollars > 1 else '1 dollar')
        if num_quarters > 0:
            print(f'{num_quarters} quarters' if num_quarters > 1 else '1 quarter')
        if num_dimes > 0:
            print(f'{num_dimes} dimes' if num_dimes > 1 else '1 dime')
        if num_nickels > 0:
            print(f'{num_nickels} nickels' if num_nickels > 1 else '1 nickel')
        if num_pennies > 0:
                print(f'{num_pennies} pennies' if num_pennies > 1 else '1 penny')
