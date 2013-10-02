#!/usr/bin/env python

import sys

BankPubKey = '991'

#recuperation du nom de fichier de facture dont on veut realiser le chaque
factureFileName = sys.argv[1]

facture = open(factureFileName).read().split('\n', 2)
certifVendeur = rsa.dechiffrer(facture[1], BankPubKey).split('/')
#vendeurHRId = certifVendeur[0]
ribVendeur = certifVendeur[1]
pubKeyVendeur = certifVendeur[2]


facture = rsa.dechiffrer(facture[0], pubKeyVendeur).split('/')
montant = facture[0]
transactionId = facture[2]

#recuperation de la cle privee du client
cleClient = open('client.key', 'r').readline()


#chiffrage de la 1ere partie du cheque C(V.RIB+montant+transactionID, C.Kpriv)
#firstChequeParts = rsa.chiffrer(ribVendeur+'/'+montant+'/'+transactionId, cleClient)
firstChequeParts = 'firstParts'


#recuperation du certificat de la banque fournis au client
certif = open('banque.certif', 'r').readline()

#creation du cheque
open('cheque'+str(int(transId))+'.fact', 'w+').write(firstChequeParts+'\n'+certif)
