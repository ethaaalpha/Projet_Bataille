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
        self.debut = None
        self.fin = None

    def taille(self):
        # retourne la taille de la file
        if(self.debut == None):
            return 0
        m = self.debut
        i = 1
        while(m.suivant != None):
            m = m.suivant
            i = i+1
        return i

    def enfile(self, v):
        # pour ajouter élément à la file
        if(self.debut == None):
            self.debut = Maillon(v)
            self.fin = Maillon(v)
            return
        self.debut = Maillon(v, self.debut)

    def defile(self):
        # return false si liste vide
        if(self.debut == None):
            return False
        if(self.debut.suivant == None):
            value = self.debut
            self.debut = None
            return value.valeur
        else:
            m = self.debut
            while(m.suivant.suivant != None):
                m = m.suivant
            value = m.suivant
            self.fin = m
            self.fin.suivant = None
            return value.valeur

    def __str__(self):
        return str(self.debut.suivant)
