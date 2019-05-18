#!/usr/bin/python
import re
'''
line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?)( .*)', line, re.M|re.I)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
   print("matchObj.group(3) : ", matchObj.group(3))
else:
   print ("No match!!")
'''

'''
#p = re.compile(r'(\b\w+)\s+\1')
p = re.compile(r'(\b\w+\b) \1')
print (p.search('Paris in the the spring').group())
'''

'''
m = re.match("([abc])+", "abc")
print (m.groups())
'''
'''
p = re.compile('\d+')
p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
iterator = p.finditer('12 drummers drumming, 11 ... 10 ...')
for match in iterator:
    print (match.group())
'''
############################################################################################

str = '''DATES                                  -- Generated : Petrel
  19 JUL 2009 /
  /

WCONHIST                               -- Generated : Petrel
  'L-2H' OPEN RESV 797.68 1* 3059877.94 /
  /
'''

p = re.compile("""
(DATES.+?19\sJUL\s2009.+?WCONHIST.+?'L-2H'\s.+?\s.+?\s)     #Group1 - String from DATES through WCONHIST Control Mode
(.+?)                                                       #Group2 - ORAT
(\s.+?\s)                                                   #Group3 - WRAT
(.+?)                                                    #Group4 - GRAT
(\s/)                                                        #Group5 - Trailing " /"
""",re.DOTALL | re.VERBOSE)

print (p.search(str).group())
print ("Group1: " + p.search(str).group(1))
print ("Group2: " + p.search(str).group(2))
print ("Group3: " + p.search(str).group(3))
print ("Group4: " + p.search(str).group(4))
print ("Group5: " + p.search(str).group(5))

orat = 700.00
grat = 3000000.00

final = p.sub(r"\g<1>{0}\g<3>{1}\g<5>".format(orat, grat), str)
print(final)






