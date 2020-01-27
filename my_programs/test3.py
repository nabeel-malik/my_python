import os
from shutil import copytree, ignore_patterns
import time
import glob

import fnmatch
from os.path import isdir, join
from shutil import copytree


# This is simply a function that calls glob.glob() but returns the results in a formatted form for readability.
def glob_results(pattern_string):
    my_list = glob.glob(pattern_string)
    print('Pattern string:\t\t', pattern_string)
    print('Matched list:\t\t', my_list)
    print('Length of list:\t\t', len(my_list))
    print()


src_dir = 'work_directory/test2/src'

os.chdir(src_dir)

# glob.glob() will search in the current working directory (CWD)
glob_results('case?')                   # 2 matches for all directories that match case? in the CWD
glob_results('case?/*')                 # 8 matches for all files and directories inside case? (1 level below case?)
glob_results('case?/**')                # same result as above
glob_results('case?/*/*')               # 22 matches for all files and directories 2 levels below case?
glob_results('case?/**/*')              # same result as above

print('\n\n')

glob_results('*.DATA')                  # 0 matches because there are no *.DATA files in the CWD
glob_results('case?/*/*.DATA')          # 2 matches for the *.DATA files 2 levels below case?
glob_results('case?/*/include')         # 2 matches for the 'include' directories 2 levels below case?
glob_results('case?/*/include/*')       # 34 matches for all files and directories inside the 'include' directories
                                        # 2 levels below case?
