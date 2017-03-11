#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import sys, os
import cv2
import Image
import threading
from SocketServer import ThreadingMixIn
import StringIO
import time
import re
import requests

capture=None
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/app")
os.system("pyclean .")
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from config import web_srv_cfg
from Routing import routeur
class RequestHandler(BaseHTTPRequestHandler):
    
    def send_static(self):
		basedir = os.path.dirname(os.path.realpath(__file__)) 
		#.ttf?v=4.2.0
		sendReply = False
		sendVideo = False
		if self.path.endswith(".html"):
			mimetype='text/html'
			sendReply = True
		if self.path.endswith(".jpg"):
			mimetype='image/jpg'
			sendReply = True
		if self.path.endswith(".gif"):
			mimetype='image/gif'
			sendReply = True
		if self.path.endswith(".js"):
			mimetype='application/javascript'
			sendReply = True
		if self.path.endswith(".css"):
			mimetype='text/css'
			sendReply = True
		if self.path.endswith(".ico"):
			mimetype='image/x-icon'
			sendReply = True
		if self.path.endswith(".png"):
			mimetype='image/png'
			sendReply = True	
		if re.search('\\.woff(\\?.*)$', self.path):
			mimetype='application/x-font-woff'
			sendReply = True
		if re.search('\\.ttf(\\?.*)$', self.path):
			mimetype='application/octet-stream'
			sendReply = True
		if self.path.endswith(".mp4"):
			mimetype='video/mp4'
			sendReply = True
			sendVideo = True
			
			
		if sendReply == True:
			try:
				path = re.sub('(\\.[a-zA-Z0-9_]+)(\\?.*)$', r'\1', self.path, 2)
				if re.search('^/io/', path): 
					srcFile = basedir + path
				elif sendVideo:
					srcFile = basedir + "/video" + path
				else:
					srcFile = basedir + "/static" + path
				file = open(srcFile)
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(file.read())
			except ValueError:
				print ValueError
            #f.close()
		return sendReply
        
    #handle GET command
    def do_GET(self):
        if not self.send_static():
            self.applyCommand('GET', False)
    
    #handle POST command
    def do_POST(self):
        if not self.send_static():
            self.applyCommand('POST', True)
        
    
    def applyCommand(self, action, parsePost):
        routeur.route(self, action)
  
def run():
   print('Démarrage du serveur')
   httpd = HTTPServer((web_srv_cfg['ip'], web_srv_cfg['port']),RequestHandler)
   print('Le serveur est lancé')
   httpd.serve_forever()
  
if __name__ == '__main__':
    run()
  
