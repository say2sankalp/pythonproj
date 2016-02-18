n,m=(raw_input().split())
setx=set(raw_input().split())
seta=set(raw_input().split())
setb=set(raw_input().split())

sum1=0

for x in setx:
    if x in seta:
        sum1+=1
    if x in setb:
        sum1-=1
    else:
        sum1=sum1
print sum1
