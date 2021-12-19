from structure_file import File
from random import *

class Simulation_JBataille(): #code sous forme de classe car poo c'est mieux

    def __init__(self, configurationA=None, configurationB=None):
        self.vainqueur = None
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

        print("Joueur 1 :", self.main1, "[",self.main1.taille(),"]")
        print("Joueur 2 :", self.main2, "[",self.main2.taille(),"]")
        print("##################")

    def convertirListeToFile(self, l):
        F = File()
        for i in range(0, len(l), 1):
            F.enfile(l[i])
        return F

    def simulation(self): # fonction permettant de faire la simulation du jeu de bataille avec joueur 1 = main1 et joueur 2 = main2
        self.nombreTour=0
        while(self.vainqueur == None):
            print("####->", i)
            self.nombreTour = self.nombreTour + 1
            self.jeu()
        print("Vainqueur", self.vainqueur)

    def jeu(self, tas=[]):
        a_ = self.main1.defile()
        b_ = self.main2.defile()
        if (a_ == None):
            self.vainqueur = ("B", tas)
            return
        elif (b_ == None):
            self.vainqueur = ("A", tas)
            return
        a = int(str(a_)[1:]) #pour supprimer le 1er chiffre
        b = int(str(b_)[1:])
        tas.append(a_)
        tas.append(b_)
        print("Jeu de a: ", a_, "contre b: ", b_)
        print("Le tas ", tas)
        if(a>b):
            for i in tas:
                self.main1.enfile(i)
            tas.clear()
            print("A gagnant")
            print("A : ", self.main1, " B : ", self.main2)
            print("A [",self.main1.taille(),"]", "B [",self.main2.taille(),"]")
            return "A" #carte a gagnante
        elif(a<b):
            for i in tas:
                self.main2.enfile(i)
            tas.clear()
            print("B gagnant")
            print("A : ", self.main1, " B : ", self.main2)
            print("A [", self.main1.taille(), "]", "B [", self.main2.taille(), "]")
            return "B" #carte b gagnante
        else:
            tas.append(self.main1.defile()) #carte retournées lors de la bataille
            tas.append(self.main2.defile())
            print("* BATAILLE *")
            self.jeu(tas) #rejoue si bataille



si = Simulation_JBataille()
si.simulation()
