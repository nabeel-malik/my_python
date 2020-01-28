import os
import glob
import fnmatch

"""
glob MODULE EXPLANATION:
The glob module finds all the pathnames matching a specified pattern according to the rules used by the UNIX shell,
although results are returned in arbitrary order.

The pattern rules for glob are not regular expressions. Instead, they follow standard Unix path expansion rules.
There are only a few special characters, as follows:
    - Wildcards(*):                         An asterisk (*) matches zero or more characters in a segment of a name.
    - Single character wildcard (?):        It matches any single character in that position in the name.
    - Character ranges:                     For instance [0-9] will match a any single digit.

The API for using glob is brief, with three main methods:
glob.glob(pathname, *, recursive=False)     The main guy: Returns a LIST of pathnames depending on the search criteria
                                            passed in with “pathname”
glob.iglob(pathname, recursive=False)       Same as glob.glob, except that it returns an ITERATOR, meaning that not all
                                            values get stored in memory - so can be much more efficient.
glob.escape(pathname)                       Escapes special characters in the passed in “pathname”.

That’s it! This is a succinct yet powerful module.

Note: glob uses fnmatch under the hood (with a small difference), which is covered in the next section.

My comment: 'glob' is a very useful library to utilise for searching for files and directories. This could be simply
used by providing the UNIX style pathname patterns that are  fairly simple to understand and write.

Recommended further reading:
https://docs.python.org/2/library/glob.html
https://christophergs.github.io/python/2017/01/01/python-glob/
https://pymotw.com/2/glob/
"""


# This is simply a function that calls glob.glob() but returns the results in a formatted form for readability.
def glob_results(pattern_string, recursive=False):
    if not recursive:
        my_list = glob.glob(pattern_string)
        print('Pattern string:\t\t', pattern_string)
        print('Recursive flag:\t\t', recursive)
        print('Matched list:\t\t', my_list)
        print('Length of list:\t\t', len(my_list))
        print()
    else:
        my_list = glob.glob(pattern_string, recursive=True)
        print('Pattern string:\t\t', pattern_string)
        print('Recursive flag:\t\t', recursive)
        print('Matched list:\t\t', my_list)
        print('Length of list:\t\t', len(my_list))
        print()


src_dir = 'work_directory/ignore_pattern_paths()_function_for_copytree()/src'

os.chdir(src_dir)

print('\n################################ 1. NON-RECURSIVE SEARCH USING glob.glob() ################################\n')

# glob.glob() will search in the current working directory (CWD)
glob_results('case?')                   # 2 matches for all directories that match case? in the CWD
glob_results('case?/*')                 # 8 matches for all files and directories inside case? (1 level below case?)
glob_results('case?/*/*')               # 23 matches for all files and directories 2 levels below case?

print()

glob_results('*.DATA')                  # 0 matches because there are no *.DATA files in the CWD
glob_results('case?/*/*.DATA')          # 2 matches for the *.DATA files 2 levels below case?
glob_results('case?/*/include')         # 2 matches for the 'include' directories 2 levels below case?
glob_results('case?/*/include/*')       # 34 matches for all files and directories inside the 'include' directories
                                        # 2 levels below case?


print('\n################################## 2. RECURSIVE SEARCH USING glob.glob() ##################################\n')

"""
Starting with Python version 3.5, the glob module supports the “**” directive (which is parsed only if you pass the
recursive flag).
"""

glob_results('case?/*')                         # 8 matches for non-recursive search (same as above)
glob_results('case?/**', recursive=True)        # 69 matches for recursive search

print('\n########################################### 3. fnmatch MODULE ###########################################\n')
"""
As stated earlier, glob uses fnmatch under the hood. Keep reading for the 'difference' between glob and fnmatch.

This module provides support for Unix shell-style wildcards, which are not the same as regular expressions .
The special characters used in shell-style wildcards are:
    *       -> matches everything
    ?       -> matches any single character
    [seq]   -> matches any character in 'seq'
    [!seq]  -> matches any character not in 'seq'
    
Difference between glob and fnmatch special characters:
Note that the filename separator ('/' on Unix) is NOT special to this module. See module glob for pathname expansion 
(glob uses fnmatch() to match pathname segments). 
Similarly, filenames starting with a period are not special for this module, and are matched by the * and ? patterns.

Usage:
fnmatch.fnmatch(filename, pattern):         Tests whether the 'filename' matches the 'pattern', returning True or False.
fnmatch.fnmatchcase(filename, pattern):     Case-sensitive fnmatch.fnmatch() 
fnmatch.filter(names, pattern):             Returns a subset of the list of 'names' that match 'pattern'

"""
print(glob.glob('case1/*'))         # 4 matches only, for the files and directories 1 level below 'case1' directory.
print(fnmatch.fnmatch('case1/eclipse/case1', 'case1/*'))        # '/' is NOT a special character and is matched by '*'
print(fnmatch.fnmatchcase('Case1/eclipse/case1', 'case1/*'))    # Case-sensitive fnmatch.fnmatch()
print(fnmatch.filter(['case1/eclipse', 'case2/eclipse'], 'case1/*'))

