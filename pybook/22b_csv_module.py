import csv
import os

'''
csv module documentation: https://docs.python.org/3/library/csv.html
'''

print('\n############################# 1. READING A CSV FILE USING csv.reader() METHOD #############################\n')
'''
Python documentation states that when csv.reader() or csv.writer() methods are called on a 'file' object, the file 
should always be opened with the "newline=''" argument
'''
with open('work_directory/csv_module/names.csv', 'r', newline='') as csv_file:      # newline='' used for file object

    # csv.reader() creates a '_csv.reader' object
    csv_reader = csv.reader(csv_file)

    # checking object type
    print(csv_reader)
    print(type(csv_reader))

    next(csv_reader)                    # skip printing the header

    # print each line (list)
    for line in csv_reader:
        print(line)

    csv_file.seek(0, 0)                 # set pointer back to beginning of file
    next(csv_reader)                    # skip printing the header

    # print each email (list[2])
    for line in csv_reader:
        print(line[2])


print('\n############################ 2. WRITE TO A CSV FILE USING csv.writer() METHOD ############################\n')
'''
Now, let's say we want to read from a CSV file, and write the contents a new CSV file using '-' as the delimiter.
'''

with open('work_directory/csv_module/names.csv', 'r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('work_directory/csv_module/new_names.csv', 'w', newline='') as new_file:
        # csv.writer() creates a '_csv.writer' object
        csv_writer = csv.writer(new_file, delimiter='-')
        for line in csv_reader:
            csv_writer.writerow(line)

print(f'{new_file.name} created')

'''
Note: 
- In new_names.csv, that is just created with the '-' delimiter, for the fields that originally contained a '-' (in
names.csv), csv.writer() places a "" around the value to highlight that the '-' in the value is NOT a delimiter.
- The new_names.csv can be read again using csv.reader(<filename>, delimiter='-').
'''

print('\n############################# 3. READING A CSV FILE USING csv.reader() CLASS #############################\n')
'''
csv.reader() and csv.writer() METHODS are probably more commonly used when working with csv data, since they are the 
first methods that come up in the Python documentation, but the preferred method of working with csv data is using the 
csv.DictReader() and csv.DictWriter() CLASSES.

csv.DictReader() CLASS:
    - csv.DictReader() CLASS creates an object that operates like a regular reader but MAPS THE INFORMATION IN EACH ROW 
    TO AN ORDERED DICTIONARY (OrderedDict object) whose keys are given by the optional 'fieldnames' parameter.
    - The 'fieldnames' parameter is a 'sequence'. If 'fieldnames' is omitted, the values in the first row of file will 
    be used as the 'fieldnames'. Regardless of how the fieldnames are determined, the dictionary preserves their 
    original ordering.

csv.DictWriter() CLASS:   
    - csv.DictWriter() CLASS creates an object which operates like a regular writer but MAPS DICTIONARIES ONTO OUTPUT 
    ROWS. 
    - The 'fieldnames' parameter is a 'sequence' of keys that identify the order in which values in the dictionary 
    passed to the writerow() method are written to file.
    - Note that unlike the DictReader CLASS, the 'fieldnames' parameter of the DictWriter CLASS is NOT optional. 

Let's see why csv.DictReader() and csv.DictWriter() are preferred over csv.reader() and csv.writer().

First, we will read a CSV file using the csv.DictReader() CLASS.   
'''

with open('work_directory/csv_module/names.csv', 'r', newline='') as csv_file:

    # csv.DictReader() creates a an instance of the 'DictReader' class
    csv_reader = csv.DictReader(csv_file)

    # checking object type
    print(csv_reader)
    print(type(csv_reader))

    # print each line (ordered dict)
    for line in csv_reader:
        print(line)

    csv_file.seek(0, 0)                 # set pointer back to beginning of file

    # print each email (ordered dict[email])
    for line in csv_reader:
        print(line['email'])            # more understandable when reading code, instead of print(line[2])


print('\n########################### 4. WRITE TO A CSV FILE USING csv.DictWriter() CLASS ###########################\n')

'''
csv.DictWriter() CLASS:   
    - csv.DictWriter() CLASS creates an object which operates like a regular writer but MAPS DICTIONARIES ONTO OUTPUT 
    ROWS. 
    - The 'fieldnames' parameter is a 'sequence' of keys that identify the order in which values in the dictionary 
    passed to the writerow() method are written to file.
    - Note that unlike the DictReader CLASS, the 'fieldnames' parameter of the DictWriter CLASS is NOT optional.

Now, let's read from a CSV file, and write the contents a new CSV file using the default delimiter (',').
'''

with open('work_directory/csv_module/names.csv', 'r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    field_names = ['first_name', 'last_name', 'email']

    with open('work_directory/csv_module/new_names_DictWriter.csv', 'w', newline='') as new_file:
        # csv.DictWriter creates an instance of the 'DictWriter' class
        csv_writer = csv.DictWriter(new_file, fieldnames=field_names)       # 'fieldnames=' argument added

        # write the header
        csv_writer.writeheader()

        # write the remaining file
        for line in csv_reader:
            csv_writer.writerow(line)

print(f'{new_file.name} created')