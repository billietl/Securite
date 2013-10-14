#!/usr/bin/env python

import sys

#recuperation de montant passer en param et controle du type de valeur
try:
    montant = float(sys.argv[1])
except ValueError:
    raise "montant non numerique"

   
#recuperation de la cle privee du vendeur
cleVendeur = open('vendeur.key', 'r').readline()

#recuperation de l'id de transaction
transactionIdFile = open('transaction.id', 'r+')
try:
    transId = float(transactionIdFile.readline())
except ValueError:
    raise "ficher transaction.id corrompu"

#actualisation du futur id de transaction
nextTransId = transId+1.0
transactionIdFile.seek(0)
transactionIdFile.truncate()
transactionIdFile.write(str(nextTransId))


#chiffrage de la 1ere partie de la facture C(montant+transactionID, V.kpriv)
#firstFactureParts = rsa.chiffrer(str(montant)+'/'+str(transId), cleVendeur)
firstFactureParts = 'firstParts'

#recuperation du certificat de la banque fournis au vendeur
certif = open('banque.certif', 'r').readline()

#creation de la facture
open('facture'+str(int(transId))+'.fact', 'w+').write(firstFactureParts+'\n'+certif)
