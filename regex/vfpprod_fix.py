import sys
import os
import linecache
import itertools
import fileinput
import re

with open('./input_files/vfpprod_fix/sigrun_march2019.vfp', 'r+') as vfp_file:

    vfp_string = vfp_file.read()

    regex = r'''
    (\b \d+) \* (\d+\.?\d+ \b)
    '''
    p = re.compile(regex, re.DOTALL | re.VERBOSE | re.MULTILINE)

    counter = 0

    while p.search(vfp_string): # Match objects always have a BOOLEAN value of TRUE. Since match() and search() return
            # 'NONE' when there is no match, you can test whether there was a match with a simple IF/WHILE statement.

        #print(p.search(vfp_old_string))

        counter = counter + 1 #increment the counter to count number of matches found and substituted.

        multiplier = int(p.search(vfp_string).group(1))

        vfp_string = p.sub('\g<2> ' * multiplier, vfp_string, 1)

    vfp_string = vfp_string.replace('  ', ' ') #removing all the double spaces resulting from substitution.

    print(f'{counter} matches found and replaced.')

output_file = open('./input_files/vfpprod_fix/sigrun_march2019_updated.vfp', 'w')
output_file.write(vfp_string)

'''
Note how the WHILE loop is used to recursively go through text file and make 1 substitution at a time by setting the
COUNT argument of the sub() method to 1.
'''
