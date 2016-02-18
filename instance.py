class human():
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender

    def speak_name(self):
                print "My name is %s" %self.name
    def speak(self,text):
        print text
    def perform_math_task(self,math_op,*args):
        print "%s performed a math math operation and result was the %f" %(self.name,math_op(*args))
will =human("William","male")

print will.name
print will.gender

will.speak_name()
will.speak("I love python programming ")

def add(a,b):
    return a+b

ryan=human("ryan stevens","male")

ryan.perform_math_task(add,47,37)
print add(64,34)
