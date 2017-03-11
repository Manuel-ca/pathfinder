#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
from IO import IO 

class IO_User(IO):
    def action_user(self):
    #lire un fichier, et passe son contenu en réponse
        self.send(200, self.render())
        print 'Class user';
