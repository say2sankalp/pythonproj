import re
hand=open("c:\\important\\mbox-short.txt")

for line in hand:
    line=line.rstrip()

    if re.search('^X\S*: [0-9.]+',line): print line
