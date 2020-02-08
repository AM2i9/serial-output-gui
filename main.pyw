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
        btn['font'] = font.Font(size=30)

        btn.pack(side="top")

# Main application class
class App:
    def __init__(self, master):
        self.master = master
        self.config = open('config.json')
        global port
        global bau
        configFrame = Frame(master)
        configFrame.pack(side='top')
        port = Entry(configFrame)
        portlabel = Label(configFrame, text="Serial Port:")
        baulabel = Label(configFrame, text="Baudrate:")
        bau =  Entry(configFrame)
        refresh = Button(configFrame, text="Refresh", command=lambda: self.refresh())
        portlabel.pack(side="left")
        port.pack(side="left")
        baulabel.pack(side="left")
        bau.pack(side="left")
        refresh.pack(side="left")
        
 
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
root.minsize(500, 100)
application = App(root)
root.mainloop()