
##
## To be merged with share.py after writing & debugging
##

import os
import sys

class Settings():
    # DEFAULT configurations
    settings = {
        'HOME'  : "home.pp",     # Home page
        'DOWN'  : "download.pp", # download page template
        'CSS'   : "style.css",   # CSS file
        'TITLE' : "PShare, by Robbe VDG",             # html title
        'DIR'   : os.path.join(os.getcwd(), "share")} # shared dir
    
    def __init__(self, settingsfile="settings.txt"):
        if not os.path.exists(settingsfile):
            # create file in that location
            sys.stderr.write("LOG -- " + settingsfile + " -- does not exist\n")
            try:
                self.create_settings_file(settingsfile)
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

    def __getitem__(key):
        # this method gets called when we use square brackets
        # example:
        # s = Settings()
        # print(s['HOME']) # will call this method with key='HOME'
        # The reason for this is estetics. Otherwise I could be calling
        # settins.Settings().settings somewhere. Not willing to write code
        # that ugly.
        return self.settings[key]

    def __setitem__(self, key, value):
        # mysettings[key] = value
        if self.settings.has_key(key):
            self.settings[key] = value
        else:
            sys.stderr.write("ERR -- Could not set setting -- "
                             + key + ": " + value + "\n")

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
            self.settings[var] = val


    def create_settings_file(self, sf="settings.txt"):
        f = open(sf, 'w')
        f.write(self.__str__())
        f.close()

    def __str__(self):
        """This method gets called when a Settings object is asked to convert to
        a string. It is also used to build the settings configurations file.
        """
        s  = "# Settings PShare\n"
        for key, value in self.settings.items():
            s += key + "=" + value + "\n"      
        return s
        
