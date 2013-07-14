#!/usr/bin/env python


#
# TODO: eveverything(implement stuff promised in README)
#

import SimpleHTTPServer
import SocketServer
import os
import StringIO
import cgi
import urllib
import sys
import posixpath

class PShare(SimpleHTTPServer.SimpleHTTPRequestHandler):
    # template settings
    HTML = "index.pp"
    CSS = "style.css"
    TITLE = "PSHARE home"
    DIR = "C:/Users/robbe/Desktop"

    
    def list_directory(self, path):
        """Produce directory listing
        """
        try:
            print("list_dir::path is : " + path)
            lst = os.listdir(path)
        except os.error:
            self.send_error(404, "Permission denied")
            return None
        
        f = StringIO.StringIO()
        #displaypath = cgi.escape(urllib.unquote(self.path))
        f.write('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
        f.write("<html>\n<title>%s</title>\n" % self.TITLE)
        f.write("<hr>\n<ul>\n")
        for name in lst:
            fullname = os.path.join(path, name)
            displayname = linkname = name
            # Append / for directories or @ for symbolic links
            if os.path.isdir(fullname):
                displayname = name + "/"
                linkname = name + "/"
            if os.path.islink(fullname):
                displayname = name + "@"
                # Note: a link to a directory displays with @ and links with /
            f.write('<li><a href="%s">%s</a>\n'
                    % (urllib.quote(linkname), cgi.escape(displayname)))
        f.write("</ul>\n<hr>\n</body>\n</html>\n")
        length = f.tell()
        f.seek(0)
        self.send_response(200)
        encoding = sys.getfilesystemencoding()
        self.send_header("Content-type", "text/html; charset=%s" % encoding)
        self.send_header("Content-Length", str(length))
        self.end_headers()
        return f
        
    def translate_path(self, dir):
        """Translate the url /path/ to the OS filesystem path.
        """
       
        path = dir.split('?', 1)[0].split('#', 1)[0] # remove url params
        path = posixpath.normpath(urllib.unquote(path)) # unquote thingie
        
        # make sure the favicon.ico is found in the right folder
        if dir == '/favicon.ico':
            urlpath = os.getcwd() + "\\favicon.ico"
            return urlpath
            
        
        path = posixpath.normpath(self.DIR) + path
        sys.stderr.write("File REQUESTED -- " + path + "\n")
        return path
        
    
    def send_head(self):
        """Sends response code for GET & HEAD
        
        Returns a file object or None
        """
        
        path = self.translate_path(self.path)
        print("self.path:" + self.path)
        print("self.DIR:" + self.DIR)
        f = None
        if os.path.isdir(path):
            if not self.path.endswith('/'):
                self.send_response(301)
                self.send_header("Location", self.path + "/")
                self.end_headers()
                sys.stderr.write("err: " + str(self.path) + " misses a slash")
                return None
            return self.list_directory(path)
        ctype = self.guess_type(path)
        try:
            # Always read in binary mode. Opening files in text mode may cause
            # newline translations, making the actual size of the content 
            # transmitted less thatn the content-length!
            f = open(path, 'rb')
        except IOError:
            self.send_error(404, "File not found")
            return None
        self.send_response(200)
        self.send_header("Content-type", ctype)
        fs = os.fstat(f.fileno())
        self.send_header("Content-Length", str(fs[6]))
        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
        self.end_headers()
        return f
    
  

# Server settings
PORT = 80
httpd = SocketServer.TCPServer(("", PORT), PShare)
print( "Servering at port: " + str(PORT))
httpd.serve_forever()

