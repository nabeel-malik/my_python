import os
import shutil
import time

os.chdir('work_directory/parsing_and_renaming_of_multiple_files')
print('\nCurrent directory:\t', os.getcwd(), '\n')


if os.path.isdir('renamed_files'):
    # shutil.rmtree() is used to remove a directory and its contents, recursively.
    shutil.rmtree('renamed_files')                              # Remove previously generated 'renamed_files' folder
    print("'renamed_files' directory removed.")
    print("Sleeping for 15 seconds... \n")
    time.sleep(15)                                               # adding a 15 seconds delay

# shutil.copytree() is used to copy a directory and its contents, recursively, to another location.
shutil.copytree('original_files', 'renamed_files')          # Copy 'original_files' folder to 'renamed_files' folder
print("'original_files' folder copied to 'renamed_files' folder.")

os.chdir('renamed_files')
print('\nCurrent directory:\t', os.getcwd())

for f in os.listdir():                          # returns a list of files and folders in a directory (default = current)
    f_name, f_ext = os.path.splitext(f)                     # separating file name from extension into a tuple

    f_title, f_course, f_num = f_name.split(" - ")          # splitting file name into a list

    f_title = f_title.strip()                               # removing leading and trailing white space
    f_course = f_course.strip()
    f_num = f_num.strip()[1:].zfill(2)                      # [1:] used to remove '#', .zfill() used for zero-padding

    new_name = f'{f_num} - {f_title} - {f_course}{f_ext}'

    os.rename(f, new_name)

print('File renaming completed.')
