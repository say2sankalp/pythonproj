import re
handle=open("c:\\important\\mbox-short.txt")

for line in handle:
    line=line.rstrip()
    x=re.findall('\S+\S+',line)
    if len(x)>0:
        print x
