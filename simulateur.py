from simulation import Simulation_JBataille

class Simulateur():
    def __init__(self, nombreSimulations=1, configurationA=None, configurationB=None): #liste d'un maximum de 16 par joueur sans répétition de cartes
        self.nbSim = nombreSimulations

        if(configurationA != None):


