#!/usr/bin/env python
# coding: utf8
from simulateur import Simulateur
from tkinter import *

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

#color_bg = "#B4EDD2"
color_bg = "GRAY"
color_text = "#212227"
#window
wd = Window()
wd.setWindowSize(False, 400,500)
wd.setTitle("• Simulateur du jeu de la bataille")
wd.setCanResizable(False)
wd.setIcon("data/icon.ico")
wd.setBgColor("#B4EDD2")


#text
top_text = Text(wd.Window_Tk_Object(), 140, 35, bgcolor=color_bg, text="Simulateur", size=20, colortext=color_text)
top_text.setBold()
top_text.place(130,10)

#config_utils_menu
nbSim_text = Text(wd.Window_Tk_Object(), 160, 20, size=10, bgcolor=color_bg, text="• Nombres de simulations :", colortext=color_text)
nbSim_text.place(10, 60)

nbSim_entry = Entry(wd.get)

mainloop()