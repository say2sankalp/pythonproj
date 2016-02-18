import re
hand=open('c:\\important\\regex_sum_42.txt')
s=0
lst=list()
for line in hand:
    line= line.rstrip()

    x=re.findall('[0-9]+',line)
    results= map(int,x)
    
    print results
