from ics_image_fast import *
from random import *
from math import *

def inverse(file_name):
    '''
    Takes the picture user inputs and inverses it by substracting each rgb value
    from 255. For ex: red is 55, the inverse of that is 255-55 = 200
    '''
    load_image(file_name) #loads the image
    for row in range(get_height()):
        for col in range(get_width()):
            pix = get_pixel(col, row)
            pix[0] = 255 - pix[0] # this inverses the red value by subracting the red value from 255
            pix[1] = 255 - pix[1] # this inverses the green value by subracting the green value from 255
            pix[2] = 255 - pix[2] # this inverses the blue value by subracting the blue value from 255
            set_pixel(col, row, pix)
    save_image("inverse.bmp")
    return

def flipped(file_name, flip_horizontal):
    '''
    Takes the picture user inputs it and flips it horizontal or vertical according
    to the user. It gets two pixels from the first half and second half of the image
    and swaps them around.
    '''
    load_image(file_name)
    width = get_width()
    height = get_height()
    
    #flips it vertically
    if flip_horizontal == False:
        for col in range(width/2):
            for row in range(height):
                pix = get_pixel(col, row) # gets pixels in first half of picture
                temp = pix # stores pixel in temp
                pix = get_pixel(width-1-col, row) # gets pixels in second half of picture
                set_pixel(col, row, pix) # sets pixels of second half to first half of picture
                set_pixel(width-1-col, row, temp) # sets pixels of fist half to second half of picture
    
    # flips it horizontally
    elif flip_horizontal == True:
        for col in range(width):
            for row in range(height/2):
                pix = get_pixel(col, row)
                temp = pix
                pix = get_pixel(col, height-1-row) 
                set_pixel(col, row, pix)
                set_pixel(col, height-1-row, temp)

    save_image("flipped.bmp")
    return

def mirrored(file_name, horizontal):
    '''
    Exactly like flipped except instead of swapping, it replaces the pixel with
    the same pixel but on the other half of the image. It mirrors horizontal and
    vertical according to the user.
    '''
    load_image(file_name)
    
    # mirrors the image vertically
    if horizontal == False:
        for col in range(get_width()/2):
            for row in range(get_height()):
                pix = get_pixel(col, row) # gets pixels in first half of picture
                set_pixel(get_width()-1-col, row, pix) # sets pixels of fist half to second half of the picture
    
    # mirrors the image horizontally
    elif horizontal == True:
        for col in range(get_width()):
            for row in range(get_height()/2):
                pix = get_pixel(col, row)
                set_pixel(col, get_height()-1-row, pix)

    save_image("mirored.bmp")
    return

def greyscale(file_name):
    '''
    Takes an image, gets a pixel one at a time, adds the rgb values and divides
    by 3. Sets the pixel at the same place but with the average as the rgb value.
    '''
    load_image(file_name)
    for row in range(get_height()):
        for col in range(get_width()):
            pix = get_pixel(col, row)
            avg = (pix[0]+ pix[1]+pix[2])/ 3 #finds the average pixel num
            pix[0] = avg # replaces the red value with average num
            pix[1] = avg # replaces the green value with average num
            pix[2] = avg # replaces the blue value with average num
            set_pixel(col, row, pix)
    save_image("greyscale.bmp")
    return

def blended(file_name, file_name2):
    '''
    Takes two images. Gets a pixel from the two images, adds the two rgb values 
    together and divides by two. Sets the new rgb value at that position in the
    first image.
    '''
    load_more_images(file_name)
    load_more_images(file_name2)
    width1 = get_width(1)
    height1 = get_height(1)
    width2 = get_width(2)
    height2 = get_height(2)
    
    if width1 == width2 and height1 == height2: # makes sure that the two images are the same size
        for col in range(width1):
            for row in range(height1):
                pix = get_pixel(col, row, 1) # gets pixels of first image
                pix2 = get_pixel(col, row, 2) # gets pixels of second image
                pix[0] = (pix[0]+pix2[0])/2 # adds the two red values and finds the average
                pix[1] = (pix[1]+pix2[1])/2 # adds the two green values and finds the average
                pix[2] = (pix[2]+pix2[2])/2 # adds the two blue values and finds the average
                set_pixel(col, row, pix, 1) # sets the new pixels to the first image
        save_image("blended.bmp", 1)
    
    else:
        print "The images are different sizes"
    
    return
blended(r"C:\Users\Jeton\Pictures\Soccer\german flag.jpg", r"C:\Users\Jeton\Pictures\Cars\mercedes_slr.jpg" )

def message(message, width, height, font, num_times):
    '''
    Makes a new image, with the width and height provided. Each letter inside of 
    the message is add by randomly gernerated positons (x,y) and colours. The size
    is 1/4 of the height and the font is inputed by the user, as well as the number
    of times the message should appear in the image.
    '''
    new_image(width, height)
    fonts = get_fonts() # gets all the fonts on computer
    if fonts.__contains__(font): # makes sure the font user input is a valid font
        font = font
    else:
        font = fonts[randint(0, len(fonts))] # if not randomly generates a font to use
    size = height/4
    
    for num in range(num_times):
        for letter in message:
            message_x = randint(0, width-size) # random position of letter on x-axis
            message_y = randint(0, height-size) # random position of letter on y-axis
            r_pix = randint(0, 255) # randomly generated red value
            g_pix = randint(0, 255) # randomly generated green value
            b_pix = randint(0, 255) # randomly generated blue value
            
            add_text(letter, message_x, message_y, [r_pix, g_pix, b_pix], font, size)
    save_image("message.bmp")
    return

def random_walk(width, height, start_x, start_y):
    '''
    This function makes a new image with width and height provided by user. Places
    a 9 by 9 green square at the starting x and y positions. Randomly generates
    a number between 1 and 4, and adds or substracts 1 from the starting x and y
    positions. Sets a black pixel at that newly calculated posion in the image. 
    It will only stop if the pixels touch one of the borders.
    '''
    new_image(width, height)
    total_distance = 0
    east_west = 0
    north_south = 0
    while start_x+north_south >= 0 and start_x+north_south < width-1 and start_y+east_west >= 0 and start_y+east_west < height-1: 
        random_num = randrange(1,5)
        if random_num == 1:
            east_west += 1 # adds 1 if moving east
        
        elif random_num == 2:
            east_west -= 1 # substracts 1 if moving west
        
        elif random_num == 3:
            north_south += 1 # adds 1 if moving north
        
        elif random_num == 4:
            north_south -= 1 # substracts 1 if moving south
        
        total_distance += 1
        if start_x+north_south > 0 and start_x+north_south < width-1 and start_y+east_west > 0 and start_y+east_west < height-1: # makes sure the the pixel is not at border
            set_pixel(start_x+north_south, start_y+east_west, [0,0,0])
    
    for col in range(10):
        for row in range(10):
            if start_x+col-4 > 0 and start_y+row-4 >0 and start_x+col-4 < width-1 and start_y+row-4 < height-1: # puts a 9*9 square on the start point
                set_pixel(start_x+col-4, start_y+row-4, [0,255,0]) # makes the start-point the center of the square
            
    save_image("radom_walk.bmp")
    return total_distance

def gradient(width, height, starting_colour, ending_colour, vertical_horizontal):
    '''
    A colour transition between two colours that user inputs. The transition will
    occur horizontal or vertical according to the user input.
    '''
    new_image(width, height)
    r_grad = (ending_colour[0] - starting_colour[0])/(width*1.0) # finds how much red value should increase
    g_grad = (ending_colour[1] - starting_colour[1])/(width*1.0) # finds how much green value should increase
    b_grad = (ending_colour[2] - starting_colour[2])/(width*1.0) # finds how much blue value should increase
    
    # vertical
    if vertical_horizontal == False:       
        for col in range(width):
            for row in range(height):
                # sets the pixel at col, row with the newly calculated rgb value    
                set_pixel(col, row, [int(starting_colour[0]+r_grad*col), int(starting_colour[1]+g_grad*col), int(starting_colour[2]+b_grad*col)])
    
    # horizontal
    elif vertical_horizontal == True:
        for row in range(height):
            for col in range(width):
                    
                set_pixel(row, col, [int(starting_colour[0]+r_grad*col), int(starting_colour[1]+g_grad*col), int(starting_colour[2]+b_grad*col)])
            
    save_image("gradient.bmp")
    return


# my own functions

# new image functions
def random_pixels(width, height):
    '''
    Makes a new image with width and height provided by user. Randomly generates
    the rgb values and puts them inside the image, covering the image with multi
    coloured pixels.
    '''
    new_image(width, height)
    for col in range(width):
        for row in range(height):
            set_pixel(col, row, [randint(0, 255), randint(0, 255), randint(0, 255)]) # set pixels at col, row with randomly generated rgb values
    save_image("random_pixels.bmp")
    return

def sorted_pixels(file_name, width, height):
    '''
    Loads an image, gets all the pixels from the image and sorts them. Makes a
    new image according to user input and sets the sorted pixels in the new image.
    The image created is a type of water fall with different colours.
    '''
    load_more_images(file_name)
    w = get_width(1)
    h = get_height(1)
    load_more_images([[width, height]])
    if w == width and h == height:
        pixels = []
        for col in range(w):
            for row in range(h):
                pixels += [get_pixel(col, row, 1)] # gets all pixels from first image
        pixels.sort()
        pos = 0
        for col in range(w):
            for row in range(h):
                set_pixel(col, row, pixels[pos], 2) # sets all pixels after sorting
                if pos < len(pixels)-1:
                    pos +=1

        save_image("sorted_pixels.bmp", 2)
    else:
        print "The two images have to be the same height and width"
    return

#image modifiers
def pattern(file_name):
    '''
    Loads an image. Creates a new image with the max width and height of the loaded
    image. Converts the coordinates of the pixels in the loaded image to cartesian
    plane coordinates, rotates it 60 degrees and converts the new coordinates to 
    coordinates for an image. Sets the pixel in the new image with the newly 
    calculated coordinates. User will notice the new image with a pattern of white
    pixels on it.
    '''
    load_more_images(file_name)
    w = get_width(1)
    h = get_height(1)
    angle = radians(60)

    new_width = hypot(w,h)
    new_height = hypot(w,h)
    load_more_images([[new_width, new_height]])

    for col in range(w):
        for row in range(h):            
            c1 = col-w/2 # converts col,row to cartesian plane coordinates
            r1 = -row+h/2
            c2 = c1*cos(angle)-r1*sin(angle) # rotates the image
            r2 = c1*sin(angle)+r1*cos(angle)
            col2 = int(c2+new_width/2) # finds the new image coordinates
            row2 = int(-r2+new_height/2)
            pix = get_pixel(col, row,1)
            set_pixel(col2, row2, pix,2)
    save_image("Patterns.bmp", 2)
    return

def rotation(file_name, angle):
    '''
    Loads an image. Creates a new image with the max width and height of the loaded
    image. Converts the coordinates of the pixels in the loaded image to cartesian
    plane coordinates, rotates it x-amount of degree and converts the new coordinates 
    to coordinates for an image. Sets the pixel in the new image with the newly 
    calculated coordinates. User will notice the new image rotated that many
    degrees as he/she inputed.
    '''
    load_more_images(file_name)
    w = get_width(1)
    h = get_height(1)
    angle = radians(angle)

    new_width = int(hypot(w,h))
    new_height = int(hypot(w,h))
    load_more_images([[new_width, new_height]])

    angle = -angle # rotates it backwards
    
    for col in range(new_width):
        for row in range(new_height):            
            
            c1=col-new_width/2 # converts col,row to cartesian plane coordinates
            r1=-row+new_height/2
            c2=c1*cos(angle)-r1*sin(angle) # rotates the image
            r2=c1*sin(angle)+r1*cos(angle)
            col2=int(c2+w/2) # finds the new image coordinates
            row2=int(-r2+h/2)
            
            if col2 >= 0 and col2 < w and row2 >= 0 and row2 < h:
                pix = get_pixel(col2, row2,1)
                set_pixel(col, row, pix,2)

    save_image("rotation.bmp", 2)
    return
