#!/usr/bin/env python

import sys

BankPubKey = '991'

#recuperation du nom de fichier du cheque à encaisser
chequeFileName = sys.argv[1]

#recuperation et decoupage du cheque
cheque = open(factureFileName).read().split('\n', 2)


certifClient = rsa.dechiffrer(cheque[1], BankPubKey).split('/')
#ClientHRId = certifClient[0]
ribClient = certifClient[1]
pubKeyClient = certifClient[2]


facture = rsa.dechiffrer(cheque[0], pubKeyClient).split('/')
ribVendeur = facture[0]
montant = facture[1]


#verification de l'authenticite du RIB 
if ribClient in open("ribsFile").read()
    if ribVendeur in open("ribsFile").read()
        #RIBs Authentique -> Transaction effectue
#sinon transaction non effectue
