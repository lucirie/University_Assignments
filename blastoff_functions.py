import time

def get_countup(prompt):
    try:
        i = int(input(prompt))
        if i >= 0:
            return 'Please input a negative integer.'
        else:
            return i
    except ValueError:
        return 'Incorrect input.'

def blastoff(i):
    if i >= 0:
        print('Blastoff!!')
    else:
        print(i)
        time.sleep(1)
        blastoff(i + 1)
