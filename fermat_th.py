def check_fermat(a,b,c,n):
    if n>2:
        if a**n+c**n==c**n:
            print "Holy smokes !fermat was wrong "
        else:
            print "No that doesnt work "
    else:
        print "prog not working"
