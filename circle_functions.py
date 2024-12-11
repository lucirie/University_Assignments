# first ill define a function that takes in user input (only numbers)
import math

def get_float(prompt):
    try:
        number = float(input(prompt))
        return number
    except ValueError:
        print('Incorrect value. Please input a number')

def print_circum(radius):
    circum = round(radius * math.pi * 2, 5)
    print(circum)