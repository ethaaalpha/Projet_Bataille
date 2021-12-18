from structure_file import File
from random import *

class Simulation_JBataille(): #code sous forme de classe car poo c'est mieux

    def __init__(self, configurationA=None, configurationB=None):
        if(configurationA != None and configurationB != None):
            #lancement du jeu avec une configuration personalisée
            self.main1 = configurationA
            self.main2 = configurationB
            return
        else:
            #distribution
            self.distributionJeu()

    def distributionJeu(self):
        cartes = []
        for j in range(1,5,1):
            for i in range(7,15,1):
                cartes.append(100*j+i)
        self.main1 = sample(cartes, 16)
        self.main2 = []

        for i in range(0,32,1):
            if(cartes[i] not in self.main1):
                self.main2.append(cartes[i])

        self.main1 = self.convertirListeToFile(self.main1)
        self.main2 = self.convertirListeToFile(self.main2)

        print("Joueur 1 :", self.main1)
        print("Joueur 2 :", self.main2)

    def convertirListeToFile(self, l):
        F = File()
        for i in range(0, len(l), 1):
            F.enfile(l[i])
        return F

    def Jeu(self, a, b):
        a = int(str(a)[1:]) #pour supprimer le 1er chiffre
        b = int(str(b)[1:])
        if(a>b):
            return "A" #carte a gagnate
        elif(a<b):
            return "B" #carte b gagnante
        else:
            return "AB" #égalité



si = Simulation_JBataille()
si.Jeu(123,100)
