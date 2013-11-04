#!/usr/bin/env python

import os
import sys
sys.path.append("./lib")
import rsa
import files

def usage():
    print "CreerFacture <montant> <nom vendeur>"
    exit(1)

def main():
    if len(sys.argv)<3:
        usage()
    try:
        montant = float(sys.argv[1])
    except ValueError:
        usage()
    if not os.path.isfile(sys.argv[2]+"/private.key"):
        usage()
    vendeur = sys.argv[2]

    facture = files.Facture(montant, vendeur)
    facture.sauvegarder()

if __name__ == "__main__":
    main()
