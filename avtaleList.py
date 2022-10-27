from avtale import Avtale
from inputHandler import *
import datetime
import random

class AvtaleList:
    def __init__(self, avtaler = []):
        self.avtaler = avtaler


    #fyller ut en liste med n antall avtaler, for å slippe å lage en hel liste selv
    def fillAvtaler(self, n = 5):
        now = datetime.datetime.now()
        for i in range (n):
            #fyller ut avtaler med tilfeldig måned, dag, og tidspunkt
            nyAvtale = Avtale((f'''Avtale {i + 1}'''),(f'''Sted  {i + 2}'''), 
            datetime.datetime(now.year, random.randint(1, 12), random.randint(1, 28), random.randint(0, 23), random.randint(0, 59)), random.randint(0, 120) )
            self.avtaler.append(nyAvtale)
            

    #sletter alle avtalene i listen
    def clearAvtaler(self):
        self.avtaler = []

    #sletter en avtale
    def deleteAvtale(self, n):
        if n+1 <= len(self.avtaler):
            self.avtaler.pop(n)
        else:
            return False

    #legger til en avtale
    def addAvtale(self, avtale):
        self.avtaler.append(avtale)

    def editAvtale(self, n):
        avtale = self.avtaler[n]
        print(f'''Rediger avtale {n+1}:
                (1)     Rediger navn
                (2)     Rediger sted
                (3)     Rediger start
                (4)     Rediger varighet
                ''')
        choice = input('Valg: ')
        if isValidChoice(choice, ['1', '2', '3', '4']):
            if choice == '1':
                nyttNavn = input('Gi nytt navn: \n')
                print(f'''
                Avtale "{avtale.name}" byttet til "{nyttNavn}"
                ''')
                avtale.name = nyttNavn
                print(f'{avtale} ')
            elif choice == '2':
                nyttSted = input('Gi nytt sted: \n')
                print(f'''
                Sted "{avtale.place}" byttet til "{nyttSted}"
                ''')
                avtale.place = nyttSted
                print(f'{avtale} \n')
            elif choice == '3':
                print('Angi ny start: \n')
                nyDato = inputDate()
                print(f'''
                Starttidspunkt "{avtale.start}" byttet til "{nyDato}"
                ''')
                avtale.start = nyDato
                print(f'{avtale} \n')
            elif choice == '4':
                nyVarighet = input('Gi ny varighet: \n')
                if isInt(nyVarighet):
                    print(f'''
                    Varighet "{avtale.duration}" byttet til "{nyVarighet}"             
                    ''')
                    avtale.duration = nyVarighet
                    print(f'{avtale} \n')
                else:
                    print('Skriv et tall')



