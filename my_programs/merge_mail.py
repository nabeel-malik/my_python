# Python program to mail merger
# Names are in the file names.txt
# Body of the mail is in body.txt

with open('./work_directory/merge_mail/names.txt', 'r') as name_file:
    with open('./work_directory/merge_mail/body.txt', 'r') as body_file:
        body = body_file.read()
        for name in name_file:
            with open('./work_directory/merge_mail/email_{0}.txt'.format(name.strip()), 'w+') as email_file:
                email_file.write("Hello " + name + body)

'''
For this program, we have written all the names in separate lines in the file "names.txt".
The body is in the "body.txt" file.

We open both the files using WITH in reading mode and iterate over each name using a FOR loop.
A new file with the name "email_[name].txt" is created, where name is the name of that person.

We use strip() method to clean up leading and trailing whitespaces (reading a line from the file also reads the
newline '\n' character). Finally, we write the content of the mail into this file using the write() method.

SOURCE: https://www.programiz.com/python-programming/examples/merge-mails

FILE I/O STUDY: https://www.tutorialspoint.com/python/python_files_io.htm
'''