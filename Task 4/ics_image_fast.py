# credits for fast string <-> unicode lookups go to http://www.python.org/doc/essays/list2str/

import pygame
import array
import time

__g = {0: None}

pygame.init()

class Surface():
    def __init__(self, path):
        '''
        Surface.__init__(self, path) --> None
        
        Starts up Surface object, if the passed path is a list or a tuple, then 
        a new Surface is created. Else, it will try to load an image from the
        local computer at the given path.
        
        If a pygame.Surface is passed, it will use it as the image. (Though, most
        probably do not know how to, so do not worry about this last statement)
        '''
        
        if type(path) == list or type(path) == tuple:
            self.image = pygame.Surface(path)
            self.image.fill((255, 255, 255))
            self.name = 'New Image (%i x %i)'
        elif type(path) == pygame.Surface:
            self.image = path
            self.name = 'Pygame Surface (%i x %i)'
        else:
            self.image = pygame.image.load(path)
            self.name = path.split('\\')[-1] + ' (%i x %i)'
        
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.text_add = []
        self.queue = []
        
        self.name = self.name %(self.width, self.height)

        self.string = pygame.image.tostring(self.image, 'RGB')
        self.pixels_rgb = array.array('B', self.string).tolist()       

def tostring(slot = 0):
    '''
    tostring(slot = 0) --> None
    
    Converts the image at the slot to a string.
    '''
    __g[slot].string = pygame.image.tostring(__g[slot].image, 'RGB')
    __g[slot].pixels_rgb = array.array('B', __g[slot].string).tolist()
    
def fromstring(string, slot = 0):
    '''
    fromstring(string, slot = 0) --> None
    
    Converts the input string to the image at the slot.
    The string length must match the dimensions of the image.
    '''
    __g[slot].string = string
    __g[slot].pixels_rgb = array.array('B', __g[slot].string).tolist()
    __g[slot].image = pygame.image.fromstring(string, (__g[slot].width, __g[slot].height), 'RGB')    
    
def fromunicode(uni_list, slot = 0):
    '''
    fromunicode(uni_list, slot = 0) --> None
    
    Converts the input list of unicode values to the image at the slot.
    The length of the list must match the dimensions of the image.
    '''
    
    __g[slot].pixels_rgb = uni_list
    __g[slot].string = array.array('B', __g[slot].pixels_rgb).tostring()
    __g[slot].image = pygame.image.fromstring(__g[slot].string, (__g[slot].width, __g[slot].height), 'RGB')
    
def image_string(slot = 0):
    '''
    image_string(slot = 0) --> string
    
    Returns the str version of the image in the slot.
    '''
    return __g[slot].string

def image_unicode(slot = 0):
    '''
    image_string(slot = 0) --> list
    
    Returns the str pixels of the image in the slot.
    '''
    return __g[slot].pixels_rgb
        
def get_width(slot = 0):
    '''
    get_width(slot = 0) --> int
    
    Returns an int equal to the width of the image in the slot in pixels.
    '''
    return __g[slot].width

def get_height(slot = 0):
    '''
    get_height(slot = 0) --> int
    
    Returns an int equal to the height of the image in the slot in pixels.
    '''
    return __g[slot].height

def get_pixel(x, y, slot = 0):
    '''
    get_pixel(x, y, slot = 0) --> list
    
    Returns the current colour values (rgb) of the pixel at the co-ordinate 
    (x, y) in the image in the slot in a 3-item list [r, g, b].
    '''
    
    x *= 3
    return __g[slot].pixels_rgb[__g[slot].width * 3 * y + x:__g[slot].width * 3 * y + x + 3]

def get_all_pixels(slot = 0):
    '''
    get_all_pixels(slot = 0) --> list
    
    Retrieves the RGB values of all pixels in the current str pixels list of the 
    image in the slot and stores them in a list of lists of 3-item lists
    [[[r, g, b], [r, g, b]], [[r, g, b], [r, g, b]]] with the length of the list
    equal to the height of the image, and the length of the lists of 3-item lists 
    equal to the width.
    
    If you are working with multiple images, try to use the load_many_images 
    function instead as it is faster.
    '''
    
    nlist = []
    height = __g[slot].height
    width = __g[slot].width
    lappend = nlist.append
    image = __g[slot]
    for y in range(height):
        lappend([])
        lappendr = nlist[y].append
        for x in range(0, width * 3, 3):
            lappendr(image.pixels_rgb[width * 3 * y + x:width * 3 * y + x + 3])
    #print len(nlist), len(nlist[0]), len(nlist[0][0])
    
    return nlist

def get_red(x, y, slot = 0):
    """
    get_red(x, y, slot = 0) --> int

    Return the red component of the pixel at position (x, y) in the image in the slot.
    """
    return __g[slot].pixels_rgb[__g[slot].width * 3 * y + x * 3]

def get_green(x, y, slot = 0):
    """
    get_green(x, y, slot = 0) --> int

    Return the green component of the pixel at position (x, y) in the image in the slot.
    """
    return __g[slot].pixels_rgb[__g[slot].width * 3 * y + x * 3 + 1]

def get_blue(x, y, slot = 0):
    """
    get_blue(x, y, slot = 0) --> int

    Return the blue component of the pixel at position (x, y) in the image in the slot.
    """
    return __g[slot].pixels_rgb[__g[slot].width * 3 * y + x * 3 + 2]

def set_red(x, y, value, slot = 0):
    """
    set_red(x, y, value, slot = 0) --> None

    Set the red component of the pixel at position (x, y) in the image in the slot
    to the given integer value.
    """
    __g[slot].pixels_rgb[__g[slot].width * 3 * y + x * 3] = value
    
def set_green(x, y, value, slot = 0):
    """
    set_green(x, y, value, slot = 0) --> None

    Set the green component of the pixel at position (x, y) in the image in the 
    slot to the given integer value.
    """
    __g[slot].pixels_rgb[__g[slot].width * 3 * y + x * 3+ 1] = value
    
def set_blue(x, y, value, slot = 0):
    """
    set_blue(x, y, value, slot = 0) --> None

    Set the blue component of the pixel at position (x, y) in the image in the slot
    to the given integer value.
    """
    __g[slot].pixels_rgb[__g[slot].width * 3 * y + x * 3 + 2] = value
        
def load_queue(rgb, slot = 0):
    '''
    load_queue(rgb, slot = 0) --> None
    
    The argument rgb must be a 3-item list [r, g, b].
    
    Prepares the queue for filling the image in the slot. Can only be used when 
    filling the entire image (once per queue_fill call). Queuing then filling is
    much faster than filling the image pixel by pixel.
    
    Unless queue_fill is called, the queue will overwrite any changes made by using
    set_pixel, or set_red/green/blue.
    
    Limitations: The queue can only be used to fill an image left to right, row by row.
    '''

    __g[slot].queue += rgb
    
def empty_queue(slot = 0):
    '''
    empty_queue(slot = 0) --> None
    
    Empties the queue list of the image in the slot.
    '''
    __g[slot].queue = []

def queue_fill(slot = 0):
    '''
    queue_fill(slot = 0) --> None
    
    Fills the image in the slot with the queued image str pixels. Only works when
    queue is full (does not including being over-full), otherwise, ValueError is
    raised.
    
    The save_image function automatically calls this function when saving the image
    if the queue is not empty, unless otherwise specified. Therefore, a call to 
    this function is usually not needed unless the you absolutely need the image
    to be ready for showing (a call to show_image before save_image).
    '''
    
    #lchr = chr
    __g[slot].string = array.array('B', __g[slot].queue).tostring()
    __g[slot].pixels_rgb = __g[slot].queue
    if len(__g[slot].string) != __g[slot].width * __g[slot].height * 3:
        raise ValueError("Expected string length of %i, got string length of %i" %(__g[slot].width * __g[slot].height * 3, len(__g[slot].string)))
    __g[slot].image = pygame.image.fromstring(__g[slot].string, __g[slot].image.get_size(), 'RGB')
    __g[slot].queue = []
    
def set_pixel(x, y, rgb, slot = 0):
    '''
    set_pixel(x, y, rgb, slot = 0) --> None
    
    The argument rgb must be a 3-item list [r, g, b].
    
    Sets the pixel at the given co-ordinate (x, y) to a colour (rgb) in the image
    in the slot. Only valid RGB values (0 <= r, g, b <= 255) will be processed
    properly, invalid values would cause the update function to raise an exception.
    '''

    x *= 3
    __g[slot].pixels_rgb[__g[slot].width * 3 * y + x:__g[slot].width * 3 * y + x + 3] = rgb
    
def save_image(filename = "temp.png", slot = 0, auto_update = True):
    '''
    save_image(filename = "temp.png", slot = 0, auto_update = True) --> None
    
    Saves an image of the image in the slot. update will be called automatically,
    unless otherwise specified by the auto_update argument or if the queue is
    not empty. Unmerged text is applied after the update/queue_fill call.
    '''
    
    if auto_update:
        if __g[slot].queue:
            queue_fill(slot)
        else:
            update(slot)
    
    #__g[slot].update()
    if __g[slot].text_add:
        for item in __g[slot].text_add:
            __g[slot].image.blit(item[2], item[:2])
            
    pygame.image.save(__g[slot].image, filename)

def update(slot = 0):
    '''
    update(slot = 0) --> None
    
    Synchronizes the current image in the slot with the str pixel version.
    It is usually unnecessary to call this function, unless the image has been
    modified and merged text is going to be added, or if you are going to call
    show_image before save_image.
    
    This function does not need to be called after calling queue_fill.
    '''
    
    __g[slot].string = array.array('B', __g[slot].pixels_rgb).tostring()
    if len(__g[slot].string) != __g[slot].width * __g[slot].height * 3:
        raise ValueError("Expected string length of %i, got string length of %i" %(__g[slot].width * __g[slot].height * 3, len(__g[slot].string)))
    __g[slot].image = pygame.image.fromstring(__g[slot].string, __g[slot].image.get_size(), 'RGB')
       
def get_fonts():
    """
    get_fonts() --> list

    Return a list of the names of the fonts (as strings) available
    on this system.  These font names may be used with add_text().
    """
    return pygame.font.get_fonts()
        
def add_text(text, x, y, rgb = [0, 0, 0], font_name = 'times new roman', size = 32, bold = False, italics = False, merged = False, slot = 0):
    """
    add_text(text, x, y, rgb = [0, 0, 0], font_name = 'times new roman', size = 32, bold = False, italics = False, merged = False, slot = 0) --> None

    Add a label with the specified text (a str) to the image in the slot.
    The top-left corner of the text will be at coordinates (x, y), and will
    be in the specified colour (a 3-part list of ints containing
    the [red, green, blue] values).
    The font_name should be one in the list returned from get_fonts(), but there
    is a built-in default font if font_name is not valid.
    The font size (an int), and bold/italics (both boolean arguments) can also
    be specified.
    If the text should be merged with the image, the boolean merged value
    should be True.  If False, the text will not be modified by any other
    pixel manipulation, and will be applied once the image is saved.

    flatten must be called after adding merged text to an image.
    """
    
    font = pygame.font.SysFont(font_name, size, bold, italics)
    text = font.render(text, 1, rgb)
    
    if slot not in __g.keys():
        raise IndexError('No image loaded at slot %i' %(slot))
    
    surface = __g.values()[slot]
    if merged:
        surface.image.blit(text, (x, y))
    else:
        surface.text_add.append([x, y, text])
            
def flatten(slot = 0):
    '''
    flatten(slot = 0) --> None
    
    "Flattens" the image in the slot. This function only needs to be called after
    adding merged text to an image. It is very slow, placing it within a loop and
    executing it every iteration will cause your program to run until next week, 
    so place it after the loop.
    '''

    if slot not in __g.keys():
        raise IndexError('No image loaded at slot %i' %(slot))
    tostring(slot)
    
## TODO: modify the 2 text thingies

def load_image(path):
    '''
    load_image(path) --> None
    
    Loads an image at the given path argument. The image will always be loaded
    at slot 0.
    
    All functions have their slot set to 0 as a default.
    '''
    
    __g[0] = Surface(path)
    global __image0
    __image0 = __g[0]
    
def load_more_images(paths):
    """
    load_more_images(paths) --> None
    
    Ideally, the paths argument must be a list. However, passing a single str or 
    a 2-item tuple (width, height) is also valid. The former would load the image 
    from its stored location, while the latter would create a new image.
    
    Passing a 2-item list, [width, height], or a 2-item tuple (width, height) as
    a list item in paths is also valid. This will result in a new, blank image
    being created. The 2-item list can only be passed when paths itself is a list.
    
    Images will always be loaded in slot 1, or greater. If there are already images
    loaded, the image will be loaded at the next available slot.
    
    Note: Images loaded by this function ALWAYS have an image number of 1, or greater
    So do not forget to change the image number when calling functions
    
    Example:
    # create the list
    paths = [[1920, 1080], 'computer.png', 'flower.png']
    
    # load the images
    load_many_images(paths) # resulting image numbers: 1, 2, 3 respectively
    
    # To edit the first pixel in the first image loaded to white, do:
    set_pixel(0, 0, [255, 255, 255], 1) # the 1 at the end is the image number
    
    load_many_images((2560 x 1440)) # would result in a new image being created,
    that is 2560px wide and 1440px tall, and its image number would be 4
    """
    k = len(__g)

    if type(paths) == str or type(paths) == tuple and len(paths) == 2:
        __g[k] = Surface(paths)
    elif type(paths) == list:
        for p in range(0 + k, len(paths) + k):
            __g[p] = Surface(paths[p-k])
            
def load_many_images(paths):
    """
    load_many_images(paths) --> None
    
    Same as load_more_images, but unloads all loaded images besides the one in slot 0.
    """
    
    lpop = __g.pop
    
    for k in __g.keys()[1:]:
        lpop(k)
    
    if type(paths) == str or type(paths) == tuple and len(paths) == 2 and type(paths[0]) == int:
        __g[1] = Surface(paths)
    elif type(paths) == list:
        for p in range(1, len(paths) + 1):
            __g[p] = Surface(paths[p-1])

def new_image(width, height):
    '''
    new_image(width, height) --> None
    
    Creates a new image with the given width and height, the image will be loaded
    in slot 0.
    '''
    load_image([width, height])
    #image = Surface((width, height))
    #return image
    
def unload_images(retain_slots = -1):
    '''
    unload_images(retain_slots = -1) --> None
    
    Unloads all images except those that are to be retained. Passing a 0 would
    result in slot 0 being retained, and passing a 1 would result in slot 0 and 1
    being retained, so on and so forth.
    
    new_image, load_image, load_more_images, or load_many_images must be called 
    before any other function calls can be made.
    '''
    
    keys = __g.keys()
    keys.sort()
    keys = keys[retain_slots + 1:]
    
    lpop = __g.pop
    for k in keys:
        lpop(k)
    
    if len(__g) == 0:
        __g[0] = None
    
def get_loaded_images():
    '''
    get_loaded_images() --> list
    
    Returns a list of all the names of loaded images. The first value will be 
    None if an image has not been loaded at slot 0.
    '''
    keys = __g.keys()
    keys.sort()
    images = []
    for k in __g.keys():
        if __g[k] != None:
            images.append(__g[k].name)
        else:
            images.append(None)
    return images

def get_image_at(slot = 0):
    '''
    get_image_at(slot = 0) --> str
    
    Gets the name of the image loaded in the slot. If no image is loaded, then
    None will be returned.
    '''
    if slot not in __g.keys() or __g[slot] == None:
        return None
    return __g[slot].name

def show_image(audio_file = None, slot = -1):
    """
    show_image(audio_file = None, slot = -1) --> None

    Display the loaded images in a window. The calling code will pause until
    the image window is closed. If an audio file argument (a str) is passed,
    that audio file will be played while the image is showing.
    
    Use the left and right arrow keys to change between images, if more than one
    is loaded.
    
    Pass a slot to lock the show_image function to that image only, an invalid slot
    number will lock the image to slot 0.
    
    Note: Since pygame MP3 support is limited, your program can crash if a MP3 is
    being loaded.
    """
    
    pygame.display.init()
    keys = __g.keys()
    keys.sort()
    
    if __g[0] == None:
        keys.pop(0)
    if len(keys) == 0:
        return
    
    if slot > -1 and slot in keys:
        keys = [slot]
    
    screen = pygame.display.set_mode(__g[keys[0]].image.get_size())
    pygame.display.set_caption(__g[keys[0]].name)
    cur_img = keys[0]
    cur_pos = 0
    
    for k in keys:
        __g[k].image = __g[k].image.convert()
    
    if audio_file and type(audio_file) == str:
        pygame.mixer.init()
        
        if '.mp3' in audio_file.lower():
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play(-1)
        else:
            sample = pygame.mixer.Sound(audio_file)
            sample.play(-1)
            
    clock = pygame.time.Clock()
        
    while 1:
        clock.tick(10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.mixer.quit()
                #sample.stop()
                #pygame.mixer.music.stop()
                #pygame.display.init()
                return
            elif event.type == pygame.KEYDOWN and slot == -1:
                if event.key == pygame.K_RIGHT:
                    cur_pos += 1
                    if cur_pos >= len(keys):
                        cur_pos = 0
                    cur_img = keys[cur_pos]
                    screen = pygame.display.set_mode(__g[cur_img].image.get_size())
                    pygame.display.set_caption(__g[cur_img].name)
                elif event.key == pygame.K_LEFT:
                    cur_pos -= 1
                    if cur_pos < 0:
                        cur_pos = len(keys) - 1
                    cur_img = keys[cur_pos]
                    screen = pygame.display.set_mode(__g[cur_img].image.get_size())
                    pygame.display.set_caption(__g[cur_img].name)
            
        screen.blit(__g[cur_img].image, (0, 0))
        pygame.display.flip()
        
################################################################################
##
##     BEGINNING OF IMAGE0 DEDICATED FUNCTIONS
##
################################################################################

# some frequently used functions dedicated to the image loaded by image_load, roughly 3 ~ 5% faster than the normal ones

def get_pixel0(x, y):
    
    x *= 3
    return __image0.pixels_rgb[__image0.width * 3 * y + x:__image0.width * 3 * y + x + 3]

def load_queue0(rgb):

    __image0.queue += rgb
    
def empty_queue0():

    __image0.queue = []

def queue_fill0():
    
    #lchr = chr
    __image0.string = array.array('B', __image0.queue).tostring()
    if len(__image0.string) != __image0.width * __image0.height * 3:
        raise ValueError("Expected string length of %i, got string length of %i" %(__image0.width * __image0.height * 3, len(__image0.string)))
    __image0.image = pygame.image.fromstring(__image0.string, __image0.image.get_size(), 'RGB')
    __image0.queue = []
    
def set_pixel0(x, y, rgb):

    x *= 3
    __image0.pixels_rgb[__image0.width * 3 * y + x:__image0.width * 3 * y + x + 3] = rgb
    
def save_image0(filename = "temp.png", auto_update = True):
    
    if auto_update:
        if __image0.queue:
            queue_fill0()
        else:
            update0()
    
    #__g[slot].update()
    if __image0.text_add:
        for item in __image0.text_add:
            __image0.image.blit(item[2], item[:2])
            
    pygame.image.save(__image0.image, filename)

def update0():
    
    __image0.string = array.array('B', __image0.pixels_rgb).tostring()
    if len(__image0.string) != __image0.width * __image0.height * 3:
        raise ValueError("Expected string length of %i, got string length of %i" %(__image0.width * __image0.height * 3, len(__image0.string)))
    __image0.image = pygame.image.fromstring(__image0.string, __image0.image.get_size(), 'RGB')

################################################################################
##
##     END OF IMAGE0 DEDICATED FUNCTIONS
##
################################################################################    
    
    