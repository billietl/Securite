#!/usr/bin/env python

import rsa

BankPubKey = rsa.charger_cle("banque/public.key")

class Facture:
    def __init__(self, montant, nom_vendeur, transId=-1):
        certif = open(nom_vendeur+'/banque.certif', 'r').read()
        certif = rsa.dechiffrer(certif, BankPubKey).split('/', 4)

        if transId<0:
            try:
                transactionIdFile = open(nom_vendeur+'/transaction.id', 'r+')
                transId = transactionIdFile.readline()
                transId = float(transId)
            except IOError:
                print "Fichier inexistant. Creation d'un nouveau fichier."
                transactionIdFile = open(nom_vendeur+'/transaction.id', 'w')
                transId = 0
            except ValueError:
                print "fichier corrompu. J'espere que t'avais une sauvegarde parce que je te fais pas de facture la !"
                exit(2)
            #actualisation du futur id de transaction
            nextTransId = transId+1.0
            transactionIdFile.seek(0)
            transactionIdFile.truncate()
            transactionIdFile.write(str(nextTransId))

        self.montant = montant
        self.transactionID = transId
        self.nom_vendeur = nom_vendeur
        self.RIB = certif[1]

    def sauvegarder(self):
        kPriv = rsa.charger_cle(self.nom_vendeur+"/private.key")
        first_part = rsa.chiffrer(str(self.montant)+'/'+str(self.transactionID), kPriv)
        second_part = open(self.nom_vendeur+"/banque.certif").read()
        facture_file = open(self.nom_vendeur+'/facture'+str(int(self.transactionID))+'.fact', 'w+')
        facture_file.write(first_part+"\n"+second_part)
        facture_file.close()

def charger_facture(path):
    facture_file = open(path, 'r')
    facture_file_content = facture_file.read().split('\n', 2)
    facture_file.close()

    #separation entre facture et certificat
    facture_content = facture_file_content[0]
    certif_content = facture_file_content[1]
    
    #dechiffrement du certificat
    certif_content = rsa.dechiffrer(certif_content, BankPubKey).split('/', 4)
    HRId = certif_content[0]
    rib = certif_content[1]
    kPub = (int(certif_content[2]), int(certif_content[3]))

    #dechiffrement de la facture
    facture_content = rsa.dechiffrer(facture_content, kPub).split('/', 2)
    montant = facture_content[0]
    transactionId = facture_content[1]

    return Facture(montant, HRId, transactionId)


class Cheque:
    def __init__(self, facture, nom_client, vendeur_rib=None, montant=None, transactionID=None):
        certif = open(nom_client+'/banque.certif', 'r').read()
        certif = rsa.dechiffrer(certif, BankPubKey).split('/', 4)

        if not facture==None:
            self.vendeur_rib = facture.RIB
            self.montant = facture.montant
            self.transactionID = facture.transactionID
            self.nom_client = nom_client
        else:
            self.vendeur_rib = vendeur_rib
            self.montant = montant
            self.transactionID = transactionID
            self.nom_client = nom_client
        self.client_rib = certif[1]

    def sauvegarder(self):
        kPriv = rsa.charger_cle(self.nom_client+"/private.key")
        first_part = rsa.chiffrer(str(self.vendeur_rib)+"/"+str(self.montant)+'/'+str(self.transactionID), kPriv)
        second_part = open(self.nom_client+"/banque.certif").read()
        cheque_file = open(self.nom_client+'/cheque'+self.vendeur_rib+str(int(self.transactionID))+'.cheq', 'w+')
        cheque_file.write(first_part+"\n"+second_part)
        cheque_file.close()

def charger_cheque(path):
    cheque_file = open(path, 'r')
    cheque_file_content = cheque_file.read().split('\n', 2)
    cheque_file.close()

    #separation entre cheque et certificat
    cheque_content = cheque_file_content[0]
    certif_content = cheque_file_content[1]
    
    #dechiffrement du certificat
    certif_content = rsa.dechiffrer(certif_content, BankPubKey).split('/', 4)
    HRId = certif_content[0]
    rib = certif_content[1]
    kPub = (int(certif_content[2]), int(certif_content[3]))

    #dechiffrement du cheque
    cheque_content = rsa.dechiffrer(cheque_content, kPub).split('/', 3)
    vendeur_rib = cheque_content[0]
    montant = cheque_content[1]
    transactionId = cheque_content[2]

    return Cheque(None, HRId, vendeur_rib, montant, transactionId)

