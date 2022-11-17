# -*- coding: utf-8 -*-
#Funksjon for å ta input fra bruker of lage et nytt avtaleobjekt

from avtale import *
from datetime import datetime
from fil_funksjoner import *
import random

def NyAvtale(stedliste):
    name = input("Navn på avtalen: ")
    place = input("Sted: ")


    while True:
        print("Hvor skal møtet være?")
        print("1. Velg sted fra liste\n2. Skriv inn sted manuelt")
        valg = int(input("Velg en: "))

        
        if valg == 1:
            PrinteUtAlle(stedliste)

            while True:
                while True:
                    try:
                        indeks_valg = int(input("Bruk indeks og velg plassering: "))
                        break
                    except:
                        print("Du må bruke et tall.")

                if indeks_valg <= len(stedliste):
                    break
                else:
                    print("Du må velge gyldig indeks.")

            sted_id = stedliste[indeks_valg - 1].id
            sted = stedliste[indeks_valg - 1]
            break
                
        elif valg == 2:
            ider = []
            for line in stedliste:
                ider.append(line.id)

            while True:
                while True:
                    try:    
                        ny_id = int(input("Id: "))
                        break
                    except:
                        print("Du må bruke et tall.")

                if str(ny_id) not in ider:
                    break
                else:
                    print("Id'en er allerede i bruk. Velg en ny.")

            nytt_sted = input("Navn på nytt sted: ")
            sted = Sted(ny_id, nytt_sted)
            stedliste.append(sted)
            break
    
    while True:
        try:
            print("Når er møtet?")
            print("1. I morgen med random klokkeslett (for testing)\n2. Skriv inn dato og klokkeslett manuelt")
            valg = int(input("Velg en: "))

            if valg == 1:
                today = datetime.today()
                hour = random.randint(0, 24)
                minute = random.randint(0, 60)
                start = datetime(today.year, today.month, today.day, hour, minute)
                break

            elif valg == 2:
                gyldig = False
                while not gyldig:
                    year = int(input("År (Oppgi årstall med fire siffer): "))
                    if year >= 2022 and year <=  9999:
                        gyldig = True
                
                gyldig = False
                while not gyldig:
                    month = int(input("Måned (legg inn månedsnummer) : "))
                    if month >=1 and month <= 12:
                        gyldig = True
                
                gyldig = False
                while not gyldig:
                    day = int(input("Dag (dato mellom 1 og 31): "))
                    if day >= 1 and day <= 31:
                        gyldig = True
                        
                gyldig = False
                while not gyldig:
                    hour = int(input("Time (00 til 24): "))
                    if hour >= 00 and hour <= 24:
                        gyldig = True
                        
                gyldig = False
                while not gyldig:
                    minute = int(input("Minutt: "))
                    if minute >= 00 and minute <= 60:
                        gyldig = True
                
                
                start = datetime(year, month, day, hour, minute)
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


    return Avtale(name, place, start, duration, sted = sted)




def ny_kategori():

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
