#!/usr/bin/env python


#
# TODO: eveverything(implement stuff promised in README)
#

import SimpleHTTPServer
import SocketServer

class PShare(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def hello(self, ):
        pass
    
PORT = 80
httpd = SocketServer.TCPServer(("", PORT), PShare)
print( "Servering at port: " + str(PORT))
httpd.serve_forever()