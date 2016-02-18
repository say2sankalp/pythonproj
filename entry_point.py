def entry_point():
    while True:
        line=raw_input('>')
        if line[0]=='#':
            print "magic is going to happen"
            continue
        if line== 'done':
            print 'i ma going to break '
            break
        print  "%s with concept" % line
    print 'done  ho gaya kitna karoge!'

def mul_table():
    for x in range(1,11):
        
        print '{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x)

def largest2():
    entry_point(raw_input())
    large=None
    print "before: ",large
    for itvar in [3,4,2,12,7,74,15]:
        if large is None or itvar > larg:
            large=itvar
        print "loop: ",itvar,large
    print "largest: ",large

def travese(ane):
    index=0
    while index < len(ane):
        lettter= ane[index]
        print letter
        index=index+1
