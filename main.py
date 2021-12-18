from structure_file import File
from random import *

class Simulation_JBataille():
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

        print("Joueur 1 :", self.main1)
        print("Joueur 2 :", self.main2)
si = Simulation_JBataille()




def distribution():
    cartes = []
    for j in range(1,5,1):
        for i in range(7,15,1):
            cartes.append(100*j+i)
    main1 = sample(cartes, 16)
    main2 = []

    for i in range(0,32,1):
        if(cartes[i] not in main1):
            main2.append(cartes[i])

    main1 = creer_file(main1)
    main2 = creer_file(main2)

    return [main1,main2]

def creer_file(L):
    F = File()
    for i in range(0,len(L),1):
        F.enfile(L[i])
    return F

