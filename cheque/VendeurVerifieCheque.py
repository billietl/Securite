#!/usr/bin/env python

import os
import sys
sys.path.append("./lib")
import rsa
import files

def usage():
    print "VendeurVerifieCheque <fichier facture> <fichier cheque>"
    exit(1)

def __DENIED__(cheque):
    print "CE CHEQUE EST UN FAUX!!! "+cheque.nom_client+" ESSAIE DE T'ENFLER!!!"
    exit(666)

def main():
    if len(sys.argv)<3:
        usage()
    if not os.path.isfile(sys.argv[1]):
        usage()
    if not os.path.isfile(sys.argv[2]):
        usage()
    
    facture = files.charger_facture(sys.argv[1])
    cheque = files.charger_cheque(sys.argv[2])

    if not facture.RIB == cheque.vendeur_rib:
        __DENIED__(cheque)
    if not facture.montant == cheque.montant:
        __DENIED__(cheque)
    if not facture.transactionID == cheque.transactionID:
        __DENIED__(cheque)
    print "Seems legit."

if __name__ == "__main__":
    main()
