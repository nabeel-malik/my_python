import os

dir1 = 'G:/TPD/FC/CRM/RNB/RNB2021/RNB-files/Files from Sharepoint/10_sep'
dir2 = 'G:/TPD/FC/CRM/RNB/RNB2021/RNB-files/Files from Sharepoint/10 sep'

set1 = set(os.listdir(dir1))
set2 = set(os.listdir(dir2))

for item in set1.difference(set2):
    print(item)
