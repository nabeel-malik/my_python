import os
from datetime import datetime           # used later in os.stat() explanation

# Note: Windows accepts forward slashes just fine for the path separator. This eliminates the need to use raw strings.


print('\n######### 1. dir() FUNCTION, AND os.getcwd(), os.chdir() and os.listdir() METHODS FROM OS LIBRARY #########\n')

print(dir(os), '\n')                    # prints all methods/attributes of an object/module

print(os.getcwd())                      # get current working directory (cwd)
os.chdir('work_directory/OS_module')    # change directory
print(os.getcwd())
print()

print(os.listdir())                     # returns a list of files and folders in a directory (default = current)


print('\n############################# 2. MAKING, RENAMING, AND REMOVING DIRECTORIES #############################\n')

print("No output is being returned for these methods. View code.\n")

# making directories inside cwd
os.mkdir('dir1')                        # creates 1 directory only
os.makedirs('dir2/subdir')              # creates subdirectories as well. corey prefers os.makedirs() over os.mkdir()

# renaming directories
os.rename('dir1', 'dir3')               # rename files/directories
os.rename('dir2/subdir',
          'dir2/subdir-new')

# removing directories
os.rmdir('dir3')                        # removes 1 (empty) directory only. corey prefers this over os.removedirs()
os.removedirs('dir2/subdir-new')        # removes subdirectories as well.

print('\n########################################## 3. os.stat() METHOD ##########################################\n')

print(os.stat('demo.txt'))              # print out some file information (output can look like gibberish)
print(os.stat('demo.txt').st_size)      # print out 'size' (in bytes) attribute
print(os.stat('demo.txt').st_mtime)     # print out 'last modification time' attribute -> returns timestamp

# to return last modified time (st_mtime attribute) in a human readable form
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

print('\n########################################## 4. os.walk() METHOD ##########################################\n')

""" os.walk() traverses through a directory tree either top-down (default) or bottom-up, rooted at the directory 
provided as the argument, and for each directory in the tree, it yields a 3-tuple (dirpath, dirnames, filenames). """

print(os.getcwd())
os.chdir('../..')
print(os.getcwd())
print()

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current path:\t', dirpath)
    print('Directories:\t', dirnames)
    print('Files:\t\t\t', filenames)
    print()

print('\n########################################## 5. os.path METHODS ##########################################\n')

""" 
os.path() is used for common pathname manipulations
https://docs.python.org/2/library/os.path.html
"""

print(dir(os.path))         # print all methods/attributes available in the os.path module
print()

print(os.getcwd())
os.chdir('work_directory/OS_module')
print(os.getcwd())
print()

file_path = os.path.join(os.getcwd(), 'newfile.txt')       # joins one or more path components 'intelligently'
print(file_path)
print()

my_path = 'Z:/python/code/my_python/pybook/work_directory/OS_module/demo.txt'       # change path if and when needed.
print('my_path:\t\t\t\t\t\t', my_path)

print('os.path.basename(my_path)\t\t', os.path.basename(my_path))
print('os.path.dirname(my_path)\t\t', os.path.dirname(my_path))
print('os.path.split(my_path)\t\t\t', os.path.split(my_path))
print('os.path.exists(my_path)\t\t\t', os.path.exists(my_path))
print('os.path.isdir(my_path)\t\t\t', os.path.isdir(my_path))
print('os.path.isfile(my_path)\t\t\t', os.path.isfile(my_path))
print('os.path.splitext(my_path)\t\t', os.path.splitext(my_path))







