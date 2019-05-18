# http://www.pythonchallenge.com/pc/def/map.html

orig_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb " \
              "gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. " \
              "lmu ynnjw ml rfc spj."

shift = 2

intab = "abcdefghijklmnopqrstuvwxyz"
outtab = intab[shift:] + intab[:shift]

print ("Input table is: " + intab)
print ("Output table is: " + outtab)

#To make a translation table
trantab = str.maketrans(intab, outtab)

print ("Input string is: " + orig_str)
print ("Output string is: " + orig_str.translate(trantab))

'''
To understand str.maketrans() method introduced in Python 3:
    https://www.tutorialspoint.com/python3/string_maketrans.htm
'''