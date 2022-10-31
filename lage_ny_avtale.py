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
                year = int(input("År (legg inn 4-sifret årstall): "))
                month = int(input("Måned (legg inn månedsnummer) : "))
                day = int(input("Dag (tall): "))
                hour = int(input("Time: "))
                minute = int(input("Minutt: "))
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