M=float(raw_input())
T=int(raw_input())
X=int(raw_input())

tip=float((T*M)/100.0)
tax=float((X*M)/100.0)

final_price=M+tip+tax
print "The final price of meal is $%d.",int(round(final_price))
