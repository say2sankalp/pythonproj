import urllib
url='http://dr-chuck.com/page1.htm'
fhand=urllib.urlopen(url)
for line in fhand:
    print line.strip()

html=fhand.read()
soupp=BeautifulSoup(html)

tags=soup('a')
for tag in tags:
    print tag.get('href',None)
