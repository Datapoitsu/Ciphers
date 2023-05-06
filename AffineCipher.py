## -------------------- Affine Cipher -------------------- ##
#Written By: Aarni Junkkala

#a,b,m
# m = amount of letters
# a and m should always be coprime

import GeneralTools as General

def Encrypt(a,b,m):
    c = General.CollectCapitals(m)
    m = m.lower()
    crypt = []
    for i in range(len(m)):
        try:
            crypt.append(General.letters[(General.letters.index(m[i]) * a + b) % len(General.letters)])
        except:
            crypt.append(m[i])
    
    return "".join(General.ApplyCapitals(crypt,c))

def Decrypt(a,b,m):
    c = General.CollectCapitals(m)
    m = m.lower()
    crypt = []
    for i in  range(len(m)):
        try:
            crypt.append(General.letters[    (m[i] - b) % len(General.letters)])
        except:
            crypt.append(m[i])
    return "".join(General.ApplyCapitals(crypt,c))
if __name__ == "__main__":
    print(Encrypt(5,8,"Hello world!"))
    print(Decrypt(5,8,"Rclla oaplx!"))