name= raw_input("Enrter file: ")
handle=open(name,'r')
text=handle.read()
words=text.split()
counts=dict()

for word in words:
    counts[word]=counts.get(word,0)+1

bgcnt=None
bgwrd=None

for word,count in counts.item():
    if bgcnt is None or count > bgcnt:
        bgwrd=word
        bgcnt=count

print bgwrd,bgcnt
