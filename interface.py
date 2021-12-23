#!/usr/bin/env python
# coding: utf8
import sys
sys.path.insert(1, "libs/")
from simulateur import Simulateur
from tkinter import *
from tkinter import ttk,font, messagebox
from textwrap import wrap

class Window():
    def __init__(self):
        self.window = Tk()

    def Window_Tk_Object(self):
        return self.window

    def destroy(self):
        self.window.destroy()

    def setTitle(self, label):
        self.title = label
        self.window.title(label)

    def setBgColor(self, color):
        self.color = color
        self.window.configure(bg=color)

    def getScreenWidth(self):
        return self.window.winfo_screenwidth()

    def getScreenHeight(self):
        return self.window.winfo_screenheight()

    def setWindowSize(self, fullscreen=False, width=0, height=0):
        if(fullscreen!=False):
            self.window.attributes("-fullscreen", True)
        else:
            size = str(width)+"x"+str(height)
            self.window.geometry(size)
    def setCanResizable(self, value):
        self.window.resizable(value, value)

    def setCursor(self, cursor):
        self.window.config(cursor=cursor)

    def setIcon(self, icon):
        self.window.iconbitmap(icon)

    def update(self):
        self.window.update()

class Text():
    def __init__(self, window, width, height, bgcolor, text, size, colortext="WHITE"):
        self.canvas = Canvas(window, width=width, height=height, bg=bgcolor, closeenough=100, highlightthickness=0)
        self.text = text
        self.police = "Comic Sans Ms"
        self.size = size
        self.text_id = self.canvas.create_text(width/2, height/2, font=(self.police , size), text=text)
        self.changeColor(colortext)

    def grid(self, column=0, row=0, padx=0, pady=0):
        self.canvas.grid(column=column, row=row, padx=padx, pady=pady)

    def place(self, x, y):
        self.canvas.place(x=x, y=y)

    def setBold(self):
        self.canvas.itemconfig(self.text_id, font=(self.police, self.size, "bold"))

    def getActualText(self):
        return self.text

    def changeText(self, text):
        self.text = text
        self.canvas.itemconfig(self.text_id, text=text)

    def changeColor(self, color):
        self.canvas.itemconfig(self.text_id, fill=color)

    def getObject(self):
        return self.text_id

    def getCanvas(self):
        return self.canvas

    def destroy(self):
        self.canvas.destroy()

color_bg = "#B4EDD2"
color_text = "#212227"
#window
wd = Window()
wd.setWindowSize(False, 400,500)
wd.setTitle("• Simulateur du jeu de la bataille")
wd.setCanResizable(False)
wd.setIcon("data/icon.ico")
wd.setBgColor("#B4EDD2")


#text
top_text = Text(wd.Window_Tk_Object(), 210, 60, bgcolor=color_bg, text="Simulateur", size=30, colortext=color_text)
top_text.setBold()
top_text.place(95,10)

#config_utils_menu
nbSim_text = Text(wd.Window_Tk_Object(), 195, 25, size=12, bgcolor=color_bg, text="• Nombres de simulations :", colortext=color_text)
nbSim_text.place(10, 80)
nbSim_entry = Entry(wd.Window_Tk_Object(), width=8)
nbSim_entry.insert(0, 1)
nbSim_entry.place(x=5, y=105)

configA_text = Text(wd.Window_Tk_Object(), 210, 25, size=12, bgcolor=color_bg, text="• Configuration du joueur A :", colortext=color_text)
configA_text.place(10, 130)
configA_entry = Entry(wd.Window_Tk_Object(), width=64)
configA_entry.place(x=5, y=155)

configB_text = Text(wd.Window_Tk_Object(), 210, 25, size=12, bgcolor=color_bg, text="• Configuration du joueur B :", colortext=color_text)
configB_text.place(10, 190)
configB_entry = Entry(wd.Window_Tk_Object(), width=64)
configB_entry.place(x=5, y=215)

nbMaxEq_text = Text(wd.Window_Tk_Object(), 240, 25, size=12, bgcolor=color_bg, text="• Nombres de plis avant égalité :", colortext=color_text)
nbMaxEq_text.place(10, 250)
nbMaxEq_entry = Entry(wd.Window_Tk_Object(), width=6)
nbMaxEq_entry.insert(0, 200)
nbMaxEq_entry.place(x=5, y=275)

history_text = Text(wd.Window_Tk_Object(), 225, 25, size=12, bgcolor=color_bg, text="• Historiques des mouvements :", colortext=color_text)
history_text.place(10, 310)
history_list = ttk.Combobox(wd.Window_Tk_Object(), values=["Oui", "Non"])
history_list.current(1)
history_list.place(x=5, y=335)

def launch_command():
    nbSim = nbSim_entry.get()
    #test value nb Sim
    try:
        nbSim = int(nbSim)
        if(nbSim>100000): #limit
            messagebox.showerror("Erreur","Nombre de simulations trop importantes")
            return
    except:
        messagebox.showerror("Erreur","Valeur impossible pour le nombre de simulations")
        return

    #config A et B
    configA = getListFromEntry(configA_entry)
    if configA == False : return
    configB = getListFromEntry(configB_entry)
    if configB == False : return

    #pour le nombre max de plis avant égalité
    nbMaxEq = nbMaxEq_entry.get()
    try:
        nbMaxEq = int(nbMaxEq)
        if(nbMaxEq>4000): #limit
            messagebox.showerror("Erreur","Nombre de plis max avant égalité trop important")
            return
    except:
        messagebox.showerror("Erreur","Valeur impossible pour le nombre max de plis avant égalité")
        return

    #pour avoir l'historiques des mouvements
    history = history_list.get()
    if(history == "Oui"):
        history = True
    else:
        history = None

    Si = Simulateur(nombreSimulations=nbSim, configurationA=configA, configurationB=configB, history=history, maxEq=nbMaxEq)
    Si.runSimulations()
    Si.dataFile()
    Si.showFile()


def getListFromEntry(entry):
    item = entry.get()
    item = wrap(item, 4) #sépare tous les 4 caractères
    l = []
    try :
        for i in item:
            l.append(int(i.removesuffix(","))) #remove ,
    except:
        messagebox.showerror("Erreur", "Syntaxe de la configuration incorrecte ")
        return False

    if(len(l)>0):
        for i in l:
            if(len(str(i))!=3):
                messagebox.showerror("Erreur", "Syntaxe de la configuration incorrecte ")
                return False
            try:
                i = int(i)
            except:
                messagebox.showerror("Erreur", "Syntaxe de la configuration incorrecte ")
                return False
    return l

#109,312,407,110,413,411,409,113,412,307,108,410,309,208,209,114
#107,111,112,207,210,211,212,213,214,308,310,311,313,314,408,414

#411,208,211,314,109,209,407,414,112,313,312,111,412,113,107,214
#108,110,114,207,210,212,213,307,308,309,310,311,408,409,410,413

#button
ft = font.Font(family="Comic Sans Ms", size=20)
launch_button = Button(wd.Window_Tk_Object(), text="Lancer", bg="#8D94BA", font=ft, command=launch_command)
launch_button.place(x=145, y=390)

mainloop()