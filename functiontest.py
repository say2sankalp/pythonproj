def summ(a,b):
    return a+b
    print a

def summ2(a,b):
    print sum(a,b)

def foo():
    print("hello from inside of foo")
    return 1

def  am_i_wrong(ans):
    if ans== 'yes':
        return True
    else:
        return False

####alrternative thing to that

def am_i(ans):
    if ans=='yes':
        print "its true"
    else:
        print "its false"

def entry_point():
    
    while True:
        res=raw_input('enter maro')    
        if res== "#":
            print "resetting the answer"
            continue
        elif res=="done":
            print "you are done "
            break
        else:
            print "%s are u happy " % res
    print "task done bro"
