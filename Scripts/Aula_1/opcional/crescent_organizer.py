"""
This module receives an array of numbers, finds the greatest number among them, and prints it.
"""

# This is the list of numbers that we will be processing.
LIST = [2, 10, 7, 2, 5, 3, 8]

# We start by assuming that the greatest number is 0, which is smaller than all positive numbers.
GREATER = 0

# This is a 'for' loop that goes through each number in the list.
for NUM in LIST:
    # For each number, we check if it's greater than our current greatest number.
    if NUM > GREATER:
        # If it is, then we have a new greatest number, so we update our greatest number.
        GREATER = NUM

# After we've checked all the numbers, we print the greatest number.
print(GREATER)
