"""
Write a program with total change amount as an integer input, and output the change using the fewest coins, 
one coin type per line. 
The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. 
Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

Ex: If the input is:

0 
(or less than 0), the output is:

No change 
Ex: If the input is:

45
the output is:

1 Quarter
2 Dimes 
"""

# Get number of cents from standard input
input_cents = int(input())
cents = input_cents

# Calculate the quantity of each coin
dollars, cents = divmod(cents, 100)
quarters, cents = divmod(cents, 25)
dimes, cents = divmod(cents, 10)
nickels, cents = divmod(cents, 5)

# Print results using conditional logic
if input_cents <= 0:
    print('No change')
else:
    if dollars > 0:
        print(f'{dollars} Dollars' if dollars > 1 else '1 Dollar')
    if quarters > 0:
        print(f'{quarters} Quarters' if quarters > 1 else '1 Quarter')
    if dimes > 0:
        print(f'{dimes} Dimes' if dimes > 1 else '1 Dime')
    if nickels > 0:
        print(f'{nickels} Nickels' if nickels > 1 else '1 Nickel')
    if cents > 0:
        print(f'{cents} Pennies' if cents > 1 else '1 Penny')
