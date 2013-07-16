import settings
import os
import sys
import posixpath
import urllib
import cgi

pp = settings.Settings("settings.txt")
f = open("home.pp", 'r')
content = f.read()
print(pp)

d = dict (who = 'tim')
#print(content.format(**pp.settings))

"""
Produce Web page
-- Don't forget to add SELF to all function when copy pasting!!
"""

def construct_html_for_files(path, files, prefix=''):
    """Constructs a list tree for alle the files and folders.
    returns this in html
    """
    html = "<ul class=\"list\">\n"
    for f in files:
        fp = os.path.join(path, f) # file path, absolute
        rfp = os.path.join(prefix, f) # relative file path
        # print(rfp)
        if os.path.isdir(fp):
            # add '\', change classname & insert subdirs.
            html += "\t<li class=\"dir\"><a class=\"dir\" href=\"\\files\\{0}\"" \
                    " title=\"{1}\">{2}\\</a>\n\t{3}\t</li>\n" \
                    .format(urllib.quote(rfp), cgi.escape(fp), cgi.escape(f),
                            construct_html_for_files(fp, get_files(fp), rfp))
            ## I know this part is messy. Take your time to try to understand this.
            ## This thing grew organically and I wouldn't make something like this
            ## on purpose.
        else:
            html += "\t<li class=\"file\"><a class=\"file\" href=\"\\files\\{0}\"" \
                    " title=\"{1}\">{2}</a></li>\n" \
                    .format(urllib.quote(rfp), cgi.escape(fp), cgi.escape(f))
                    # note te \file\ prefix in the href.
    html += "</ul>\n"
    return html   
    

def get_files(path):
    path = posixpath.normpath(path)

    # before we do anything, let's do some check.
    # We never know what Timmy the no-clue-user might have done
    if not os.path.exists(path):
        sys.stderr.write("LOG -- Given SHARE directory does not exist." +
                         " Creating: " + path + "\n")
        try:
            os.mkdir(path) # tries to create missing directory.
        except OSError:
            sys.stderr.write("ERR -- ... and that failed."
                             + " (Could not create dir)\n")
            raise # We won't be handling this any further. Abort Abort

    elif not os.path.isdir(path):
        sys.stderr.write("ERR -- Should give directory instead of "
                         + " the file that you would like to share.\n")
        raise Exception("Bad configuration, should specify a directory."
                        + " Not a file") # you silly person
    
    # at this point we can be fairly certain we have a Directory ready to use.
    files = os.listdir(path)
    return files


path = pp["DIR"]
path = os.getcwd()
path = "C:\\Users\\robbe\\Desktop\\Q-Drivers"
print(path)
files = get_files(path)
print(files)
html = construct_html_for_files(path, files)
#print(html)
params = pp.settings
params.update( { 'CONTENT' : html } )
#print(content.format(**params))
f = open("myhtml.html", 'w')
f.write(html)
f.close()
