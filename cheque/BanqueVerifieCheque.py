#!/usr/bin/env python

import os
import sys
sys.path.append("./lib")
import rsa
import files

def usage():
    print "BanqueVerifieCheque <fichier cheque>"
    exit(1)

def __DENIED__(cheque):
    print "CE CHEQUE EST UN FAUX!!! T'ES EN TRAIN DE TE FAIRE ENFLER!!!"
    exit(666)

def main():
    if len(sys.argv)<2:
        usage()
    if not os.path.isfile(sys.argv[1]):
        usage()
    
    cheque = files.charger_cheque(sys.argv[1])
    transactionsFile = open('banque/transactionsFile', 'r')
    transaction = str(cheque.vendeur_rib)+":"+str(cheque.transactionID)

    if transaction in transactionsFile.readlines():
        __DENIED__(cheque)
    print "Seems legit."
    transactionsFile = open('banque/transactionsFile', 'a')
    transactionsFile.write(transaction)

if __name__ == "__main__":
    main()
