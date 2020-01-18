"""
.read() method on a file will read the entire contents (by default, can be changed) of a file as a string. --> STRING
.readline() method reads the file one line at a time as a string (until the '\n' is encountered). --> STRING
.readlines() method on a file will read each line of the file into a list item. --> LIST

When we open a file in 'w' mode, we can only write to the file but not read.
When we open the file in 'w+' mode, we can write to and read from the file, but once we are done writing we need
to set the pointer back to the starting position using the .seek() method in order to read the file.

file.seek(character offset, optional whence):
    whence mode     description
    0               absolute file positioning
    1               points offset to the beginning of the file
    2               points offset from the current location
    3               points to the end of the file & offset is always 0

The ACCESS MODES available for the open() function are as follows:
    r:  Opens the file in read-only mode. The file pointer is placed at the beginning of the file. This is the default
        mode.
    rb: Opens the file as read-only in binary format and starts reading from the beginning of the file.
        While binary format can be used for different purposes, it is usually used when dealing with things like images,
        videos, etc.
    r+: Opens a file for reading and writing, placing the pointer at the beginning of the file.
    w:  Opens in write-only mode. The pointer is placed at the beginning of the file. Overwrites the file if the file
        exists. If the file does not exist, creates a new file for writing.
    wb: Opens a write-only file in binary mode. Overwrites the file if the file exists. If the file does not exist,
        creates a new file for writing.
    w+: Opens a file for writing and reading. Overwrites the existing file if the file exists. If the file does not
        exist, creates a new file for reading and writing.
    wb+: Opens a file for writing and reading in binary mode. Overwrites the existing file if the file exists. If the
        file does not exist, creates a new file for reading and writing.
    a:  Opens a file for appending. The pointer is placed at the end of the file if the file exists. A new file is
        created if one with the same name doesn't exist.
    ab: Opens a file for appending in binary format. The pointer is placed at the end of the file if the file exists.
        A new file is created if one with the same name doesn't exist.
    a+: Opens a file for both appending and reading. The file pointer is placed at the end of the file if the file
        exists. If the file does not exist, it creates a new file for reading and writing.
    ab+: Opens a file for both appending and reading in binary mode. The file pointer is placed at the end of the file
        if the file exists. If the file does not exist, it creates a new file for reading and writing.
"""

print('\n######################################### 1. READING FROM FILES #########################################\n')

with open('work_directory/file_read_and_write/test.txt', 'r') as f:
    print('\n------ .read() METHOD ------\n')
    f_read = f.read()               # read entire contents as a STRING
    print(f_read)
    f.seek(0, 0)                    # reset pointer to file beginning

    print('\n------ .readline() METHOD ------\n')
    f_readline = f.readline()       # read one line at a time as a STRING
    print(f_readline)
    f.seek(0, 0)

    print('\n------ .readlines() METHOD ------\n')
    f_readlines = f.readlines()     # read each line into a LIST item
    print(f_readlines)
    print()
    f.seek(0, 0)

    print('\n------ PRINT LINES USING for LOOP ------\n')
    for line in f:
        print(line, end='')
    f.seek(0, 0)

    print('\n------ PRINT CHUNKS OF TEXT USING .read() METHOD AND while LOOP ------\n')
    chunk_size = 10
    read_chunk = f.read(chunk_size)
    while len(read_chunk) > 0:
        print(read_chunk, end='*')
        read_chunk = f.read(chunk_size)
    f.seek(0, 0)

print('\n########################################## 2. WRITING TO FILES ##########################################\n')

with open('work_directory/file_read_and_write/newfile.txt', 'w+') as f:
    f.write('Test')         # write from the beginning of the file
    f.write('Test')         # continue to write from current pointer position
    f.seek(0, 0)            # reset pointer to file beginning
    f.write('R')            # overwrite the first 'T' with 'R'
    f.seek(0, 0)
    print(f.read())

print('\n############################# 3. READING FROM AND WRITING TO FILES COMBINED #############################\n')

# writing everything from test.txt to a copy called test_copy.txt
with open('work_directory/file_read_and_write/test.txt', 'r') as rf:
    with open('work_directory/file_read_and_write/test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
        print('Text file copied!')

# writing everything from bruno.jpg to a copy called bruno_copy.jpg using 'binary' access modes
with open('work_directory/file_read_and_write/bruno.jpg', 'rb') as rf:
    with open('work_directory/file_read_and_write/bruno_copy.jpg', 'wb') as wf:
        binary_chunk = 4096
        read_chunk = rf.read(binary_chunk)
        while len(read_chunk) > 0:
            wf.write(read_chunk)
            read_chunk = rf.read(binary_chunk)
        print('Image file copied!')
