import urllib

url='http://www.py4inf.com/code/romeo.txt'
fhand=urllib.urlopen(url)

for line in fhand:
    print line.strip()
    
