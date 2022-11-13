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

<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
=======
>>>>>>> Stashed changes
class Menu:
    def __init__(self):
       self.avtaleliste = ff.fillAvtaler(5)
       self.kategoriliste = ff.fillKategorier()
       self.stedliste = ff.fillSteder()
   
>>>>>>> Stashed changes

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

<<<<<<< Updated upstream
    kommando = input("Hva ønsker du å gjøre? Velg med tall 1 til 9: ")

    if kommando == "1":
        
        ff.ReadAvtale(avtaleliste)
=======
        while True:   
            print("Du har følgende valg:")
            print("1. Lese inn data fra filer")
            print("2. Skrive inn data til filer")
            print("3. Skrive inn en ny avtale")
            print("4. Skrive ut alle avtalene/kategoriene/steder") 
            print("5. Søk etter avtaler for gitt dato") 
            print("6. Søk etter avtaler med søkeord i navnet")
            print("7. Slett en avtale")
            print("8. Rediger en avtale")
            print('9. Lag liste med avtaler, liste med kategorier, og liste med steder')
            print("10. Avslutte")

            kommando = input("Hva ønsker du å gjøre? Velg med tall 1 til 10: ")

            if kommando == "1":
                
                ff.ReadAvtale(self.avtaleliste)
                ff.ReadKategori(self.kategoriliste)
                ff.ReadSted(self.stedliste)
                            
            elif kommando == "2":
                ff.SaveAvtale(self.avtaleliste)
                ff.SaveKategori(self.kategoriliste)
                ff.SaveSted(self.stedliste)
                
            elif kommando == "3":
                nyavtale = lna.NyAvtale()
                self.avtaleliste.append(nyavtale)
                            
            elif kommando == "4":
                while True:
                    try:
                        print("""For å skrive ut alle:
              avtaler - velg 1
              kategorier - velg 2
              steder - velg 3""")
                        valg = int(input("Velg: "))
        
                        if valg == 1:
                            ff.PrinteUtAlle(self.avtaleliste)  
                            break
                        elif valg == 2:
                           ff.PrinteUtAlle(self.kategoriliste)
                           break
                        elif valg == 3:
                           ff.PrinteUtAlle(self.stedliste)
                           break
                        else:
                           print("Velg mellom 1 og 3")  
                           
                    except ValueError:
                         print("Må være et tall. Prøv igjen... ")
            
            elif kommando == "5":
                ff.AvtalePerDato(self.avtaleliste)
>>>>>>> Stashed changes
                    
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

<<<<<<< Updated upstream
    elif kommando == "8":
        #Rediger
        rediger = int(input("Velg indeksen til avtalen du vil redigere: "))
        print (f"{avtaleliste[rediger-1]}")
        avtaleliste[rediger-1] = lna.NyAvtale()

    elif kommando == "9":
        print ('Programmet avsluttet')
=======
            elif kommando == '9':
                self.avtaleliste = ff.fillAvtaler(int(input('Fyll med hvor mange avtaler? ')))
                self.kategoriliste = ff.fillKategorier()
                self.stedliste = ff.fillSteder(int(input('Fyll med hvor mange steder? ')))
            
<<<<<<< Updated upstream
            if kommando == "10":
                
                ff.ReadKategori(self.kategoriliste)
                            
            elif kommando == "11":
                ff.SaveKategori(self.kategoriliste)
=======
>>>>>>> Stashed changes

            elif kommando == "10":
                print ('Programmet avsluttet')
>>>>>>> Stashed changes

        break