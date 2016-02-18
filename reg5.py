import re
handle= open('c:\\important\\mbox-short.txt')

for line in handle:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0 :
        print x

