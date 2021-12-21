from random import sample

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
        # return none si la file est vide
        if(self.debut == None):
            return None
        if(self.debut.suivant == None):
            value = self.debut
            self.debut = None
            value_ = value.valeur
            del value
            return value_
        else:
            m = self.debut
            while(m.suivant.suivant != None):
                m = m.suivant
            value = m.suivant
            self.fin = m
            self.fin.suivant = None
            value_ = value.valeur
            del value_
            return value.valeur

    def __str__(self):
        # str de la file, si vide alors false
        if (self.debut == None):
            return "Vide"
        else:
            return str(self.debut)

class Configuration():
    def __init__(self, cardsA=None, cardsB=None, heridity=None):
        self.Jcartes = []
        self.config = [[],[]] # main A et B

        for j in range(1, 5, 1): #cartes
            for i in range(7, 15, 1):
                self.Jcartes.append(100 * j + i)

        if(heridity!=None): #construire sur hérédité
            for i in heridity.getCards():
                self.Jcartes.remove(i)

        if (cardsA != None): #on ajoute les cartes predef de a et b
            self.addCards(cardsA)

        if (cardsB != None):
            self.addCards(cardsB, 1)

        L = sample(self.Jcartes, 16 - len(self.config[0])) #on complete le jeu A des cartes manquantes
        for i in L:
            if(i in self.Jcartes):
                self.Jcartes.remove(i)
        self.config[0] = self.config[0] + L

        L2 = sample(self.Jcartes, 16 - len(self.config[1])) #pareil avec Jeu B
        for i in L2:
            if(i in self.Jcartes):
                self.Jcartes.remove(i)
        self.config[1] = self.config[1] + L2

    def getCards(self):
        return self.config

    def addCard(self, cardNumber, l=0):
        if(len(self.config[l]) == 16):
            return "Configuration déjà pleine"
        else:
            self.config[l].append(cardNumber)
            self.Jcartes.remove(cardNumber)

    def addCards(self, cardList, l=0):
        for i in cardList:
            self.addCard(i, l)

class simulationData():
    def __init__(self):
        self.actions = []
        self.numberRound = 0
        self.numberBattle = 0
        self.mainA = None
        self.mainB = None
        self.winner = None

    def setWinner(self, winner):
        self.winner = winner

    def getWinner(self):
        return self.winner

    def setUpMain(self, cards, main):
        if(main == "A"):
            self.mainA = cards
        if(main == "B"):
            self.mainB = cards
        else:
            return "Erreur, veuillez choisir la main A ou B"

    def getMain(self, main):
        if (main == "A"):
            return self.mainA
        if (main == "B"):
            return self.mainB
        else:
            return "Erreur, veuillez choisir la main A ou B"

    def addBattle(self):
        self.numberBattle = self.numberBattle + 1

    def getBattles(self):
        return self.numberBattle

    def addRound(self):
        self.numberRound = self.numberRound + 1

    def getRounds(self):
        return self.numberRound

    def addAction(self, actionData):
        self.actions.append(actionData)

    def getActions(self):
        return self.actions

    def getDuration(self):
        return self.numberRound*10

    def getData(self):
        return (self.winner, self.numberRound, self.numberBattle, self.mainA, self.mainB, self.actions, self.getDuration())

    def __str__(self):
        return str(self.mainA)+str(self.mainB)
class actionData():
    def __init__(self, cardA, cardB, winner, tmain1, tmain2):
        self.cardA = cardA
        self.cardB = cardB
        self.winner = winner
        self.tmain1 = tmain1
        self.tmain2 = tmain2

    def getData(self):
        return (self.cardA, self.cardB, self.winner)

    def __str__(self):
        return ("J(A)"+"("+str(self.tmain1)+"):"+ str(self.cardA)+" contre J(B)"+"("+str(self.tmain2)+"): "+str(self.cardB)+ " # Vainqueur : "+ self.winner)

