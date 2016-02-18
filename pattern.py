n = int(raw_input())
k=n
for i in range(1,n+1):
        print ('#'*i).rjust(k)
        k-=1
