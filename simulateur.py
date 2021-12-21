from simulation import Simulation_JBataille
from file_edit import *

class Simulateur():
    def __init__(self, nombreSimulations=1, configurationA=None, configurationB=None): #liste d'un maximum de 16 par joueur sans répétition de cartes
        self.nbSim = nombreSimulations
        self.simulationsData = []
        self.configurationA = configurationA
        self.configurationB = configurationB


    def runSimulations(self):
        for i in range(self.nbSim):
            si = Simulation_JBataille(configurationA=self.configurationA, configurationB=self.configurationB)
            self.simulationsData.append(si.getSimulationData())

    def dataFile(self):
        self.file = Txt_File()
        self.file.addText("#########################################")
        self.file.addText("Nombres de simulations :"+str(self.nbSim))
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
            self.file.addText("- Durée estimée de la partie : "+str(li[6]))
            self.file.addText("**")
            self.file.addText("- Historiques des mouvements :")
            for k in li[5]:
                self.file.addText(str(k))
            self.file.addText("********")


si = Simulateur(1)
si.runSimulations()
si.dataFile()
