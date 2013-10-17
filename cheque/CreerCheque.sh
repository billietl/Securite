#!/bin/bash

usage(){
    echo "$0 <fichier facture> <nom client>"
    exit 1
}

if [ ! $# -eq 2 ]
then 
    usage
fi
if ! ls $2 >/dev/null
then
    usage
fi

tmpdir=tmp$RANDOM$RANDOM$RANDOM$RANDOM

# Extraction de la facture
mkdir $tmpdir
cd ./$tmpdir
tar xvf ../$1 >/dev/null
tar xvf banque.certif.tgz >/dev/null
# Extraction des données
montant=`cat ./facture.txt | head -n 1`
transactionID=`cat ./facture.txt | tail -n 1`
HRid=`cat ./banque.certif | head -n 1`
RIB=`cat ./banque.certif | head -n 2 | tail -n 1`
# Exit si signature fausse
if ! openssl dgst -sha256 -verify ./public.key -signature ./facture.txt.sha256 ./facture.txt >/dev/null 2>/dev/null
then
    echo "facture mal signée"
    exit 2
fi
# Interrogation humain
reponse="caca"
while [ ! $reponse = "oui" -a ! $reponse = "non" ]
do
    read -p "voulez-vous payer $montant euros a $HRid ? (oui/non) " reponse
done
if [ $reponse = "non" ]
then
    echo "paiement annulé"
    exit 3
fi
# Creation cheque
echo $RIB > cheque.txt
echo $montant >> cheque.txt
echo $transactionID >> cheque.txt
cat cheque.txt | openssl dgst -sha256 -sign ../$2/private.key > cheque.txt.sha256
rm banque.certif.tgz
cp ../$2/banque.certif.tgz .
tar czf ../$2/cheque$RIB$transactionID.tgz cheque.txt cheque.txt.sha256 banque.certif.tgz

# Nettoyage
cd ..
rm -r $tmpdir
