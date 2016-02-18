def countdown(n):
    if n<=0:
        print "there will be blast"
    else:
        print 'program in progress'
        countdown(n-1)

def print_n(s,n):
    if n<=0:
        return
    print s
    print_n(s,n-1)
###traingle chekcer
def istraingle(a,b,c):
        if a+b>c and b+c>a and a+c>b:
            print "it is triangle"
            

def isdivisible(x,y):
    return x%y==0

    if isdivisible(x,y)== True:
        print "it is divisible"

def factorial(n):
    if not isinstance(n,int):
        print "faco is made for integer numbers "
        return None
    elif(n<0):    
        print "facto is made for postove integers "
        return None
    if (n==1):
        return 1
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
def fibo(n):
    if n==0:
        return 1
    if n==1:
        return 1
    else:
        return fibo(n-2)+fibo(n-1)


###visialization of recursive function

def facto(n):
    space=' '*(4*n)
    print space,'facto',n
    if n==0:
        return 1
    if n==1:
        return 1
    else:
        result=n*facto(n-1)
        print space,'facto',result
        return result
    
