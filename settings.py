import os
import sys

class Settings():
    # DEFAULT settings
    HOME  = "home.pp"     # Home page
    DOWN  = "download.pp" # download page template
    CSS   = "style.css"   # CSS file
    TITLE = "PShare, by Robbe VDG"             # html title
    DIR   = os.path.join(os.getcwd(), "share") # Directory that is being shared
    
    def __init__(self, settingsfile="settings.txt"):
        if not os.path.exists(settingsfile):
            # create file in that location
            sys.stderr.write("LOG -- " + settingsfile + " -- does not exist\n")
            try:
                self.create_settings_file()
                sys.stderr.write("LOG -- Created settingsfile -- "
                                 + settingsfile + "\n")
            except IOError:
                sys.stderr.write("ERR -- Could not create -- "
                                 + settingsfile + "\n")
            
        elif os.path.isdir(settingsfile):
            sys.stderr.write("ERR -- " + settingsfile + " -- is a DIRECTORY\n")
        else:
            # we might have proper settings file here,
            # let's parse it
            self.parse_settings(settingsfile)

    def parse_settings(self, sf):        
        print("lets parse some settings")

    def create_settings_file(self, sf="settings.txt"):
        print(self)
        f = open(sf, 'w')
        f.write(self.__str__())
        f.close()

    def __str__(self):
        s  = "# Settings PShare\n"
        s += "HOME="  + self.HOME  + "\n"
        s += "DOWN="  + self.DOWN  + "\n"
        s += "CSS="   + self.CSS   + "\n"
        s += "TITLE=" + self.TITLE + "\n"
        s += "DIR="   + self.DIR   + "\n"
        return s
        
