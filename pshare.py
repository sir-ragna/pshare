
#
# Attempt to implement own version of a Request handler.
# Rewrite of share.py
# docs:
# http://docs.python.org/2/library/basehttpserver.html

import SocketServer
import BaseHTTPServer
import os
import cgi
import urllib
import sys
import posixpath
import shutil

class PShare(BaseHTTPServer.BaseHTTPRequestHandler):
    """Webserver that serves files from a dedicated folder."""

    def __init__(self, *args):
        # my own code that creates
        # an object that contains settings
        super().__init__(args)

    def do_GET(self):
        pass

    def do_HEAD(self):
        pass

    def send_file(self, f):
        """Send file(html or data) towards the requesting client"""
        shutil.copyfileobj(f, self.wfile)
        
