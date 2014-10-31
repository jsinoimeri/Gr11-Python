#                   By: Jeton Sinoimeri
#                 Date: November 28, 2009
# This program generates a picture for the user using these characters "#", "+", "O", " "
# Then it will print the picture according to the length and width provided by the user

def build_pic(z):

    text = ""
    
    while len(text) < z:
        
        pixel = random.randint(1,10)

        if pixel <= 4:
            text+= "#"

        elif pixel <= 7:
            text+= "+"

        elif pixel <= 9:
            text += "O"

        else:
            text += " "
    return text

def print_picture(w, x, z):
    
    pound = 0
    big_o = 0
    plus = 0
    space = 0
    pic = ""
    
    for pos in range(z):
        
        pic += w[pos]
        
        if pos%x == x-1:
            print pic
            pic = ""        

        if w[pos] == "#":
            pound += 1

        elif w[pos] == "+":
            plus += 1

        elif w[pos] == "O":
            big_o += 1
        
        else:
            space +=1
    
    print "\n'#' = %0.2f%% \n'+' = %0.2f%% \n'O' = %0.2f%% \n' ' = %0.2f%%" %(100*(pound /(z*1.0)), 100*(plus /(z*1.0)), 100*(big_o /(z*1.0)), 100*(space /(z*1.0)))
    return

import random    

length = int(raw_input("Length please: "))
width = int(raw_input("Width please: "))

area = length*width
text2 = build_pic(area)

print ""
print_picture(text2, length, area)