def find_gcd(a,b):
    if a==b:
        return a
    else:
        x=max(a,b)-min(a,b)
        y=min(a,b)
        return find_gcd(x,y)
    return find_gcd(b,a%b)


gcd=find_gcd(5,1)
print gcd
    
