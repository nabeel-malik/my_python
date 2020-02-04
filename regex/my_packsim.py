import os
import re
import glob


def find_includes(file_path):
    # Finding INCLUDE files in the given file
    with open(file_path, 'r') as rf:
        rf_string = rf.read()

        regex_include = r"""
        (?:^INCLUDE.*?)                 # Non-capturing group
        (^.*?)                          # Block of text with include files (commented and non-commented)
        (?:^[A-Z0-9\s]+?)               # Non-capturing group
        """

        p = re.compile(regex_include, re.DOTALL | re.VERBOSE | re.MULTILINE)
        my_list = p.findall(rf_string)

        pre1_inc_str = ''
        pre2_inc_str = ''

        for item in my_list:
            pre1_inc_str = pre1_inc_str + item.strip() + '\n'

        with open('temp.txt', 'w+') as temp_file:
            temp_file.write(pre1_inc_str)
            temp_file.seek(0, 0)

            for line in temp_file:
                if not line.startswith('--'):
                    pre2_inc_str += line.strip().rstrip('/').rstrip().strip("'") + '\n'

        with open('master_inc.txt', 'a+') as master_file:
            master_file.write(pre2_inc_str)

        print('-----------------------------------------------------')
        print('File path:\t\t', file_path)
        print('# of INCLUDES:\t', len(my_list))
        print('\nList of INCLUDES:\n' + pre2_inc_str)


def my_packsim(src, dst):
    os.chdir(src)
    file_path = glob.glob('*.DATA')[0]
    find_includes(file_path)

    with open('master_inc.txt', 'r') as master_file:
        for line in master_file:
            with open(line.strip(), 'r'):
                find_includes(line.strip())
                print('TEST!')

        master_file.seek(0, 0)


my_packsim('input_files/my_packsim/src', 'input_files/my_packsim/dst')

