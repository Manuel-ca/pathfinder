#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import urlparse
import re
from Service import service
import Service
import os.path
import inspect


class Routing:
    def route(self, server, action):
        obj_url = urlparse.urlparse(server.path)
        str_path = re.sub('^/|/$', '', obj_url.path, 2)
        array_path = str_path.split('/') if str_path else [] 
        lenght = len(array_path)
        if lenght :
            str_io_class_name = array_path[0]
        else :
            str_io_class_name = 'default'
        if lenght == 2:
            str_action = array_path[1]
        else :
            str_action = 'default'
            
        if not service.is_controler_action_exist(str_io_class_name, str_action): 
            str_io_class_name = 'error'
            str_action = 'not_found'
            
        self.apply_route(server, str_io_class_name, str_action)

    
    def apply_route(self, server, str_io_class_name, str_action): 
        ctrl_def = service.get_controler(str_io_class_name)
        obj = ctrl_def['klass'](server)
        func = getattr(obj, 'action_' + str_action)
        func()
        
        #getattr(service.get_controler(str_io_class_name)(), 'action_' + str_action)()
        
        
routeur = Routing()
