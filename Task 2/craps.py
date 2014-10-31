#                   By: Jeton Sinoimeri
#                 Date: November 27, 2009
# This program generates 12 different numbers like rolling a die and adds them up
# This program is a boot-leg version of the Casino game Craps

import random

play = raw_input("Do you wish to play (y/n): ")

while play == "y":
    
    roll_1 = random.randint(1,6)
    roll_2 = random.randint(1,6)
    sum = roll_1 + roll_2
    
    if sum == 2 or sum == 3 or sum == 12:
        print "Roll: %i  %i  --> LOSS!" %(roll_1, roll_2)
    
    elif sum == 7 or sum == 11:
        print "Roll: %i  %i  --> WIN!" %(roll_1, roll_2)
    
    else:
        point = sum
        score = 0
        print "Roll: %i  %i  --> point is now %i" %(roll_1, roll_2, point)
        
        while score == 0:
            
            roll_1 = random.randint(1,6)
            roll_2 = random.randint(1,6)
            sum = roll_1 + roll_2
            
            if sum == point:
                print "Roll: %i  %i  --> WIN!" %(roll_1, roll_2)
                score +=1
            
            elif sum != 7:
                print "Roll: %i  %i  --> still safe" %(roll_1, roll_2) 

            elif sum == 7:
                print "Roll: %i  %i  --> LOSS!" %(roll_1, roll_2)
                score -=1
    
    print ""
    play = raw_input("Play again (y/n): ")
    print ""

print "You have quit!"