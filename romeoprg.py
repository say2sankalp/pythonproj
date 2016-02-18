
fh =open("C:\\important\\romeo.txt")
lst=list()

for lines in fh:
    word=lines.rstrip()
    word=word.split()
    print word
    for lulli in word:
        if lulli in lst:
            continue
        else:
            lst.append(lulli)
lst.sort()
print lst
