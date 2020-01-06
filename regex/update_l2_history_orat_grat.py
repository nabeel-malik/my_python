import sys
import os
import linecache
import itertools
import fileinput
import re

with open('./input_files/update_l2_history_orat_grat/RNB_2018_HIGH_v1.SCH', 'r+') as sch_file:
    str = sch_file.read()

    with open('./input_files/update_l2_history_orat_grat/historic_rate_file.txt', 'r+') as rate_file:
        for line in rate_file:
            rate_list = line.rstrip().split(" ")
            date = "\s".join(rate_list[0:3])
            orat = "".join(rate_list[3])
            grat = "".join(rate_list[4])

            # regex = "(^DATES[^\d.]+?{0}.+?WCONHIST.+?'L-2H'\s.+?\s.+?\s)(.+?)(\s.+?\s)(.+?)(\s/$)".format(date)

            regex = """
            (^DATES[^\d.]+?{0}.+?WCONHIST.+?'?L-2H'?\s.+?\s.+?\s)   #Group1 - String from DATES through Control Mode
            (.+?)                                                   #Group2 - ORAT
            (\s.+?\s)                                               #Group3 - WRAT
            (.+?)                                                   #Group4 - GRAT
            (\s/$)                                                  #Group5 - Trailing " /"
            """.format(date)

            p = re.compile(regex, re.DOTALL | re.VERBOSE | re.MULTILINE)
            str = p.sub('\g<1>{0}\g<3>{1}\g<5>'.format(orat, grat), str)

output_file = open('./input_files/update_l2_history_orat_grat/RNB_2018_HIGH_v1_output.SCH', 'w')
output_file.write(str)


