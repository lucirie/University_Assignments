#Inluce the defined functions
import circle_functions

for i in range(3):
    radius = circle_functions.get_float('Please Input Radius: ')
    circle_functions.print_circum(radius)