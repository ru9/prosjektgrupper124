# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 20:49:15 2022

@author: AOstebo
"""

class Sted:
    
    def __init__(self, id, navn, gateadresse, postnummer, poststed):
        self.id = id
        self.navn = navn
        self.gateadresse = gateadresse
        self.postnummer = postnummer
        self.poststed = poststed
        
    def __str__(self):
        return f"Stedet har id {self.id} og navn {self.navn}. Adressen er {self.gateadresse}, {self.postnummer}, {self.poststed}"
        
        
