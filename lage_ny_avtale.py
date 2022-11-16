# -*- coding: utf-8 -*-
#Funksjon for å ta input fra bruker of lage et nytt avtaleobjekt

from avtale import *
from datetime import datetime
import random

def NyAvtale():
    name = input("Navn på avtalen: ")
    place = input("Sted: ")
    
    while True:
        try:
            print("Når er møtet?")
            print("1. I morgen med random klokkeslett (for testing)\n2. Skriv inn dato og klokkeslett manuelt")
            valg = int(input("Velg en: "))

            if valg == 1:
                today = datetime.today()
                hour = random.randint(0, 24)
                minute = random.randint(0, 60)
                start = datetime(today.year, today.month, today.day+1, hour, minute)
                start = str(start)
                break

            elif valg == 2:
                year = int(input("År: "))
                month = int(input("Måned: "))
                day = int(input("Dag: "))
                hour = int(input("Time: "))
                minute = int(input("Minutt: "))
                start = datetime(year, month, day, hour, minute)
                start = str(start)
                break

        except KeyboardInterrupt:
            exit()
        except:
            print("Noe gikk galt, prøv igjen... ")
    
    while True:
        try:
            duration = float(input("Hvor lenge varer møtet (i minutter): "))
            break

        except ValueError:
            print("Må være et tall. Prøv igjen... ")

<<<<<<< Updated upstream
    return Avtale(name, place, start, duration)
=======
    return Avtale(name, place, start, duration)

def NyKategori():
    id = None
    navn = None
    prioritet = None
    print('Legg til kategori: \n')
    while not id:
        id = input('id: ')
    while not navn:
        navn = input('navn: ')
    while not prioritet:
        prioritet = input('Prioritet: ')
        try:
            int(prioritet)
        except:
            print('Tast inn et tall mellom 1 og 3')
            prioritet = None
        else:
            if int(prioritet) in range(1, 4):
                break
            else:
                print('Tast inn et tall mellom 1 og 3')
                prioritet = None
    return Kategori(id, navn, prioritet)

def NySted():
    id = None
    navn = None
    gateadresse = None
    postnummer = None
    poststed = None
    print('Legg til sted: \n')
    while not id:
        id = input('id: ')
    while not navn:
        navn = input('navn: ')
    print("For legge inn gateadresse, postnummer og poststed velg 1; for å hoppe over velg 2: ")
    while not gateadresse:
        try:        
            valg = int(input("Velg 1 eller 2: "))    
            if valg==1:
                gateadresse = input('gateadresse: ') 
                postnummer = input('postnummer: ')
                poststed = input ('poststed: ')
            elif valg==2:
                gateadress=None
                postnummer=None
                poststed=None
                break
        except KeyboardInterrupt:
           exit()
        except:
           print('Tast inn et tall mellom 1 og 2')
    return Sted(id, navn, gateadresse, postnummer, poststed)
>>>>>>> Stashed changes
