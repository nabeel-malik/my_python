"""
shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False,
                dirs_exist_ok=False)

shutil.copytree() is used to recursively copy an entire directory tree rooted at src, to a directory named dst, and
return the destination directory.

shutil.ignore_patterns() is a factory function that creates a function that can be used as a callable for copytree()’s
'ignore' argument, ignoring files and directories that match one of the glob-style patterns provided.

The API for shutil.ignore_patterns() doesn't support paths, but it is trivially easy to roll your own variant by
copying the ignore_patterns() function from the shutil module and customizing it to accept glob-style pathname patterns.

I have done this, and called this new function ignore_pattern_paths().

Usage:      ignore_pattern_paths(src, *patterns)
            The 'src' argument should be the same as the 'src' argument to copytree().
            The *patterns positional arguments are glob-style (UNIX) path patterns that need to be ignored.


The following section compares the behaviour and performance of both ignore_patterns() and ignore_pattern_paths().
"""

import os
from shutil import copytree, ignore_patterns
import fnmatch
import shutil
import time


def ignore_pattern_paths(src, *patterns):
    """Function that can be used as copytree() ignore parameter. *patterns is a sequence of glob-style patterns that
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

            # printing key variables
            print('path:\t\t\t\t', path.replace('\\', '/'))
            print('names:\t\t\t\t', names)
            print('path_end:\t\t\t', path_end)
            print('pattern_path:\t\t', pattern_path)
            print('pattern_filedir:\t', pattern_filedir)

            # if 'path_end' matches 'pattern_path' and directory levels, AND any of the 'names' match 'pattern_filedir'
            # note: we have to do an additional directory levels check because '/' is not a special char. for fnmatch
            if fnmatch.fnmatch(path_end, pattern_path) and path_end.count('/') == pattern_path.count('/'):
                print('#################### path_end MATCHES pattern_path!! ####################\n')
                ignored_names.extend(fnmatch.filter(names, pattern_filedir))
            else:
                print()

        return set(ignored_names)

    return _ignore_pattern_paths


src_dir = 'work_directory/ignore_pattern_paths()_function_for_copytree()/src'
dst_dir_ignore_patterns = 'work_directory/ignore_pattern_paths()_function_for_copytree()/dst_ignore_patterns'
dst_dir_ignore_pattern_paths = 'work_directory/ignore_pattern_paths()_function_for_copytree()/dst_ignore_pattern_paths'

print('\nCurrent directory:\t', os.getcwd(), '\n')

# Remove destination directories if they already exist from previous program run.
if os.path.isdir(dst_dir_ignore_patterns):
    print('Removing previous destination directory...')
    shutil.rmtree(dst_dir_ignore_patterns)          # to remove the directory and its contents recursively
    print("'dst_dir_ignore_patterns' directory removed.\n")
if os.path.isdir(dst_dir_ignore_pattern_paths):
    print('Removing previous destination directory...')
    shutil.rmtree(dst_dir_ignore_pattern_paths)          # to remove the directory and its contents recursively
    print("'dst_dir_ignore_pattern_paths' directory removed.\n")

print('Sleeping for 10 seconds...')
time.sleep(10)                                  # adding a 10 seconds delay


print('\n############################### 1. copytree() USING ignore=ignore_patterns ###############################\n')

print('Copying tree using copytree() with ignore=ignore_patterns...')

copytree(
    src_dir,
    dst_dir_ignore_patterns,
    ignore=ignore_patterns('*.DATA', '*.INC')       # would ignore ALL *.DATA and *.INC files in ALL directories.
)

print('\n############################# 2. copytree() USING ignore=ignore_pattern_paths #############################\n')

print('Copying tree using copytree() with ignore=ignore_pattern_paths...\n')

copytree(
    src_dir,
    dst_dir_ignore_pattern_paths,
    ignore=ignore_pattern_paths(src_dir, 'case?/*/*.DATA', 'case_s*/*/include'))
