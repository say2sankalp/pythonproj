## modualr programming

def openfile():
    fname=raw_input("enter the file name ")
    if len(fname)<1 :fname="c:\\important\\mbox-short.txt"
    try:
        fh=open(fname,'r')
    except:
        print "Error opening file ,file removed or moved"
        quit()
    return fh

def strtsWith():
    sw=raw_input("enter the line of prefix: ")
    if len(sw)<1 :sw="From"
    return sw

def counttimes(lines,s):
    count=dict()
    for line in lines:
        if line.startswith(s) and not line.startswith(s+':'):
            line=((line.rstrip()).lstrip()).split()
            print line
            str=line[5]
            hour=str[0:str.find(":"):1]
            count[hour]=count.get(hour,0)+1
    return count

def sortimes(d):
    lst=list()
    for key,val in d.items():
        lst.append((val,key))
    print lst
    lst.sort
    for val,key, in lst:
        print key,val

fh=openfile()
sw=strtsWith()
dicitionary=counttimes(fh,sw)
t=sortimes(dicitionary)
