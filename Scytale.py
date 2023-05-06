## ------------------------- Scytale -------------------- ##
#Written By: Aarni Junkkala

#Explination by wikipedia: https://en.wikipedia.org/wiki/Scytale
#My explination:
#crypted message is built in a way where we choose shift amount order of letters,
#in a way where reading would require you to read every n:th letter,
#untill there is no letters left and moving to next letter. stopping when all letters are read

#Wikipedia page has good illustration!

#Best way to think of it is as a table:
# Input -> we always love coding
# ['w','e','a','l','w','a'],
# ['y','s','l','o','v','e'],
# ['c','o','d','i','n','g'],
# Output -> wycesoaldloiwvnaeg

# now instead of reading it from left to right where it would make sense,
# we crypt it by writing it from top to bottom.
# From there we get the result of 'wycesoaldloiwvnaeg'

#Decrypting
# ['w','y','c'],
# ['e','s','o'],
# ['a','l','d'],
# ['l','o','i'],
# ['n','v','w'],
# ['e','a','g'],

# ['c','o','d','i','n'],
# ['g','i','s','v','e'],
# ['r','y','f','u','n'],


#When decrypting, we have to use the amount of rows in the original, instead of width

#This program will have two versions, one whit spaces and one whit out

def ReOrder(m,d):
    t = []
    for i in range(len(m)):
        if i % d == 0:
            t.append([])
        t[-1].append(m[i])
    
    crypted = []
    
    for k in range(len(t[0])): #k = 6
        for i in range(len(t)): # i = 3
            crypted.append(t[i][k])
    print("".join(crypted))

def DeOrder(m,d): #encrypted, distance
    t = []
    for i in range(len(m)):
        if i % d == 0:
            t.append([])
        t[-1].append(m[i])
    num = len(t)
        
    decrypt = []
    for i in range(len(t[0])): #3
        for k in range(len(t)):
            decrypt.append(t[k][i])
    
    print("".join(decrypt))

ReOrder("codingisveryfun",5)
DeOrder("cgroiydsfivunen",5)
ReOrder("wealwayslovecoding",6)
DeOrder("wycesoaldloiwvnaeg",6)

def ScytaleNoSpaces(m,d): #message, distance. message must be in multiplier of the 
    m = m.replace(" ","")
    print(m)
    if len(m) %  d != 0:
        return False
            
#print(ScytaleNoSpaces("hello you all again",4))