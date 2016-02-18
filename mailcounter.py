name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name,'r')

count=dict()

for line in handle:
    if line.startswith("From "):
        word=line.split()
        mail=word[1]
        count[mail]=count.get(mail,0)+1

for word,key in count.items():
    
        
