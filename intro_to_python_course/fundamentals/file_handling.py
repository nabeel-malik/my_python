# .read() method on a file will read the entire contents of a file as a string. --> STRING
# .readlines() method on a file will read each line of the file into a list item. --> LIST
# .readline() method reads the file one line at a time as a string (until the '\n' is encountered). --> STRING

# when we open a file in 'w' mode, we can only write to the file but not read.
# when we open the file in 'w+' mode, we can write to and read from the file, but once we are done writing we need
# to set the pointer to the file back to the starting position using the .seek() method in order to read the file.

# file.seek(character offset, optional whence)
    # whence mode       description
    # 1                 points offset to the beginning of the file
    # 2                 points offset from the current location
    # 3                 points to the end of the file & offset is always 0
