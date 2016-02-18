def hasnoe(word):
    for letter in word:
        if letter == 'e':
            return False
    return True


def avoid(word,forbidden):
    for letter in word:
        if letter in forbidden:
                
            return False
    return True

def use_only(word,available):
    for letter  in word:
        if letter not in forbidden:
            
            return False
    return True

def uses_all(word,required):
    for letter in required:
        if letter not in word:
            return False
    return True



def is_tripleword(word):
    i=0
    c=0
    while i< len(word)-1:
        if word[i]==word[i+1]:
            c=c+1
            if c==3:
                return True
            i+=2
        else:
            c=0
            i=i+1
    return False


def find_triple_double():
    fin= open("D:\\coding\\R-Cook-Book\\lords.txt")
    for line in fin:
        word=line.strip()
        if is_tripleword(word):
            print word
        else:
            print "muh me lelo"
