count=dict()
print "enter a line of text"
line=raw_input("")

words=line.split()
print "words:",words

print "counting... "
for word in words:
    count[word]=count.get(word,0)+1

print "count ",count
