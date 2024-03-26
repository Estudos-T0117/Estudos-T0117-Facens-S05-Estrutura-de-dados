"""
Exercise 1: Sum of Numbers
Write a recursive function that receives a positive integer n
and returns the sum of all integers from 1 to n
"""

# def summation(n):
#     """
#     This function do the progressive sum from o to the inputed value
#     """

#     x = 0
#     regression = 0
#     while x <= n:
#         regression += x
#         x += 1
#     print(regression)

def summation(n):
    """
    This function do the recursive sum from o to the inputed value
    """
    if( n<= 1 ):
        return 1
    else:
        return n + summation(n-1)
    
y = input("Enter a number for regression: ")
print(summation(int(y)))

