import re
hn=open("c:\\important\\mbox-short.txt")
numlist=[]

for line in hn:
        line=line.rstrip()
        stuff=re.findall("^X-DSPAM-Confidence: ([0-9.]+)",line)
        if len(stuff)!= 1: continue
        num=float(stuff[0])
        numlist.append(num)
print 'maximum:', max(numlist)
        
