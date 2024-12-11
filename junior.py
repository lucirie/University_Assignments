# First, it is a good rule of thumb to NEVER trust a user's input.
# Thus, we will first ensure that we recieve only numbers.

def get_num(prompt):
    try:
        n = float(input(prompt))
        return n
    except ValueError: # We can use a try-except to catch non-floating point numbers
        return 'Error. Please input a number.'

def divide_num(i, n):
    if n == 0:
        # Here, we re-prompt the user and allow them to devide by a new number
        o = get_num('Cannot devide by zero. Please input a non-zero number: ')
        print(f"{i} devided by {o} is {i / o}")
    else:
        print(f"{i} devided by {n} is {i / n}")



number1 = get_num("Input the divident: ")
number2 = get_num("Input the divisor: ")
answer = divide_num(number1, number2)
