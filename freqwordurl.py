import urllib

url='http://www.py4inf.com/code/romeo.txt'
fhand=urllib.urlopen(url)
count=dict()
for line in fhand:
    words=line.split()

    for word in words:
        count[word]=count.get(word,0)+1
print count
    
