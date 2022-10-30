# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 18:51:00 2022

@author: AOstebo
"""

"""Menysystem. Skal bruke funksjonene fra de andre oppgavene og kjøre til bruker
velger avslutt.print-setningene under kommandoene er bare for å teste om scriptet
virker før funksjonene ligger der."""
import fil_funksjoner as ff
import lage_ny_avtale as lna
avtaleliste = [] 


while True:   
    print("Du har følgende valg:")
    print("1. Lese inn avtaler fra fil")
    print("2. Skrive avtalene til fil")
    print("3. Skrive inn en ny avtale")
    print("4. Skrive ut alle avtalene") 
    print("5. Søk etter avtaler for gitt dato") 
    print("6. Søk etter avtaler med søkeord i navnet")
    print("7. Slett en avtale")
    print("8. Rediger en avtale")
    print("9. Avslutte")

    kommando = input("Hva ønsker du å gjøre? Velg med tall 1 til 9: ")

    if kommando == "1":
        
        ff.ReadAvtale(avtaleliste)
                    
    elif kommando == "2":
        ff.SaveAvtale(avtaleliste)
         
    elif kommando == "3":
        nyavtale = lna.NyAvtale()
        avtaleliste.append(nyavtale)
                      
    elif kommando == "4":
        ff.PrinteUtAlle(avtaleliste)
    
    elif kommando == "5":
        ff.AvtalePerDato(avtaleliste)
            
    elif kommando == "6":
        ff.AvtaleMedSokeOrd(avtaleliste)

    elif kommando == "7":
        #Slett
        ff.PrinteUtAlle(avtaleliste)
        slett = int(input("Velg indeksen til avtalen du vil slette: "))
        del avtaleliste[slett-1]

    elif kommando == "8":
        #Rediger
        rediger = int(input("Velg indeksen til avtalen du vil redigere: "))
        print (f"{avtaleliste[rediger-1]}")
        avtaleliste[rediger-1] = lna.NyAvtale()

    elif kommando == "9":
        print ('Programmet avsluttet')

        break