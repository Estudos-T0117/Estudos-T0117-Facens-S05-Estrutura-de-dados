"""
This module asks the user to input two numbers and prints their sum.
"""

# Ask the user to input their first number.
#The input is converted to a floating point number and stored in the variable 'x'.
PROMPT1 = "digite seu primeiro numero: "
x = float(input(PROMPT1))

# Ask the user to input their second number.
#The input is converted to a floating point number and stored in the variable 'y'.
PROMPT2 = "digite seu segundo numero: "
y = float(input(PROMPT2))

# Print the sum of 'x' and 'y'. The '+' operator adds the values of 'x' and 'y' together.
print(x + y)
