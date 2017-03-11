#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
import os
import sys
import json

class IO:
    def __init__(self, server):
        self.server = server
        
    def successJson(self):
        response = {}
        response["success"] = True
        print response
        return response
    
    def _send(self, code, body, mimeType):
        server = self.server
        server.send_response(200)
        server.send_header('content-type ', mimeType)
        server.end_headers()
        server.wfile.write(body)
        server.wfile.close()
        #print body
        
    def sendJson(self, code, body):
        self._send(code, json.dumps(body), 'application/json')
        
    def send(self, code, body):
        self._send(code, body, 'text/html; charset=UTF-8')
        
    def render(self, path = 'index.html'):
        base_path = os.path.dirname(sys.modules[self.__class__.__module__].__file__)
        path = base_path + '/view/' + path
        file = open(path ,"r") 
        content =  file.read()
        file.close()
        return content
