from random import *
from os import *
from os.path import *
from time import *

def sublist(list_values, number):
    '''
    Takes 2 arguments: a list and an integer. Prints a sublist of the orginal list.
    Length of list is the integer. The sublist contains random values inside the 
    orginal list.
    '''
    sub = []
    list_copy = []
    list_copy += list_values
    for num_times in range(number):
        pos = randint(0,len(list_copy)-1)
        sub += [list_copy[pos]]
        list_copy.remove(list_copy[pos])
    print sub
    return

def get_files(path, file_extension):
    '''
    Takes two arguments: absolute path of directory and file_extension. Gets all 
    the files in the directory and sorts them in aplhabetical order regardless of
    the casing.
    '''
    files = []
    files2 = []
    if isdir(path):
        dir_list = listdir(path)
        
        for pos in range(len(dir_list)):
            if dir_list[pos][-len(file_extension):] == file_extension:
                files += [dir_list[pos]]
        for each_file in files:
            files2 += [each_file.upper()]

        files2.sort()
        pos = 0
        pos2 = 0
        while pos2 < len(files2):
            if files2[pos2] == files[pos].upper():
                files2[pos2] = files[pos]
                pos2 += 1
            pos+=1

        return files2          
    
    else:
        return files
    
    return

def avg_accessed(path):
    '''
    Takes 1 agrument: absolute path of a directory. Gets all the files and directories
    in that path. For each file/directory, it finds the last accessed time and 
    adds it up. Returns the average last accessed time for that absolute path
    directory.
    '''
    if isdir(path):
        list_dir = listdir(path)
        total_time = 0
        for files_dir in list_dir:
            total_time += getatime(files_dir)
        avg_time = ctime(total_time/float(len(list_dir)))
        return avg_time
    else:
        return "Directory does not exist."
    return

def spy(path):
    '''
    Takes 1 argument: absolute path of a directory. Gets all the files and directories
    in that path. For each file/directroy, it adds up the last modified time.
    Sleeps for 45 seconds, recalculates last modified times. If different, prints
    a statement. If same does nothing.
    '''
    if exists(path):
        while 0 == 0:
            orginal_time = 0
            secondary_time = 0

            list_dir = listdir(path)
            for files_dir in list_dir:
                orginal_time += getmtime(path +"\\" + files_dir)
            
            sleep(45)
            list_dir = listdir(path)
            for files_dir in list_dir:
                secondary_time += getmtime(path +"\\" + files_dir)
            
            if secondary_time > orginal_time or secondary_time < orginal_time:
                print "A change has occured in %s." %(path)
    else:
        print "Enter a valid directory"
    return
