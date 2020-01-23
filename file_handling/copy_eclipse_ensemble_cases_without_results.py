import os
import shutil
import time


src_dir = '//statoil.net/unix_st/Scratch/beta/nabm/beta_pred_v3_rev1_2chan_cases_2_4_fix.runs'
dst_dir = '//statoil.net/unix_st/Scratch/beta/nabm/test.runs'

os.chdir(src_dir)
print('\nCurrent directory:\t', os.getcwd(), '\n')


def exclude_patterns():
    pattern_set = set(
        [
            'Case2_*',
            'Case2c_1*',
            'Case2c_2*',
            'Case2c_f*',
            'Case4_*',
            'batch',
            '*eclipse'
        ]
    )

    return shutil.ignore_patterns(*pattern_set)


shutil.copytree(src_dir, dst_dir, ignore=exclude_patterns())

# # shutil.copytree() is used to copy a directory and its contents, recursively, to another location.
# shutil.copytree('original_files', 'renamed_files')          # Copy 'original_files' folder to 'renamed_files' folder
# print("'original_files' folder copied to 'renamed_files' folder.")
#
# os.chdir('renamed_files')
# print('\nCurrent directory:\t', os.getcwd())
#
# for f in os.listdir():
#     f_name, f_ext = os.path.splitext(f)                     # separating file name from extension into a tuple
#
#     f_title, f_course, f_num = f_name.split(" - ")          # splitting file name into a list
#
#     f_title = f_title.strip()                               # removing leading and trailing white space
#     f_course = f_course.strip()
#     f_num = f_num.strip()[1:].zfill(2)                      # [1:] used to remove '#', .zfill() used for zero-padding
#
#     new_name = '{} - {} - {}{}'.format(f_num, f_title, f_course, f_ext)
#
#     os.rename(f, new_name)
#
# print('File renaming completed.')

# os.path.join('Case2c_no-dep_*', 'eclipse')


