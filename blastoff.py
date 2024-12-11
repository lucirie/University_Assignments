import blastoff_functions

countup = blastoff_functions.get_countup('How many seconds till flight? ')

# Check if countup is an integer before calling blastoff
if isinstance(countup, int):
    blastoff_functions.blastoff(countup)
else:
    print(countup)  # Print the error message returned by get_countup
