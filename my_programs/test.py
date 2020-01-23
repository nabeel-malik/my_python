import os
from shutil import copytree, ignore_patterns
import time
import glob

# https://christophergs.github.io/python/2017/01/01/python-glob/

from fnmatch import fnmatch, filter
from os.path import isdir, join
from shutil import copytree

def include_patterns(*patterns):
    """Factory function that can be used with copytree() ignore parameter.

    Arguments define a sequence of glob-style patterns
    that are used to specify what files to NOT ignore.
    Creates and returns a function that determines this for each directory
    in the file hierarchy rooted at the source directory when used with
    shutil.copytree().
    """
    def _ignore_patterns(path, names):
        keep = set(name for pattern in patterns
                            for name in filter(names, pattern))
        ignore = set(name for name in names
                        if name not in keep and not isdir(join(path, name)))
        return ignore
    return _ignore_patterns


src_dir = '//statoil.net/unix_st/Scratch/beta/nabm/beta_pred_v3_rev1_2chan_cases_2_4_fix.runs'
dst_dir = '//statoil.net/unix_st/Scratch/beta/nabm/test.runs'

os.chdir(src_dir)
print('\nCurrent directory:\t', os.getcwd(), '\n')


# def ignored_files(*args):
#     total_list = [file for file in glob.glob('**/*', recursive=True)]
#     total_set = set(total_list)
#
#     copy_list_include = [file for file in glob.glob('Case2c_no-dep_???/eclipse/model/include/*', recursive=True)]
#     copy_list_data = [file for file in glob.glob('Case2c_no-dep_???/eclipse/model/*.DATA', recursive=True)]
#     copy_list = copy_list_include + copy_list_data
#     copy_set = set(copy_list)
#
#     ignore_set = total_set.difference(copy_set)
#
#     for item in ignore_set.copy():
#         if os.path.isdir(item):
#             ignore_set.discard(item)
#
#     ignore_list = sorted(ignore_set)
#
#     for item in ignore_list.copy():
#         ignore_list[ignore_list.index(item)] = '*' + item
#
#     return ', '.join(ignore_list)




# # my_list = [file for file in glob.glob('Case2c_fixedPE???/**/*', recursive=True)]
# # my_list = [file for file in glob.glob('./**/*', recursive=True)]
#
# # for i in ignored_files(src_dir):
# #     print(i)
#
# with open('ignored_files.txt', 'w+') as f:
#         f.write(ignored_files())
#
#
copytree(
    src_dir,
    dst_dir,
    ignore=include_patterns('*.DATA', '*/include/**/*'))



