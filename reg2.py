import re
handle=open("c:\\important\\mbox-short.txt")

def reg1():
    for line in handle:
        line=line.rstrip()
        if re.search('^From:.+n@',line): print line

def reg2():
    for line in handle:
        line=line.rstrip()
        if re.findall('\S+@\S+',line) : print line
        
