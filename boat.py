class boat():
    pass

my_boat=boat()
my_boat2=boat()

if my_boat is my_boat2:
    print "they point ot sam address in  memory"

print my_boat
print my_boat2
print id(my_boat)
print id(my_boat2)
