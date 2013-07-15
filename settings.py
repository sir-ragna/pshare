
##
## To be merged with share.py after writing & debugging
##

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
            try:
                self.parse_settings(settingsfile)
            except IOError:
                sys.stderr.write("ERR -- Settings file could not be READ -- "
                                 + settingsfile + "\n")

    def parse_settings(self, sf):
        f = open(sf, 'r')
        lines = f.readlines()
        f.close()
        for l in lines:
            l = l.strip()
            if not l or l[0] == '#' or not '=' in l:
                # filter empty lines and lines that start as a comment
                continue
            lin = l.split('#', 1)[0] # strip trailing comments
            var = lin.split('=', 1)[0] # the variable name
            val = lin.split('=', 1)[1] # the value for that name

            # check variable and assign value
            if 'HOME' == var:
                self.HOME = val
            elif 'DOWN' == var:
                self.DOWN = val
            elif 'CSS'  == var:
                self.CSS = val
            elif 'TITLE' == var:
                self.TITLE = val
            elif 'DIR' == var:
                self.DIR = val
            else:
                sys.stderr.write("ERR -- line is not a valid SETTINGs line -- "
                                 + l + "\n")

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
        
pp = Settings()
