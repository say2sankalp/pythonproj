import re
hand=open('c:\\important\\regex_sum_223176.txt')
s=0
lst=list()
for line in hand:
    line= line.rstrip()

    x=re.findall('[0-9]+',line)
    
    results= [int(i) for i in x]
    if len(x)>0:
        print results
        lst.append(results)

sf=[item for sublist in lst for item in sublist]
print sum(sf)

       
        

