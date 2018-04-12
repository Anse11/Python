def anti_vowel(text):
    t=""
    for c in text:
        #If character is vowel make it blank
        #otherwise just add it
        for i in "ieaouIEAOU":
            if c==i:
                c=""
            else:
                c=c
        t=t+c
    return t
