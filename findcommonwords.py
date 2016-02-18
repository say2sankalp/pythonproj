fname=raw_input('enter the file name:')
handle=open(fname,'r')
counts=dict()

for line in handle:
    words=line.split()
    print words
    for word in words:
        counts[word]=counts.get(word,0)+1

lst=list()

#for key,value in counts.items():
 #   lst.append((value,key))

lst.sort(reverse=True)

print sorted([(v,k) for k,v in counts.items()])
#for value,key in lst[:10]:
 #   print key,value



