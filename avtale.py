class Avtale:
    def __init__(self, name, place, start, duration):
        self.name = name
        self.place = place
        self.start = start
        self.duration = duration

    def __str__(self):
        return (f'''
        {self.name}
        At: {self.place}
        Start: {self.start}
        Duration: {self.duration} minutes''')
    
    #funksjon som returnerer avtale variabler på et format som er enkelt å lese inn fra fil
    def formatData(self):
        return [self.name, self.place, self.start, self.duration]

    
    
