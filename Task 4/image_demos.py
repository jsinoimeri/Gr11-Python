from ics_image_fast import *
from math import *
from random import *


def test(w, h):
    new_image(w, h)
    for row in range(h):
        for col in range(w):
            set_pixel(col, row, [col, (col+row)/2, row])
    save_image("test_demo.bmp")
    
def flipped(file_name, boolean):
    load_image(file_name)
    if boolean == True:
        for col in range(get_width()/2):
            for row in range(get_height()):
                pix = get_pixel(col, row)
                temp = pix
                pix = get_pixel(get_width()-1-col, row) 
                set_pixel(col, row, pix)
                pix = temp
                set_pixel(get_width()-1-col, row, pix)
    else:
        for col in range(get_width()):
            for row in range(get_height()/2):
                pix = get_pixel(col, row)
                temp = pix
                pix = get_pixel(col, get_height()-1-row) 
                set_pixel(col, row, pix)
                pix = temp
                set_pixel(col, get_height()-1-row, pix)

    save_image("flipped.bmp")
    return

def rotation(file_name, angle):
    
    load_more_images(file_name)
    w = get_width(1)
    h = get_height(1)
    angle = radians(angle)

    new_width = int(hypot(w,h))
    new_height = int(hypot(w,h))
    load_more_images([[new_width, new_height]])

    angle=-angle
    for col in range(new_width):
        for row in range(new_height):            
            c1=col-new_width/2
            r1=-row+new_height/2
            c2=c1*cos(angle)-r1*sin(angle)
            r2=c1*sin(angle)+r1*cos(angle)
            col2=int(c2+w/2)
            row2=int(-r2+h/2)
            if col2>=0 and col2<w and row2>=0 and row2<h:
                pix = get_pixel(col2, row2,1)
                set_pixel(col, row, pix,2)

    save_image("e.bmp",2)

    return

            
def blended(file_name, file_name2):
    
    load_more_images(file_name)
    load_more_images(file_name2)
    width1 = get_width(1)
    height1 = get_height(1)
    width2 = get_width(2)
    height2 = get_height(2)
    
    if width1 == width2 and height1 == height2:
        for col in range(width1):
            for row in range(height1):
                pix = get_pixel(col, row, 1)
                pix2 = get_pixel(col, row, 2)
                pix[0] = (pix[0]+pix2[0])/2
                pix[1] = (pix[1]+pix2[1])/2
                pix[2] = (pix[2]+pix2[2])/2
                set_pixel(col, row, pix, 1)
        save_image("blended.bmp", 1)
    
    else:
        print "The images are different sizes"
    
    return

def grandient(width, height, starting_colour, ending_colour, vertical_horizontal):
    new_image(width, height)
    r_grad = (ending_colour[0] - starting_colour[0])/(width*1.0)
    g_grad = (ending_colour[1] - starting_colour[1])/(width*1.0)
    b_grad = (ending_colour[2] - starting_colour[2])/(width*1.0)

    
    if vertical_horizontal == False:       
        for col in range(width):
            for row in range(height):
                    
                set_pixel(col, row, [int(starting_colour[0]+r_grad*col), int(starting_colour[1]+g_grad*col), int(starting_colour[2]+b_grad*col)])
    else:
        for row in range(height):
            for col in range(width):
                    
                set_pixel(row, col, [int(starting_colour[0]+r_grad*col), int(starting_colour[1]+g_grad*col), int(starting_colour[2]+b_grad*col)])
            
    save_image("gradient.bmp")

def message(message, width, height, font):
    new_image(width, height)
    fonts = get_fonts()
    col = 0 
    row= 0
    if fonts.__contains__(font):
        font = font
    else:
        font = fonts[randint(0, len(fonts))]
    size = height/5

    for num in range(height-size):
        for letter in message:
            col+=35
            if col > width-1:
                col = 0
                row+=45

            r_pix = randint(0, 255)
            g_pix = randint(0, 255)
            b_pix = randint(0, 255)
            add_text(letter, col, row, [r_pix, g_pix, b_pix], font, size)
    save_image("message.bmp")
message("thekiller", 300, 300, "arial")

def pattern(file_name):
    load_more_images(file_name)
    w = get_width(1)
    h = get_height(1)
    angle = radians(60)

    new_width = hypot(w,h)
    new_height = hypot(w,h)
    load_more_images([[new_width, new_height]])

    for col in range(w):
        for row in range(h):            
            c1=col-w/2
            r1=-row+h/2
            c2=c1*cos(angle)-r1*sin(angle)
            r2=c1*sin(angle)+r1*cos(angle)
            col2=int(c2+new_width/2)
            row2=int(-r2+new_height/2)
            pix = get_pixel(col, row,1)
            set_pixel(col2, row2, pix,2)
    save_image("Patterns.bmp", 2)
    return
 
def random_walk(width, height, start_x, start_y):
    new_image(width, height)
    total_distance = 0
    east_west = 0
    north_south = 0
    while start_x+north_south >= 0 and start_x+north_south < width-1 and start_y+east_west >= 0 and start_y+east_west < height-1:
        random_num = randrange(1,5)
        if random_num ==1:
            east_west += 1
        elif random_num ==2:
            east_west -= 1
        elif random_num == 3:
            north_south+=1
        elif random_num == 4:
            north_south-= 1
        total_distance+=1
        if start_x+north_south > 0 and start_x+north_south < width-1 and start_y+east_west > 0 and start_y+east_west < height-1:
            set_pixel(start_x+north_south, start_y+east_west, [0,0,0])
    
    for col in range(10):
        for row in range(10):
            if start_x+col-4 > 0 and start_y+row-4 >0 and start_x+col-4 < width-1 and start_y+row-4 < height-1:
                set_pixel(start_x+col-4, start_y+row-4, [0,255,0])
            
    save_image("radom_walk.bmp")
    return total_distance
    
def random_pixels(width, height):
    new_image(width, height)
    for col in range(width):
        for row in range(height):
            set_pixel(col, row, [randint(0, 255), randint(0, 255), randint(0, 255)])
    save_image("random_pixels.bmp")
    return

def sorted_pixels(file_name, width, height):
    load_more_images(file_name)
    w = get_width(1)
    h = get_height(1)
    load_more_images([[width, height]])
    if w == width and h == height:
        pixels = []
        for col in range(w):
            for row in range(h):
                pixels += [get_pixel(col, row, 1)]
        pixels.sort()
        pos = 0
        for col in range(w):
            for row in range(h):
                set_pixel(col, row, pixels[pos], 2)
                if pos < len(pixels)-1:
                    pos +=1

        save_image("e.bmp", 2)
    else:
        print "The two images have to be the same height and width"
    return
sorted_pixels("candies.jpg", 500, 375)
                
    
