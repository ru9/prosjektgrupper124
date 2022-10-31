# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:22:01 2022

@author: alexa
"""

from avtale import Avtale
from datetime import datetime
from random import randint
from input_handler import inputDate

def avtale_to_tuple(avtale):
    return (avtale.name, avtale.place, avtale.start, avtale.duration)


# Lagre avtale i en fil 
def SaveAvtale(avtaleliste):
  import csv  
  with open ('avtalefil.txt', 'w', newline='') as fil:
    writer = csv.writer(fil)
    for avtale in avtaleliste:
        row = avtale_to_tuple(avtale)
        writer.writerow(row)                
  print ('Avtaleliste lagret i fil' + '\n')  
    
#Lese alle avtaler fra en fil til en liste "Avtaleliste" som må lages før funksjonen kalles
def ReadAvtale(avtaleliste):
    from avtale import Avtale
    import csv
    try:       
        with open("avtalefil.csv") as fil:
            reader = csv.reader(fil)
            for row in reader:
                  avtale = Avtale(*row)
                  avtaleliste.append(avtale)      
        print ('Avtaleliste er lest fra fil' + '\n')
    except FileNotFoundError:
        print ('filen er ikke funnet'+'\n')
        


#Printe ut alle avtaler i avtaleliste
def PrinteUtAlle(avtaleliste):
    if len(avtaleliste) !=0:
        print ('Alle avtaler på avtaleliste: ')
        avtale_indeks = 0
        for i in avtaleliste:
            avtale_indeks +=1
            print (f' Avtale nummer {avtale_indeks}:', end='')
            print (f'{i}' +'\n')
    else:
        print ('Avtalelisten er tom' + '\n')
        
        
#Printe ut og returnere liste med alle avtalene for spesifisert dato  
def AvtalePerDato(avtaleliste):
    
    dagens_avtaler = []
    print('Søk etter hvilken dato? \n')
    dato = inputDate()
    f_dato = dato.strftime("%x")
    for avtale in avtaleliste:
        avtaledato = datetime(avtale.start.year, avtale.start.month, avtale.start.day)
        if dato == avtaledato:
            dagens_avtaler.append (avtale)
    if len(dagens_avtaler) == 0:
        print (f'***Ingen avtaler er funnet for dato {f_dato}***'+'\n')
    else:
        print (f' Avtaler for dag {f_dato}', end='')
        for avtale in dagens_avtaler:
               print (f' {avtale} ')
    return dagens_avtaler
 
    
#printe ut og returnerer liste med alle avtalene som inneholder søkeord i tittel
def AvtaleMedSokeOrd (avtaleliste):
    avtaler_med_ord = []
    sokeord = input ('Skriv ord/setning som er del avtalenavn: ')
    sokeordliste=sokeord.split()
    for avtale in avtaleliste:
        for i in sokeordliste:
            if i.lower() not in avtale.name.lower():
                break
        else:
             avtaler_med_ord.append (avtale)
    if len(avtaler_med_ord) == 0:
        print (f'***Ingen avtaler inneholder sokeord "{sokeord}"***'+'\n')
    else:
        print (f' Avtaler som har "{sokeord}" i navnet:', end='')
        for avtale in avtaler_med_ord:
               print (f' {avtale} ')
    return avtaler_med_ord

#fyller ut en liste med n antall avtaler, for å slippe å lage en hel liste selv
def fillAvtaler( n = 5):
    now = datetime.now()
    avtaler  = []
    for i in range (n):
        #fyller ut avtaler med tilfeldig måned, dag, og tidspunkt
        nyAvtale = Avtale((f'''Avtale {i + 1}'''),(f'''Sted  {i + 2}'''), 
        datetime(now.year, randint(1, 12), randint(1, 28), randint(0, 23), randint(0, 59)), randint(0, 120) )
        avtaler.append(nyAvtale)
    return avtaler

