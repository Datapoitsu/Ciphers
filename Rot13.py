## -------------------- Rot 13 -------------------- ##
#Written By: Aarni Junkkala

#Rotate 13 is basicly just ceasar's cipher, with 13 as the amount to rotate.
import CeasarsCipher as CC

def EncryptRot13(m): #m = message
    return CC.CaesarsCipher(m,13)
    
def DecryptRot13(m):
    return CC.CaesarsCipher(m,-13)

if __name__ == "__main__": 
    #Rot13
    print("Rot13:")
    e = EncryptRot13("Hello world!")
    print("Encrypted: " + str(e))
    d = DecryptRot13(e)
    print("Decrypted: " + str(d))