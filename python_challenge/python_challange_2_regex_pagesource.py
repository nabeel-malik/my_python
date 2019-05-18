import sys
import os
import linecache
import itertools
import fileinput
import re

with open('./inputfiles/python_challange_2_regex_pagesource/pagesource.txt', 'r+') as pagesource_file:
    pagesource_string = pagesource_file.read()

    regex = r"""
    ^<!--
    [\w\s:]*?
    -->.*?
    ^<!--
    (.*?)               #Group1: The mess in which we need to search the rare characters
    -->
    """

    p = re.compile(regex, re.DOTALL | re.VERBOSE | re.MULTILINE)
    mess_str = p.search(pagesource_string).group(1)

    m = re.compile(r"[a-zA-Z0-9]")
    found_str = ''.join(m.findall(mess_str))
    print(found_str)