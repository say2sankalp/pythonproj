def rot13(word,rot):
    rot=int(rot)
    for letter in word:
        let=ord(letter)+rot
        
        if let >122:
            let=let-26
        if let < 97:
            let=let+26
        print " ".join(chr(let))
        
