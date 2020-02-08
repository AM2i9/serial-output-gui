### **Created by Patrick Brennan** ###
# **Serial Output Gui** # 



  This program was created for sending commands out through a computers serial ports easier. For instance, when setting up an Arduino, and   and it executes certain commands when it recives a certain message from serial. This could be used if you wanted a temporary solution     for a user interface.
  
  ## **Setup** ##
  
  The setup of the GUI is incredibly simple. The downloaded zip file from the [releases](https://github.com/AwesomeMiner291/serial-output-gui/releases) page contains an exe file named main.exe, and a      json file named config.json. The first thing you want to do, is open conifg.json. This can be done with a program like Notepad++,       Visual Studio or Visual Studio Code, or any other text editor that can open json files.
  
  Inside, you should see somthing that looks like this:
  
    {
      "Example":
          [
              "Command"
          ]
    }
    
   Now considering you know how JSON works, this next part should be pretty easy. To add a new configuration, simply create a new JSON object like "Example", and place a comma at the end bracket of the last command:
   
   
    {
      "Example":
          [
              "Command"
          ],
       "Example2":
          [
              "Command2"
          ]
    }
    
        
   The name of the object, or in this case, Example, is the name of the button. This is the text that will appear on the button to tell you what it is. The the attribute, or in this case, Command, is the command that will be sent to your serial port. For instance, if the command that was to be sent was "speak", then Command would be replaced with the string, "speak".
   
 ## **Usage** ##
 
 Once you have configured your buttons in config.json, which, by the way can be reconfigured at any time, you will want to open the second file in the download named main.exe. If windows says the program looks sketchy, and says you shouldn't run it, you can click on more info and run it anyway. I know this sounds sketchy, but I promise I'm not trying to steal your stuff.
 
 Next, you will see a gui similar to this:
 
![Start GUI](https://cdn.discordapp.com/attachments/675532248493326359/675532279375986709/unknown.png)
 
 As instructed by the GUI, you should enter the name of the serial port you are using to connect to your serial device. If you are using an Arduino, this can usually be found in the bottom right corner while connected to you board.
 
 Next, enter the baud rate. This varies from programs, as you usually have to set it when you open your serial device's ports. Enter what you have set it as here.
 
 Then, click refresh. When you click refresh, it will not only close and reopen the connection with your device, but it will also read through your config.json file and apply any changes you might have made.

When you hit refresh, as long as you have correct JSON format in the config, your buttons should appear as such:

![Refreshed GUI](https://cdn.discordapp.com/attachments/675532248493326359/675533781561770033/unknown.png)

Upon pressing these buttons, the command which you specified in config.json will be sent to your serial device.
