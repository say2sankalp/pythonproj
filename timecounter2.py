name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count=dict()
for line in handle:      
        words=line.split()
        if words[0] is "From":
            time=words[5].split(':')
            count[time[0]]=count.get(time[0],0)+1

lst=list()
lst =count.items()
lst.sort()

for key,value in lst:
    print key,value


    
