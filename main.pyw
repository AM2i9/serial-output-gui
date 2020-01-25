# Created by Patrick Brennan
# 2020
#-----------------------------

from tkinter import *
from tkinter import ttk
import tkinter.font as font
import os
import json
from serial import Serial

class guibtn:
    def __init__(self,master,txt,cmd):


        btn = Button(master, text=txt , bg='#0052cc', fg='#ffffff',command=lambda: App.sendSerial(App, cmd))
        btn['font'] = font.Font(size=60)

        btn.pack(side="top")

# Main application class
class App:
    def __init__(self, master):
        self.master = master
        self.config = open('config.json')
        global port
        global bau
        port = Entry(master)
        portlabel = Label(master, text="Serial Port:")
        baulabel = Label(master, text="Baudrate:")
        bau =  Entry(master)
        refresh = Button(master, text="Refresh", command=lambda: self.refresh())
        portlabel.pack(side="top")
        port.pack(side="top")
        baulabel.pack(side="top")
        bau.pack(side="top")
        refresh.pack(side="top")
        
        
    #Refreshes the GUI
    def refresh(self):
        global serport
        serport = Serial(port.get(), bau.get())
        self.config = open('config.json')
        c = 0
        r = 0
        configs = json.load(self.config)

        for i in configs:
            guibtn(self.master, i, configs[i][0])

    def sendSerial(clss, cmd):
        global serport
        serport.write(cmd.encode('ascii'))

root = Tk()
root.title("Serial Output")
application = App(root)
root.mainloop()