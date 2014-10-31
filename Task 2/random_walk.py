#                   By: Jeton Sinoimeri
#                 Date: November 30, 2009
# This program simulates the walk for a person who is very drunk from
# too much sour Red Bull

import random

north_south = 0
south = 0
north = 0
east_west = 0
west = 0
east = 0
actual_distance = 0

desired_distance = int(raw_input("How many steps do you want to go?: "))

while actual_distance < desired_distance:    
    
    steps = random.randint(1,4)    

    if steps == 1:
        north_south += 1
        north += 1

    elif steps == 2:
        north_south -= 1
        south += 1

    elif steps == 3:
        east_west += 1
        east += 1

    elif steps == 4:
        east_west -= 1
        west += 1

    actual_distance = (east_west*east_west + north_south*north_south)**0.5

print "North: %i steps \nSouth: %i steps \nEast: %i steps \nWest: %i steps" %(north, south, east, west)