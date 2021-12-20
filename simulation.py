import file_edit
from utils import *
from random import *
from file_edit import *

class Simulation_JBataille(): #code sous forme de classe car poo c'est mieux

    def __init__(self, configurationA=None, configurationB=None):
        self.vainqueur = None
        self.data = simulationData()

        config = Configuration(cardsA=configurationA, cardsB=configurationB).getCards()
        self.main1 = self.convertirListeToFile(config[0])
        self.main2 = self.convertirListeToFile(config[1])

        self.data.setUpMain(config[0], "A")
        self.data.setUpMain(config[1], "B")

        self.simulation()

        #mettre ne file
    def getSimulationData(self):
        return self.data

    def convertirListeToFile(self, l):
        F = File()
        for i in range(0, len(l), 1):
            F.enfile(l[i])
        return F

    def simulation(self): # fonction permettant de faire la simulation du jeu de bataille avec joueur 1 = main1 et joueur 2 = main2
        while(self.vainqueur == None):
            self.data.addRound()
            self.jeu()
            print(self.data.getRounds())
            if(self.data.getRounds() > 2000):
                self.data.setWinner("Egalité")
                self.vainqueur = "Egalité"

        self.data.setWinner(self.vainqueur)
        print("Gagnant de la simulation "+self.vainqueur)
    def jeu(self, tas=[]):
        a_ = self.main1.defile()
        b_ = self.main2.defile()
        if (a_ == None):
            self.vainqueur = ("B")
            return
        elif (b_ == None):
            self.vainqueur = ("A")
            return
        a = int(str(a_)[1:]) #pour supprimer le 1er chiffre
        b = int(str(b_)[1:])
        tas.append(a_)
        tas.append(b_)

        if(a>b):
            for i in tas:
                self.main1.enfile(i)
            tas.clear()
            self.data.addAction(actionData(str(a_), str(b_), "A"))
            return "A" #carte a gagnante

        elif(a<b):
            for i in tas:
                self.main2.enfile(i)
            tas.clear()
            self.data.addAction(actionData(str(a_), str(b_), "B"))
            return "B" #carte b gagnante
        else:
            tas.append(self.main1.defile()) #carte retournées lors de la bataille
            tas.append(self.main2.defile())
            self.data.addAction(actionData(str(a_), str(b_), "BATAILLE"))
            self.data.addBattle()
            self.jeu(tas) #rejoue si bataille


si = Simulation_JBataille()
print(si.getSimulationData())