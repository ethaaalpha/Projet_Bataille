import datetime
from datetime import date
import os

#pour fichier txt
class Txt_File():
    def __init__(self):
        self.date = date.today()
        self.txt_name = str(self.date)+"_1"+".txt"

        if not (os.path.isdir("simulations")):
            os.mkdir("simulations")

        while(os.path.isfile("simulations/"+self.txt_name)): #si le fichier existe déjà
            value = self.txt_name.removesuffix(".txt")
            value = str(int(value[11:])+1)
            self.txt_name = str(self.date)+"_"+value+".txt"
        self.file = open("simulations/"+self.txt_name, "w")
        self.addText("### "+"Fichier créé le "+str(self.date)+" ###\n") #information de base

    def addText(self, text):
        self.file.write(text)
        self.file.write("\n")

    def close(self):
        self.file.close()


