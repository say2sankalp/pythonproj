import re
hand=open("c:\\important\\mbox-short.txt")

for line in hand:
    line=line.rstrip()
    if  re.search('^From:.+@*',line): print line

text="From: stephen.marquard@uct.ac.za, csev@umich.edu, and cwen @iupui.edu"
lin=lin.rstrip()
if re.search('^From:.+@',lin):print lin
