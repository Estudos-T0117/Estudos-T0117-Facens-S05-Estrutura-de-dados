"""
Exercise 4: String Reversal
Develop a recursive function that receives a string s and
returns the same string, but with the characters in reverse order.
"""

# This is our recursive function to reverse a string
def reverse_string(s):
    # Base case: if the string is empty, we return it as is
    if len(s) == 0:
        return s
    else:
        # We print the current string for debugging purposes
        print(s)
        # Recursive case: we call the function with the string excluding the first character (s[1:])
        # and then append the first character (s[0]) to the end of the result
        # This effectively reverses the string
        return reverse_string(s[1:]) + s[0]

# We ask the user for a string to reverse and pass it to our function
# The result is then printed to the console
print(reverse_string(input("Enter the string you want to reverse: ")))
