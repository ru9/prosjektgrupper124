# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 18:51:00 2022

@author: AOstebo
"""

"""Menysystem. Skal bruke funksjonene fra de andre oppgavene og kjøre til bruker
velger avslutt.print-setningene under kommandoene er bare for å teste om scriptet
virker før funksjonene ligger der."""


while True:
    
    print("Du har følgende valg:")
    print("1. Lese inn avtaler fra fil")
    print("2. Skrive avtalene til fil")
    print("3. Skrive inn en ny avtale")
    print("4. Skrive ut alle avtalene") 
    print("5. Avslutte")

    kommando = input("Hva ønsker du å gjøre? Velg med tall 1 til 5: ")

    if kommando == "1":

                    # her må funksjon for å lese inn avtale fra fil inn
                    # noe som filen = open
        print("1")  
                    
    elif kommando == "2":
        
                    # her må funksjon for å skrive avtalene til fil inn
        print("2")
        
    elif kommando == "3":
        
        n = input("Navn på avtalen : ")

        p = input("Plass : ")

        s = input("starttidspunkt  : ")

        v = input("Varighet : ")
        
        print(n,p,s,v)

        # c = Avtale(n,p,s,v)  #lager ny avtale 

        # "listenavn".append(c) # skal legge avtalen til i listen over avtaler
                    
    elif kommando == "4":
                
        # skrive ut alle avtalene
         print("4")
            

    elif kommando == "5":

        break