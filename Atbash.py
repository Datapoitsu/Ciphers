## -------------------- Atbash -------------------- ##
#Written By: Aarni Junkkala

import GeneralTools as General

def Atbash(m):
    c = General.CollectCapitals(m)
    m = m.lower()
    crypt = []
    for i in range(len(m)):
        try:
            crypt.append(General.letters[len(General.letters) - General.letters.index(m[i]) - 1])
        except:
            crypt.append(m[i])
    return "".join(General.ApplyCapitals(crypt,c))

if __name__ == "__main__":
    e = Atbash("Hello world")
    print(e)
    d = Atbash(e)
    print(d)
    
    e = Atbash("abcdefghijklmnopqrstuvwxyz")
    print(e)
    d = Atbash("zyxwvutsrqponmlkjihgfedcba")
    print(d)