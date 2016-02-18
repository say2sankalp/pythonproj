import re
hn=open("c:\\important\\mbox-short.txt")
for line in hn:
    line=line.strip()
    if re.search('From:',line):
        print line
