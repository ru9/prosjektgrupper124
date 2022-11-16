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
        avtaleliste = []
        kategoriliste = []
        stedliste = []
        self.avtaleliste=avtaleliste
        self.kategoriliste=kategoriliste
        self.stedliste=stedliste
   

    def run(self):
        while True:   
            print("Du har følgende valg:")
            print("1. Lese inn data fra filer")
            print("2. Skrive inn data til filer")
            print("3. Skrive inn en ny avtale")
            print("4. Skrive ut alle avtalene/kategoriene/steder") 
            print("5. Søk etter avtaler for gitt dato") 
            print("6. Søk etter avtaler med søkeord i navnet")
            print("7. Tomt menyvalg")
            print("8. Slett en Avtale / Rediger en avtale / Legg til Kategori til Avtale")
            print('9. Ledig')
            print("10. Avslutte")

            kommando = input("Hva ønsker du å gjøre? Velg med tall 1 til 10: ")

            if kommando == "1":
                ff.ReadFiler(self.avtaleliste, self.kategoriliste, self.stedliste)
               
                            
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
                    
            elif kommando == "6":
                ff.AvtaleMedSokeOrd(self.avtaleliste)

            elif kommando == "7":
                # Slett er flyttet til 8, åpen for bruk
                print("Menyvalg åpen for bruk")

            elif kommando == "8":
                #Slett, Rediger avtale eller legg Kategori til Avtale
                while True:
                    try:
                        print("""Velg mellom:
            1 - Slett en Avtale
            2 - Rediger en Avtale
            3 - Legg Kategori til Avtale""")
                        valg = int(input("Velg et nummer: "))

                        if valg == 1:
                            while True:
                                try:
                                    ff.PrinteUtAlle(self.avtaleliste)
                                    slett = int(input("Velg indeksen til avtalen du vil slette: "))
                                    del self.avtaleliste[slett - 1]
                                    break
                                except IndexError:
                                    print("Velg en gyldig indeks!")
                        elif valg == 2:
                            while True:
                                try:
                                    ff.PrinteUtAlle(self.avtaleliste)
                                    rediger = int(input("Velg indeksen til avtalen du vil redigere: "))
                                    print(f"{self.avtaleliste[rediger - 1]}")
                                    self.avtaleliste[rediger - 1] = lna.NyAvtale()
                                    break
                                except IndexError:
                                    print("Velg en gyldig indeks!")
                            break
                        elif valg == 3:
                            while True:
                                try:
                                    ff.PrinteUtAlle(self.avtaleliste)
                                    AvtaleTilKat = int(input("Velg indeksen til avtalen du vil legge til Kategori: "))
                                    ff.PrinteUtAlle(self.kategoriliste)
                                    KatTilAvtale = int(input("Velg indeksen til Katagorien over du vil tilegne Avtalen: "))
                                    print(f"{self.avtaleliste[AvtaleTilKat - 1]}" + '\n' + f"{self.kategoriliste[KatTilAvtale - 1]}" + '\n')
                                    BekreftKat = str(input("Vil du knytte Avtalen og Kategorien over sammen? (ja/nei): "))
                                    # Legger til funksjonen som slår sammen avatlen og kategorien her
                                except IndexError:
                                    print("Velg en gyldig indeks!")
                                break
                        else:
                            print("Velg mellom 1 og 3")

                    except ValueError:
                        print("Må være et tall. Prøv igjen... ")
                    break


            #elif kommando == '9':
            #ledig
            
            elif kommando == "10":
                print ('Programmet avsluttet')  
                break
            
            