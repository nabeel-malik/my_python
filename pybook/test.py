mainlist = ['case1', 'case2', 'case_special_3', 'case_special_4', 'GRID.INC', 'MULTIREG.params', 'PERMX.GRDECL']
otherlist = mainlist.copy()

print(mainlist)
print(otherlist)

for item in mainlist:
    if item.startswith('c'):
        otherlist.remove(item)

print(mainlist)
print(otherlist)
