import sys
import os
import linecache
import itertools
import fileinput
import re

with open('./input_files/vfpprod_fix/sigrun_march2019.vfp', 'r+') as vfp_file:

    vfp_string = vfp_file.read()

    regex = r'''
    \b \d+ \.? \d* \b
    '''
    p = re.compile(regex, re.DOTALL | re.VERBOSE | re.MULTILINE)

    fbhp_list = p.findall(vfp_string)

    for item in fbhp_list:
        item = float(item)

    print(max(fbhp_list))

# test comment