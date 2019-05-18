import os

# Note: Windows accepts forward slashes just fine for the path separator. This eliminates the need to use raw strings.

print (dir(os))                         #prints all methods/attributes of an object/module

print(os.getcwd())                      #get current working directory

os.chdir('Z:/Private/nabm/python')      #change directory

print(os.getcwd())

print(os.listdir())                     #returns a list of files and folders in a directory

os.mkdir('dir1')                        #creates 1 directory only
os.makedirs('dir2/subdir')              #creates subdirectories as well. corey prefers os.makedirs() over os.mkdir()

os.rename('dir1', 'dir3')               #rename files/directories
os.rename('dir2/subdir',
          'dir2/subdir-new')

os.rmdir('dir3')                        #removes 1 (empty) directory only. corey prefers this over os.removedirs()
os.removedirs('dir2/subdir-new')        #removes subdirectories as well.


