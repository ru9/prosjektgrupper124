# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 21:09:42 2022

@author: AOstebo
"""

from klasse_sted import Sted

def legg_til_sted(): 
    id = None
    navn = None
    gateadresse = None
    postnummer = None
    poststed = None
    
    print("Legg til sted:")
    while not id:
        id = input("Id: ")
        
    while not navn:
        navn = input ("Navn på stedet: ")
        
    while not gateadresse:
        gateadresse = input("Gateadresse: ")
    
    while not postnummer:
        postnummer = input("Postnummer: ")
        try:
            int(postnummer)
        
        except:
            print("Skriv inn et firesifret tall: ")
            postnummer = None
        
        else:
            if int(postnummer) in range(10000): #sjekker ikke at det er 4 siffer
                break
            else:
                print("Tast inn et firesifret tall")
                postnummer = None
                
    while not poststed:
        poststed = input("Poststed: ")
    
    return Sted(id, navn, gateadresse, postnummer, poststed)

ny = legg_til_sted()
print(ny)
