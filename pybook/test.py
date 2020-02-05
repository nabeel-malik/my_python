paths = {}
line = "'GRIDS' '/disk1/studies/grids' /"

path_info = line.split("--")[0].strip().split("'")
paths[path_info[1]] = path_info[3]

# str1 = line.split("--")[0]
# str2 = str1.strip()
# str3 = str2.replace("", "X")
# str4 = str3.split()
#
# print(str1)
# print(str2)
# print(str3)
# print(str4)
#
#
print(paths)
