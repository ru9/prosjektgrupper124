# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:22:01 2022

@author: alexa
"""
# Lagre avtale i en fil 
def SaveAvtale(Avtale):
  import pickle    
  with open ('Avtalefil.dat', 'wb') as fil:
     for i in Avtale:
         pickle.dump(i, fil)
  print ('Avtaleliste lagret i fil' + '\n')  
    
#Lese alle avtaler fra en fil til en liste "Avtaleliste" som må lages før funksjonen kalles
def ReadAvtale(avtaleliste):
    import pickle
    try:       
        with open('Avtalefil.dat', 'rb')  as fil:
          while True:
              try:
                  avtaleliste.append (pickle.load (fil))
              except EOFError:
                  break
        print ('Avtaleliste er lest fra fil' + '\n')
    except FileNotFoundError:
        print ('filen er ikke funnet'+'\n')
        


#Printe ut alle avtaler i avtaleliste
def PrinteUtAlle(avtaleliste):
    overskrift = input ('Skriv en overskrift for avtaleliste: ')
    print (overskrift)
    if avtaleliste:
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
    dato = input ('Skriv dato du vil se avtaler for, i format YYYY-MM-DD: ')
    for avtale in avtaleliste:
        avtaledato = str (avtale.start.date())
        if dato == avtaledato:
            dagens_avtaler.append (avtale)
    if len(dagens_avtaler) == 0:
        print (f'***Ingen avtaler er funnet for dato {dato}***'+'\n')
    else:
        print (f' Avtaler for dag {dato}', end='')
        for avtale in dagens_avtaler:
               print (f' {avtale} ')
    return dagens_avtaler
 
    
#printe ut og returnerer liste med alle avtalene som inneholder søkeord i tittel
def AvtaleMedSokeOrd (avtaleliste):
    avtaler_med_ord = []
    sokeord = input ('Skriv ord/setning som er del avtalenavn: ')
    for avtale in avtaleliste:   
        if sokeord.lower() in avtale.name.lower():
            avtaler_med_ord.append (avtale)
    if len(avtaler_med_ord) == 0:
        print (f'***Ingen avtaler inneholder sokeord "{sokeord}"***'+'\n')
    else:
        print (f' Avtaler som har "{sokeord}" i navnet:', end='')
        for avtale in avtaler_med_ord:
               print (f' {avtale} ')
    return avtaler_med_ord
    
    

 
