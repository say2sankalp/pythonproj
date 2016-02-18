def count(word,letter):
    index=0
    c=0
    while index < len(word):
        if word[index: ]==letter[0:len(letter)]:
            c+=1
            
        index+=1   
    print c

def in_both(word1,word2):
    for letter in word1:
        if letter in word2:
            print letter,"+",

