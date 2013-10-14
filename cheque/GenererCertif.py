#!/usr/bin/env python

import os
import sys
import random
sys.path.append("./lib")
import rsa

def usage():
    print "GenererCertif.py <nom>"
    print "nom esta la fois le HRid de la personne et le dossier contenant une paire de cles rsa"
    exit(1)

def main():
    if len(sys.argv)<2:
        usage()
    if not os.path.isdir(sys.argv[1]):
        usage()

    HRid = sys.argv[1] 

    try:
        kPub = rsa.charger_cle(HRid+"/public.key")
    except Exception:
        print "Ce n'est certainement pas un dossier ou on trouve une paire de cles ca!"

    kPriv = rsa.charger_cle("banque/private.key")

    ribsFile = open('banque/ribsFile', 'r')

    ribnum = random.randint(100000000, 999999999)
    while ribnum in ribsFile.readlines():
        ribnum = random.randint(100000000, 999999999)
    ribsFile = open('banque/ribsFile', 'a')
    ribsFile.write(str(ribnum)+'\n')
    ribsFile.close()

    open(HRid+'/banque.certif', 'w').write(rsa.chiffrer(HRid+'/'+str(ribnum)+'/'+str(kPub[0])+'/'+str(kPub[1]), kPriv))

if __name__ == "__main__":
    main()
