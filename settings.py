import os
import sys

class Settings():
    HOME  = None # Home page
    DOWN  = None # download page template
    CSS   = None # CSS file
    TITLE = None # html title
    DIR   = None # Directory that is being shared
    
    def __init__(self, settingsfile="settings.txt"):
        if not os.path.exists(settingsfile):
            # create file in that location
            sys.stderr.write("LOG -- " + settingsfile + " -- does not exist")
            
        elif os.path.isdir(settingsfile):
            sys.stderr.write("ERR -- " + settingsfile + " -- is a DIRECTORY")
        else:
            # we might have proper settings file here,
            # let's parse it
            parse_settings(settingsfile)

    def parse_settings(self, sf):
        
        print("lets parse some settings")
