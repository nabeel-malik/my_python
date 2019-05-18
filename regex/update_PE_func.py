import sys
import os
import linecache
import itertools
import fileinput
import re


def update_pe(sch_file_path, pe_file_path):

    with open(sch_file_path, 'r+') as sch_file:
        sch_str = sch_file.read()

        with open(pe_file_path, 'r+') as pe_file:
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

    output_file = open(os.path.splitext(sch_file_path)[0] + '_PE_UPDATE' + os.path.splitext(sch_file_path)[1], 'w')
    output_file.write(sch_str)

update_pe('./input_files/update_PE/PRED28_J3JUL18_J2AUG19_RNB2019.inc', './input_files/update_PE/PE_RNB2019_BASE.txt')
#update_pe('./input_files/update_PE/PREDICTION20_J2H_LWI.INC', './input_files/update_PE/PE_file.txt')
#update_pe('./input_files/update_PE/PREDICTION23_NFA_J1.INC', './input_files/update_PE/PE_file.txt')
#update_pe('./input_files/update_PE/PREDICTION24_J2H_LWI_J1.INC', './input_files/update_PE/PE_file.txt')


'''
NOTE the usage of FILE PATH MANIPULATION (os.path)

See http://xahlee.info/python/python_path_manipulation.html for more details on FILE PATH MANIPULATION
'''