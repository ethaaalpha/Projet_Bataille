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
        file = Txt_File()
        file.addText("###########")
        file.addText("Nombres de simulations :"+str(self.nbSim))
        file.addText("###########")
        print(self.simulationsData)
        for i in self.simulationsData:
            for j in i.getData():
                file.addText(str(j))
                if(type(j)=="actionData"):
                    for k in j:
                        file.addText(k)


si = Simulateur(2000)
si.runSimulations()
si.dataFile()
