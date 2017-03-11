#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
#Importations standard
import os
import sys
import imp 
import inspect
import re
import types
from optparse import OptionParser
import inspect

os.system("pyclean .")
action = 'action_'
class_ditc = {}
for str_io_name in os.listdir("io/"):
    if os.path.isdir("io/" + str_io_name):
        str_io_class_name = 'IO_' + str_io_name.capitalize()
        str_io_class_path = 'io/' + str_io_name + '/'
        (file, filename, data) = imp.find_module(str_io_class_name,[str_io_class_path])
        klass = getattr(imp.load_module(str_io_class_name, file, filename, data), str_io_class_name)
        dico_actions = {}
        class_ditc[str_io_name] = {'klass':klass,'actions': dico_actions}
        for method in inspect.getmembers(klass, predicate=inspect.ismethod):
            if (method[0].startswith("action_")):
                dico_actions[method[0].replace("action_", "")] = method[0]


class Service :
    def get_controler(self,name):
        global class_ditc
        print 'name', name
        return class_ditc[name] if (name in class_ditc) else None
        
    def is_controler_action_exist(self,str_io_class_name,str_action):
        global class_ditc
        return True if ((str_io_class_name in class_ditc) and (str_action in class_ditc[str_io_class_name]['actions'])) else False


service = Service()
