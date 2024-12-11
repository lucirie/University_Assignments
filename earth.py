# Calculate the circum of the earth, using a stick's shadow

# def functions

def enviroment():
    date = input('Is your date between March 20th and September 23rd? (y or n)')
    # check if date is correct (required time-period)
    if date != 'y' or date != 'n':
        print('--> Please enter y or n')
    elif date == 'n':
        print('--> Please wait for the requested date.')
        return 0
    print('--> Instructions: On flat sand or dirt, place your one-meter stick. Measure the lenght of the shadow.')
    try:
        length = float(input('What is the length: '))
        distance = float(input('How far is the closest city to you in kms: '))
        # calculate_circum(length, distance)
    except ValueError:
        print('--> Please enter a number')
        return 0
