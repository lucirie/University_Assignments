import math

def hypotenuse(x, y):
    if x > 0 and y > 0: # Checks for negative numbers
        sides = x**2 + y**2
        sqrt = math.sqrt(sides) 
        return round(sqrt, 2) 
    return 'Please enter correct input. Only non-negative numbers allowed.' # Error message
try:
    x = float(input('Please input first length: '))
    y = float(input('Please input second length: '))
    print(hypotenuse(x, y))
except ValueError: # Checks for correct number input
    print('Please enter correct input. Only numbers allowed.')

