import urllib

fhand=urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
count=dict()
for line in fhand:
    words=line.split()
    for word in words:
        count[word]=count.get(word,0)+1
print count
