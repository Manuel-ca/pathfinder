#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
from IO import IO 

class IO_Error(IO):
    def action_not_found(self):
        # lire un fichier, et passe son contenu en réponse
        self.send(404, 'ere')
        print 'Class error';
