##file reader by clasifying the words

name=raw_input("enter the file name")
handle=open(name,'r')
text=handle.read()
words=text.split()

count=dict()

for word in words:
    count[word]=count.get(word,0)+1


bigcount=None
bigword=None
for word,count in count.items():
    if bigcount is None or count > bigcount:
        bigword=word
        bigcount=count

print bigword,bigcount

    
