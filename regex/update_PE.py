import sys
import os
import linecache
import itertools
import fileinput
import re

with open('./input_files/update_PE/PREDICTION19_NFA.INC', 'r+') as sch_file:
    sch_str = sch_file.read()

    with open('./input_files/update_PE/PE_file.txt', 'r+') as pe_file:
        for line in pe_file:
            pe_list = line.rstrip().split(" ")
            date = "\s".join(pe_list[0:3])
            pe = "".join(pe_list[3])

            regex = r"""
            (^DATES[^\d.]+?""" + date + """.+?GEFAC.+?JP\s)         #Group1 - String from DATES through JP\s
            (.+?)                                                   #Group2 - JP PE
            ({\*}%PEMULT%)                                          #Group3 - %PEMULT% Modifier
            (.+?)                                                   #Group4
            (JI\s)                                                  #Group5
            (.+?)                                                   #Group6 - JI PE
            ({\*}%PEMULT%)                                          #Group7 - %PEMULT% Modifier
            (\s/)                                                   #Group8 - Trailing " /"
            """

            p = re.compile(regex, re.DOTALL | re.VERBOSE | re.MULTILINE)
            sch_str = p.sub('\g<1>' + pe + '\g<3>\g<4>\g<5>' + pe + '\g<7>\g<8>', sch_str)

output_file = open('./input_files/update_PE/out.INC', 'w')
output_file.write(sch_str)

