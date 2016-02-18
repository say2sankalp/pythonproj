import time
s=time.time()
a=set(map(int,raw_input().split()))
b=set(map(int,raw_input().split()))
c= a.union(b).difference(a.intersection(b))
d=a.union(b)
for i in sorted(list(c)):
            print i
print time.time()-s
