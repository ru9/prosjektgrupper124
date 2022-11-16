# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:22:01 2022

@author: alexa
"""

from avtale import Avtale 
from avtale import Kategori
from avtale import Sted
from datetime import datetime
from random import randint
from input_handler import inputDate


def avtale_to_tuple(avtale):
    return (avtale.name, avtale.place, avtale.start, avtale.duration)

def kategori_to_tuple(kategori):
    return (kategori.id, kategori.navn, kategori.prioritet)

def sted_to_tuple(sted):
    return (sted.id, sted.navn, sted.gateadresse, sted.postnummer, sted.poststed)

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
        with open("avtalefil.txt") as fil:
            reader = csv.reader(fil)
            for row in reader:
                  avtale = Avtale(*row)
                  avtaleliste.append(avtale)      
        print ('Avtaleliste er lest fra fil' + '\n')
    except FileNotFoundError:
        print ('filen er ikke funnet'+'\n')

        
# Lagre kategori i en fil 
def SaveKategori(kategoriliste):
  import csv  
  with open ('kategorifil.txt', 'w', newline='') as fil:
    writer = csv.writer(fil)
    for kategori in kategoriliste:
        row = kategori_to_tuple(kategori)
        writer.writerow(row)                
  print ('Kategoriliste lagret i fil' + '\n')  
    
#Lese alle kategorier fra en fil til en liste "Kategoriliste" som må lages før funksjonen kalles
def ReadKategori(kategoriliste):
    from avtale import Kategori
    import csv
    try:       
        with open("kategorifil.txt") as fil:
            reader = csv.reader(fil)
            for row in reader:
                  kategori = Kategori(*row)
                  kategoriliste.append(kategori)      
        print ('Kategoriliste er lest fra fil' + '\n')
    except FileNotFoundError:
        print ('filen er ikke funnet'+'\n')

# Lagre kategori i en fil 
def SaveSted(stedliste):
   import csv  
   with open ('stedfil.txt', 'w', newline='') as fil:
     writer = csv.writer(fil)
     for sted in stedliste:
         row = sted_to_tuple(sted)
         writer.writerow(row)                
   print ('Stedliste lagret i fil' + '\n')  
     
 #Lese alle kategorier fra en fil til en liste "Kategoriliste" som må lages før funksjonen kalles
def ReadSted(stedliste):
     from avtale import Sted
     import csv
     try:       
         with open("stedfil.txt") as fil:
             reader = csv.reader(fil)
             for row in reader:
                   sted = Sted(*row)
                   stedliste.append(sted)      
         print ('Stedliste er lest fra fil' + '\n')
     except FileNotFoundError:
         print ('filen er ikke funnet'+'\n')       

#Printe ut alle avtaler i avtaleliste
def PrinteUtAlle(liste):
    if len(liste) !=0:
        indeks = 0
        for i in liste:
            indeks +=1
            print (f' Indeks nummer {indeks}:', end='')
            print (f'{i}' +'\n')
    else:
        print ('listen er tom' + '\n')
                
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
def fillAvtaler( n, steder, kategorier):
    now = datetime.now()
    avtaler  = []
    print(len(steder))
    print(len(kategorier))
    for i in range (n):
        #fyller ut avtaler med tilfeldig måned, dag, og tidspunkt
        nyAvtale = Avtale((f'''Avtale {i + 1}'''),steder[randint(0, len(steder)-1)], 
        datetime(now.year, randint(1, 12), randint(1, 28), randint(0, 23), randint(0, 59)), randint(0, 120) )
        for j in range (randint(0, 4)):
            nyAvtale.kategorier.append(kategorier[randint(0, len(kategorier)-1)])
        
        avtaler.append(nyAvtale)

    return avtaler


        
#fyller ut en liste med default kategorier
def fillKategorier():
    kategorier  = []
    navneliste = ["familie", "jobb", "venner", "skole", "borettslag", "trening"]
    for i in navneliste:
        id = randint(1, 100)
        NyKategori = Kategori((id), (f'''Kategori {i}'''))
        kategorier.append(NyKategori)
    return kategorier

#fyller ut en liste med n antall steder, for å slippe å lage en hel liste selv
def fillSteder( n = 5):
    steder  = []
    for i in range (n):
        #fyller ut steder med tilfeldige verdiger
        NySted = Sted((f'''{randint(1,100)}'''),(f'''Sted {i + 2}'''), (f'''Gatenavn {i + 3}'''), randint(1000,9999),
        (f'''Postested {i + 4}''') )
        steder.append(NySted)
    return steder

def finn_avtaler_paa_sted(id, avtaler):
    matches = []
    for avtale in avtaler:
        if avtale.place.id == id:
            matches.append(avtale)
    return matches

