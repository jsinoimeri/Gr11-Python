#                   By: Jeton Sinoimeri
#                 Date: December 2, 2009
# This program calculates the approximation of pi according to the number of points
# the user inputs

import random
pi = 0
prev_num=1
out = ""

for four_times in range(4):
    
    num = int(raw_input("Enter a number: "))
    
    while num < prev_num:
        num = int(raw_input("Enter a bigger number than previous: "))
    
    for num_times in range(prev_num,num+1):
        
        x = random.random()
        y = random.random()
        
        # in order to save cpu usage, I did not do the square root since 1**2 is still 1
        dis_xy = x*x+y*y
        
        if dis_xy <= 1:
            pi += 1
       
    aprox_pi = (pi/(num*1.0))*4
    
    out += "Mone Carlos method with %i points guessed that pi = %0.9f " %(num, aprox_pi)+"\n"
    prev_num = num+1

print out