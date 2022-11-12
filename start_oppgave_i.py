# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 18:58:35 2022

@author: AOstebo
"""

""" Enten lag funksjoner som lagrer og leser inn steder fra en egen sted-fil, eller utvid 
funksjonene fra øving 9 slik at de også lagrer og leser inn stedlista. Avgjør om stedene skal 
lagres i samme fil som avtalene eller i sin egen fil"""

def Lag_stedfil(stedliste):
    
    stedfil = open("stedfil.txt", "a")  
    
    # a lager ny fil om den ikke finnes og legger til istedetfor å skrive over
    # om vi vil skrive over - bytt til "w"
    
    for sted in stedliste:              #stedlisten må lages i menyen - når funksjonen lag_sted kjøres
        stedfil.write(f"{sted}\n")
    
    stedfil.close()
    print("Stedene er lagt til i filen stedfil.txt. ")
    
    
    