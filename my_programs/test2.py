import os
from shutil import copytree, ignore_patterns
import time
import glob

# https://christophergs.github.io/python/2017/01/01/python-glob/
# https://pymotw.com/2/glob/

# from fnmatch import fnmatch, filter
import fnmatch
from os.path import isdir, join
from shutil import copytree


def ignore_pattern_paths(src, *patterns):
    """Function that can be used as copytree() ignore parameter. Patterns is a sequence of glob-style patterns that
    are used to exclude files"""

    def _ignore_pattern_paths(path, names):
        ignored_names = []
        src_length = len(src)
        for pattern in patterns:

            # splitting pattern into path AND pattern file or directory
            pattern_path = pattern.rsplit('/', 1)[0]
            pattern_filedir = pattern.rsplit('/', 1)[1]

            # creating path_end variable for fnmatch.fnmatch() later
            path_end = path.replace('\\', '/')[src_length+1:]

            # printing diagnostics
            print('path:\t\t\t\t', path.replace('\\', '/'))
            print('names:\t\t\t\t', names)
            print('path_end:\t\t\t', path_end)
            print('pattern_path:\t\t', pattern_path)
            print('pattern_filedir:\t', pattern_filedir)

            # if 'path_end' matches 'pattern_path' and directory levels, AND any of the 'names' match 'pattern_filedir'
            if fnmatch.fnmatch(path_end, pattern_path) and path_end.count('/') == pattern_path.count('/'):
                print('#################### path_end MATCHES pattern_path!! ####################\n')
                ignored_names.extend(fnmatch.filter(names, pattern_filedir))
            else:
                print()

        return set(ignored_names)

    return _ignore_pattern_paths


src_dir = 'work_directory/test2/src'
dst_dir = 'work_directory/test2/dst'

print('\nCurrent directory:\t', os.getcwd(), '\n')

copytree(
    src_dir,
    dst_dir,
    ignore=ignore_pattern_paths(src_dir, 'case?/*/*.DATA', 'case_s*/*/include'))
