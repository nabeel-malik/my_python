# http://www.pythonchallenge.com/pc/def/map.html

#orig_str = "pc/def/map.html"


orig_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb " \
              "gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. " \
              "lmu ynnjw ml rfc spj."


decoded_str = ""

shift = 2

for letter in orig_str:
    if letter.isalpha():
        if (ord(letter) + shift) > 122:
            decoded_str += chr(ord(letter) + shift - 26)
        elif (ord(letter) + shift) < 97:
            decoded_str += chr(ord(letter) + shift + 26)
        else:
            decoded_str += chr(ord(letter) + shift)

    else:
        decoded_str += letter


#decoded_str = ''.join([chr(ord(letter) + 2) for letter in orig_str])

print (decoded_str)

'''
NOTE:

ord() method returns an integer [UTF-8 (decimal)] representing the Unicode code point of the given Unicode character.
chr() method is the inverse of ord()

A-Z: 65-90
a-z: 97-122

See: http://www.utf8-chartable.de/unicode-utf8-table.pl?utf8=dec

For example:
ord(A) = 65
chr(65) = A

'''