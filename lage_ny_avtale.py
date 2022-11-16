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


    return Avtale(name, place, start, duration)




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


