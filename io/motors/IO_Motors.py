#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
import requests
from IO import IO 

class IO_Motors(IO):
    def action_rotation_lat_more(self):
        self.sendJson(200, self.successJson())
    
    def action_rotation_lat_less(self):
        self.sendJson(200, self.successJson())
        
    def action_left(self):
        self.sendJson(200, self.successJson())
       
    def action_right(self):
        self.sendJson(200, self.successJson())


