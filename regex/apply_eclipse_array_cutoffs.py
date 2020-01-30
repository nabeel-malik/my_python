import re
import textwrap
import os


def update_array_cutoffs(input_file_path, array_name, max_cutoff, min_cutoff):
    """
    This function takes in a GRDECL file, and applies maximum and minimum cut-offs to the specified array.
    :param input_file_path:     Path of the input *.GRDECL file relative to this .py file
    :param array_name:          Name of the property/array that the cut-oss are to be applied to, e.g. PORO, PERMX etc.
    :param max_cutoff:          Maximum cut-off value
    :param min_cutoff:          Minimum cut-off value
    """

    with open(input_file_path, 'r') as rf:
        f_read = rf.read()

    # Finding whole string with property name
    a = re.compile("{}\n(.+?)/".format(array_name), re.DOTALL)
    property_string = a.search(f_read).group(1)

    # Finding just the values string and putting the values in a list
    b = re.compile("[-.\d]+?\s", re.DOTALL)
    values_list = b.findall(property_string)

    # Stripping all strings and converting to float
    values_list_strip_float = []

    def strip_and_float(string):
        new_float = float(string.strip())
        return new_float

    for i in map(strip_and_float, values_list):
        values_list_strip_float.append(i)
        # print(i)

    # Applying cut-offs
    values_list_strip_final = []

    for item in values_list_strip_float:
        if item > max_cutoff:
            values_list_strip_final.append(max_cutoff)
        elif 0 <= item < min_cutoff:
            values_list_strip_final.append(min_cutoff)
        else:
            values_list_strip_final.append(item)

    # Printing QC parameters
    print("-----------------------------------------------")
    print('Max {}:\t\t\t\t\t\t\t'.format(array_name), max(values_list_strip_final))
    print('Min {}:\t\t\t\t\t\t\t'.format(array_name), min([x for x in values_list_strip_final if 0 <= x <= min_cutoff]))
    print('Any {} values greater than {}?\t'.format(array_name, max_cutoff),
          any(x > max_cutoff for x in values_list_strip_final))
    print('Any {} values less than {}?\t\t'.format(array_name, min_cutoff),
          any(0 < x < min_cutoff for x in values_list_strip_final))
    print('# of values in {} array:\t\t\t'.format(array_name), len(values_list_strip_final))

    # Converting all floats in list to strings
    final_list = []

    for i in map(str, values_list_strip_final):
        final_list.append(i)

    # Writing updated array to a new file
    final_string_wrapped = "{}\n".format(array_name) + \
                           textwrap.fill(" ".join(final_list), width=125, break_long_words=False) + '\n/'

    updated_file_string = a.sub(final_string_wrapped, f_read)

    with open(os.path.splitext(input_file_path)[0] + '_{}_updated'.format(array_name) + '.txt', 'w+') as wf:
        wf.write(updated_file_string)


update_array_cutoffs('input_files/apply_eclipse_array_cutoffs/input.txt', 'PORO', 0.2, 0.06)
update_array_cutoffs('input_files/apply_eclipse_array_cutoffs/input_PORO_updated.txt', 'PERMX', 175, 50)

