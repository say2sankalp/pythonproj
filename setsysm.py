import time 
s=time.time()
a=set(map(int,raw_input().split()))
b=set(map(int,raw_input().split()))
c=a.symmetric_difference(b)
for n in sorted(list(c)):
    print n
print time.time()-s
