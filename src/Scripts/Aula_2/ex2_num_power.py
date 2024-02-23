"""
Exercise 2: Power of a Number
Implement a recursive function that calculates x raised to the power of
y, where x is a real number and y is a non-negative integer.
"""

def power(x, y):
    """
    This function calculates a number x raised to the power of y if Y is not a non-negative integer
    """
    if (y != int and y < 0):
        return print("Y is a negative number")
    return print(x ** y)

base = input("Enter the base number: ")
exponent = input("Enter its exponent: ")
power(float(base), int(exponent))
