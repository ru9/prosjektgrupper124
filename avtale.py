class Avtale:
    def __init__(self, name, place, start, duration):
        self.name = name
        self.place = place
        self.start = start
        self.duration = duration
        self.kategorier = []

    def __str__(self):
        return (f'''
        {self.name}
        At: {self.place}
        Start: {self.start}
        Duration: {self.duration} minutes''')
   
    #funksjon som returnerer avtale variabler på et format som er enkelt å lese inn fra fil
    def formatData(self):
        return [self.name, self.place, self.start, self.duration]
        
    def legg_til_kategori(self, kategori):
        self.kategorier.append(kategori)


class Kategori:
    def __init__(self, id, navn, prioritet = '1'):
        self.id = id
        self.navn = navn
        self.prioritet = prioritet


    def __str__(self):
        return (f'''
        id: {self.id}
        navn: {self.navn}
        prioritet: {self.translate_prio_to_str()}''')


    def translate_prio_to_str(self):
        if self.prioritet == '1':
            return str('Vanlig')
        elif self.prioritet == '2':
            return str('Viktig')
        elif self.prioritet == '3':
            return str('Svært viktig')
        else:
            return str('Ugyldig prioritet')


class Sted:
    
    def __init__(self, id, navn, gateadresse, postnummer, poststed):
        self.id = id
        self.navn = navn
        self.gateadresse = gateadresse
        self.postnummer = postnummer
        self.poststed = poststed
        
    def __str__(self):      
        return (f'''
        Stedet har id {self.id} 
        navn: {self.navn}. 
        Adressen: {self.gateadresse}
        {self.postnummer}
        {self.poststed}''')


