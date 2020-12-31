import os
import glob
import shutil
import time
import datetime

# create folder with the current date/time as the name (eg. '25 sep 1400'), to copy the files daily
today = datetime.datetime.today()
date = today.strftime('%d')
month = today.strftime('%b').lower()
t = today.strftime('%H')
folder_name = f'{date} {month} {t}00'

# the sharepoint area, where the files need to be copied from, is mapped as a network drive (S:/)
src_dir = 'S:/'
dst_dir = 'G:/TPD/FC/CRM/RNB/RNB2021/RNB-files/Files from Sharepoint/' + folder_name
# src_dir = 'C:/Users/nabm/Desktop/test_files'
# dst_dir = 'G:/TPD/FC/CRM/RNB/RNB2021/RNB-files/Files from Sharepoint/' + 'test'

# files to ignore during copying
ignore_files = ['Hanz_RNB2021.xlsm', 'Ivar Aasen_RNB2021.xlsm']

# make destination directory
os.mkdir(dst_dir)

# change current working directory to source directory
os.chdir(src_dir)

# initiate copied files counter
count = 0

# initial time
t0 = time.perf_counter()

# loop through the files in the source directory, and copy files matching a specific glob pattern
for file in glob.iglob('*/RNB2021/*_RNB2021.xlsm'):
    if file.strip().split("\\")[-1] in ignore_files:
        continue
    else:
        while True:
            try:
                shutil.copy(file, dst_dir)
            except PermissionError:
                print(f"Permission denied to file: {file}. Will try again in 15 seconds...")
                time.sleep(15)
                continue
            else:
                print(f"{file} copied.")
                count += 1
                break

# final time
t1 = time.perf_counter()

time_secs = round(t1-t0, 0)
time_mins = round((t1-t0)/60, 1)

# display key information from program
print(f"\n{count} files were matched and copied to destination.")
print(f"It took {time_mins} minutes ({time_secs} seconds) to copy the files.")