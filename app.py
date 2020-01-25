# Created by Patrick Brennan
# 2020
#-----------------------------

from tkinter import *
from tkinter import ttk
import tkinter.font as font
import os
import json
from serial import Serial

# A class to create the buttons on the gui
class guibtn:
    def __init__(self,master,txt,cmd):

        btn = Button(master, text=txt , bg='#0052cc', fg='#ffffff',command=lambda: App.sendSerial(App, cmd))
        btn['font'] = font.Font(size=60)

        btn.pack()

# Main application class
class App:
    def __init__(self, master):
        global serport
        self.master = master
        self.config = open('config.json')
        serport = Serial('COM3', 9600)
        self.refresh()
        
        
    #Refreshes the GUI
    def refresh(self):

        self.config = open('config.json')
        c = 0
        r = 0
        configs = json.load(self.config)

        for i in configs:
            guibtn(self.master, i, configs[i][0])

    def sendSerial(clss, cmd):
        global serport
        serport.write(cmd.encode('ascii'))
