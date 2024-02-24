"""
Exercise 3: Fibonacci
Write a recursive function that returns the nth number of
Fibonacci. Remember that the Fibonacci sequence is
defined as fib(n) = fib(n-1) + fib(n-2) with fib(0) = 0 and fib(1) = 1.
"""
def fibonacci(n):
    """
    This function return the number for the inputed fibonnaci sequence
    """
    if n <= 0:
        return "The input value must be a positive integer."
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

fib_inp = int(input("Enter the number to return the position of the Fibonacci sequence: "))
print(fibonacci(fib_inp))
