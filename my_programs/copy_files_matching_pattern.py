import os
import glob
import shutil
import time
import datetime

today = datetime.date.today()
date = today.strftime('%d').zfill(2)
month = today.strftime('%b').lower()
folder_name = date + ' ' + month

src_dir = 'S:/'
dst_dir = 'G:/TPD/FC/CRM/RNB/RNB2021/RNB-files/Files from Sharepoint/' + folder_name
# src_dir = 'C:/Users/nabm/Desktop/test_files'
# dst_dir = 'G:/TPD/FC/CRM/RNB/RNB2021/RNB-files/Files from Sharepoint/' + 'test'

os.mkdir(dst_dir)

os.chdir(src_dir)

count = 0
t0 = time.perf_counter()

for file in glob.iglob('*/RNB2021/*_RNB2021.xlsm'):
#    if "Gungne" in file:
#        continue
#    else:
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

t1 = time.perf_counter()
time_secs = round(t1-t0, 0)
time_mins = round((t1-t0)/60, 1)

print(f"\n{count} files were matched and copied to destination.")
print(f"It took {time_mins} minutes ({time_secs} seconds) to copy the files.")

