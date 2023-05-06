## -------------------- General tools -------------------- ##
#Written By: Aarni Junkkala

#This file is mostly functions that are used in multiple codes,
#like collecting capilat letters and aplying them.

#Only uses English alpabeth. If you want to use alphabet of your language, then you have to change this list.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def CollectCapitals(m):
    CapitalIndex = []
    for i in range(len(m)):
        if m[i].isupper() == True:
            CapitalIndex.append(i)
    return CapitalIndex

def ApplyCapitals(m,c):
    for i in range(len(c)):
        m[c[i]] = m[c[i]].upper()
    return m