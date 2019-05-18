import sys
import os
import linecache
import itertools
import fileinput
import re

with open('./inputfiles/python_challange_2_regex_pagesource/pagesource.txt', 'r+') as pagesource_file:
    pagesource_string = pagesource_file.read()

    mess_str = re.findall(r"<!--(.*?)-->", pagesource_string, re.DOTALL)[-1]
    found_str = "".join(re.findall(r"[a-zA-Z]", mess_str))
    print(found_str)

"""
NOTE. Using findall() [instead of match() or search()] has a big advantage in a case like this,
because we want to find all the occurrences of the regex, but only pick the last occurrence for further work.
"""