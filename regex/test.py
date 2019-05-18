import os
import re

target_dir = 'Y:/private/nabm/eph_projects/beta/lwd_log_data/4-11'
search_str = r'DLIS_CONTENT.ASC'

os.chdir(target_dir)      #change directory
total_files = len(os.listdir('.'))
remaining_files = total_files
deleted_files = 0

for file in os.listdir('.'):
    if re.search(search_str, file):
        # print(file)
        os.remove(file)
        deleted_files+=1
        remaining_files-=1

print('{0} total files existed in target directory.'.format(total_files))
print('{0} files have been removed!'.format(deleted_files))
print('{0} files currently in target directory'.format(remaining_files))

