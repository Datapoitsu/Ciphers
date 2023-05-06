## -------------------- Ceasar's Cipher -------------------- ##
#Written By: Aarni Junkkala

#Ceasar's Cipher crypts messages by moving letters forward in the alphabeth.
#Example by moving one letter forward: "example" -> "fybnqmf"

import GeneralTools as General


def ConvertToNumbers(m):  
    #Turns message into numbers equiling indexes of the letters.
    m = m.lower() #lowers first, to make shifting possible
    numerical = []
    for i in range(len(m)):
        letterFound = False
        for k in range(len(General.letters)):
            if m[i] == General.letters[k]:
                numerical.append(k)
                letterFound = True
                break
        if letterFound == False: #If the symbol isn't in English alphabeth, then it is added as itself.
            numerical.append(m[i])
    return numerical

def ShiftLetters(n,d):#n = numbers, d = distance; use list of numbers as parameter
    Cipher = []
    for i in range(len(n)):
        try:
            #Shifts all numbers forward by 13.
            n[i] = (n[i] + d) % len(General.letters)
            #Converts numbers into letters
            Cipher.append(General.letters[n[i]])
        except:
            #Just adds the symbol as it isn't a number
            Cipher.append(n[i])
    return Cipher

def CaesarsCipher(m,d):
    c = General.CollectCapitals(m)
    numerical = ConvertToNumbers(m)
    s = ShiftLetters(numerical,d)
    s = General.ApplyCapitals(s,c)
    s = "".join(s)
    return s

if __name__ == "__main__": 
    print("Ceasar Cipher (5):")
    e = CaesarsCipher("Hello world!",5)
    print("Encrypted: " + str(e))
    d = CaesarsCipher(e,-5)
    print("Decrypted: " + str(d))