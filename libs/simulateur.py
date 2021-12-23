from simulation import Simulation_JBataille
from file_edit import *
from utils import Configuration
import os

class Simulateur(): #pour lancer plusieurs simulations à la suite
    def __init__(self, nombreSimulations=1, configurationA=None, configurationB=None, history=None, maxEq=200): #liste d'un maximum de 16 par joueur sans répétition de cartes
        self.nbSim = nombreSimulations
        self.simulationsData = []
        self.configurationA = configurationA
        self.configurationB = configurationB
        self.history = history
        self.maxEq = maxEq


    def runSimulations(self): #lancer les simulations
        for i in range(self.nbSim):
            si = Simulation_JBataille(configurationA=self.configurationA, configurationB=self.configurationB, history=self.history, maxEq=self.maxEq)
            self.simulationsData.append(si.getSimulationData())
            print(i)

    #partie gestion des données récupérées
    def getWinnerStats(self):
        vA = 0
        vB = 0
        vE = 0
        for i in range(len(self.simulationsData)):
            li = self.simulationsData[i].getData()
            if(str(li[0])=="A"):
                vA = vA+1
            if(str(li[0])=="B"):
                vB = vB+1
            if(str(li[0])=="Egalité"):
                vE = vE+1
        return (vA, vB, vE)

    def getNumberRounds(self): #
        nb = 0
        for i in range(len(self.simulationsData)):
            li = self.simulationsData[i].getData()
            nb = nb + int(li[1])
        return nb

    def getNumberBattles(self):
        nb = 0
        for i in range(len(self.simulationsData)):
            li = self.simulationsData[i].getData()
            nb = nb + int(li[2])
        return nb

    #pour créer le fichier texte
    def dataFile(self):
        self.file = Txt_File()
        self.file.addText("#########################################")
        self.file.addText("***")
        self.file.addText("Nombres de simulations : "+str(self.nbSim))
        self.file.addText("Nombres de victoires du joueur A : "+str(self.getWinnerStats()[0]) +" ("+str(round((self.getWinnerStats()[0]/self.nbSim)*100, 2))+"%)")
        self.file.addText("Nombres de victoires du joueur B : "+str(self.getWinnerStats()[1]) +" ("+str(round((self.getWinnerStats()[1]/self.nbSim)*100, 2))+"%)")
        self.file.addText("Nombres de parties nulle : "+str(self.getWinnerStats()[2]) +" ("+str(round((self.getWinnerStats()[2]/self.nbSim)*100, 2))+"%)")
        self.file.addText("***")

        self.file.addText("SN = Satistiques calculées en enlevant les parties nulles.")
        nombreRoundsSN = self.getNumberRounds()-(self.getWinnerStats()[2]*(self.maxEq+1))
        nombreSimSN = self.nbSim-self.getWinnerStats()[2]

        if(nombreSimSN == 0):
            nombreSimSN = 1
        self.file.addText("Nombres de plis moyens d'une partie (SN) : "+str(round(nombreRoundsSN/nombreSimSN)))
        self.file.addText("Nombres de batailles moyennes par partie : "+str(round(self.getNumberBattles()/int(self.nbSim))))
        self.file.addText("Durée moyenne d'une partie (SN) : "+str(round(nombreRoundsSN/nombreSimSN*10/60))+" minutes")
        self.file.addText("***")

        self.file.addText("#########################################")
        for i in range(len(self.simulationsData)):
            li = self.simulationsData[i].getData()
            self.file.addText("\n")
            self.file.addText("********")
            self.file.addText("- Simulation n'"+str(i+1))
            self.file.addText("- Joueur A : " +str(li[3]))
            self.file.addText("- Joueur B : " +str(li[4]))
            self.file.addText("- Vainqueur : "+str(li[0]))
            self.file.addText("- Nombre(s) de plis : "+str(li[1]))
            self.file.addText("- Nombre(s) de bataille(s) : "+str(li[2]))
            self.file.addText("- Durée estimée de la partie : "+str(round(li[5]/60))+" minutes")
            if(self.history == True):
                self.file.addText("**")
                self.file.addText("- Historiques des mouvements :")
                for k in li[6]:
                    self.file.addText(str(k))
            self.file.addText("********")

        self.file.close()#ferme l'instance d'édition du fichier

    def showFile(self): #permet d'ouvrir le fichier écrit (avec un éditeur de texte)
        os.startfile(os.getcwd()+"\\simulations\\"+self.file.txt_name)
