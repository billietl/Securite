#!/usr/bin/env python

import sys
import random

#cle publique du nouvel utilisateur
kPub = sys.argv[1] 
#hrid de l'utilisateur
hrid = sys.argv[2] 

ribsFile = open('ribsFile', 'r')

#genere un rib non utilise
ribnum = random.randint(100000000, 999999999)
while ribnum in ribsFile.readlines():
    ribnum = random.randint(100000000, 999999999)

ribsFile = open('ribsFile', 'a')
ribsFile.write(str(ribnum)+'\n')


open('user.certif', 'w').write(rsa.chiffrer(hrid+'/'+ribnum+'/'+kPub, cleBanque))

