### application of whiel loop
def counter(n):
    while n>0:
        n-=1
        print n 
    print "blastoff"

def sequence(n):
    while n!=1:
        print n,
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
            


##apllication of break
def promp():
    while True:
        line=raw_input('//')
        if line =='done':
            break
        print line
    print "i am going to end this loop "



def sqroot(float a,float b):
    while True:
        print a
        y=(a+b/a)/2
        if y==a:
            break
        a=y
    print y
