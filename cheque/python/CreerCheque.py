#!/usr/bin/env python

import os
import sys
sys.path.append("./lib")
import rsa
import files

def usage():
    print "CreerCheque <fichier facture> <nom client>"
    exit(1)

def main():
    if len(sys.argv)<3:
        usage()
    if not os.path.isfile(sys.argv[1]):
        usage()
    if not os.path.isdir(sys.argv[2]):
        usage()

    nom_client = sys.argv[2]

    facture = files.charger_facture(sys.argv[1])

    reponse = "caca"
    while (not reponse=='oui') and (not reponse=='non'):
        reponse = raw_input("voulez-vous payer " + str(facture.montant) + "euros a " + facture.nom_vendeur + " ? (oui/non)")

    if reponse=='non':
        print "annulation du paiement"
        exit(2)
    cheque = files.Cheque(facture, nom_client)
    cheque.sauvegarder()

if __name__ == "__main__":
    main()

