name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count=dict()
for line in handle:
    if  line.startswith('From'):      
        words=line.split()
        for word in words:
            if ':' in word:
                time=word[5].split(':')
                count[time[0]]=count.get(time[0],0)+1

lst=list()

for key,value in count.items():
    lst.append((value,key))

lst.sort(reverse=True)

for value,key in lst:
    print key,value


    
