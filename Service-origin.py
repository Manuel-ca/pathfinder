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
class_ditc = {'action':'','controleur':''}
for str_io_name in os.listdir("io/"):
    if os.path.isdir("io/" + str_io_name):
        str_io_class_name = 'IO_' + str_io_name.capitalize()
        str_io_class_path = 'io/' + str_io_name + '/'
        (file, filename, data) = imp.find_module(str_io_class_name,[str_io_class_path])
        mod_io = imp.load_module(str_io_class_name, file, filename, data)
        klass = getattr(mod_io, str_io_class_name)
        for item in inspect.getmembers(str_io_class_name):
            string = str(item)
            if string.startswith("('action_"):
                action = (string.split(',',1)[0]).replace("('","").replace("'","")
                class_ditc['action'] = action
                class_ditc['controleur'] = klass  
                
print [key for key in locals().keys()
       if isinstance(locals()[key], type(sys)) and not key.startswith('__')]

        # commence par "action" si oui mettre dans tableau ou cle = nom de methode sans 
        #ensuite mettre tout ça dans class_dict)
        #il doit y avoir 6 controleurs et autant de classes action 
    
class Service :
    def getControler(name):
        global class_ditc
        return (name in class_ditc) if class_ditc[name] else None
        
    def is_controler_action_exist(self,str_io_class_name,str_action):
        if str_io_class_name in class_ditc.keys():
            print str_io_class_name,"est présent"
        else :
            print "erreur 404"
            
    def get_controler(self,str_io_class_name):
        print str_io_class_name
        
service = Service()
