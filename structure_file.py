class Maillon:
    def __init__(self, x, suivant = None):
        self.valeur = x
        self.suivant = suivant

    def __str__(self):
        if self.suivant != None:
            return str(self.valeur) + " - " + str(self.suivant)
        else:
            return str(self.valeur)

class File:
    def __init__(self):
        self.tete = None
        self.queue = None

    def taille(self):
        if(self.queue == None):
            return 0
        m = self.queue
        i = 1
        while(m.suivant != None):
            m = m.suivant
            i = i+1
        return i

    def enfile(self, v):
        if(self.tete == None):
            self.tete = Maillon(v)
            return
        if(self.queue == None):
            self.queue = Maillon(v, self.tete)
            return
        self.queue = Maillon(v, self.queue)

    def defile(self):
        if(self.tete == None):
            return "La liste est vide"
        m = self.queue
        while(m.suivant.suivant != None):
            m = m.suivant
        self.tete = m
        self.tete.suivant = None

    def concatener(self, file):
        if(self.tete == None):
            return file
        if(file.tete == None):
            return self
        self.tete.suivant = file.queue


