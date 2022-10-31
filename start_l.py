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

class Menu:
    def __init__(self):
        self.avtaleliste = ff.fillAvtaler(5)

    def run(self):

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
            print('9. Lag en liste med avtaler')
            print("10. Avslutte")

            kommando = input("Hva ønsker du å gjøre? Velg med tall 1 til 10: ")

            if kommando == "1":
                
                ff.ReadAvtale(self.avtaleliste)
                            
            elif kommando == "2":
                ff.SaveAvtale(self.avtaleliste)
                
            elif kommando == "3":
                nyavtale = lna.NyAvtale()
                self.avtaleliste.append(nyavtale)
                            
            elif kommando == "4":
                ff.PrinteUtAlle(self.avtaleliste)
            
            elif kommando == "5":
                ff.AvtalePerDato(self.avtaleliste)
                    
            elif kommando == "6":
                ff.AvtaleMedSokeOrd(self.avtaleliste)

            elif kommando == "7":
                #Slett
                while True:
                    try:
                        ff.PrinteUtAlle(self.avtaleliste)
                        slett = int(input("Velg indeksen til avtalen du vil slette: "))
                        del self.avtaleliste[slett-1]
                    except IndexError:
                        print("Velg en gyldig indeks!")

            elif kommando == "8":
                #Rediger
                while True:
                    try:
                        rediger = int(input("Velg indeksen til avtalen du vil redigere: "))
                        print (f"{self.avtaleliste[rediger-1]}")
                        self.avtaleliste[rediger-1] = lna.NyAvtale()
                    except IndexError:
                        print("Velg en gyldig indeks!")

            elif kommando == '9':
                self.avtaleliste = ff.fillAvtaler(int(input('Fyll med hvor mange? ')))
                

            elif kommando == "10":
                print ('Programmet avsluttet')

                break