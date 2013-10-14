#!/usr/bin/env python

import os
import sys
sys.path.append("./lib")
import rsa

def usage():
    print "GenererCles.py <taille de la cle> <dossier de sauvegarde>"
    exit(1)

def main():
    if len(sys.argv)<3:
        usage()
    if not sys.argv[1].isdigit():
        usage()
    if not os.path.isdir(sys.argv[2]):
        usage()
    kPub, kPriv = rsa.generer_cles(int(sys.argv[1]))
    rsa.sauvegarder_cles(kPub, kPriv, sys.argv[2])

if __name__ == "__main__":
    main()
