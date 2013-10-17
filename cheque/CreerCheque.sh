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
tar xvf ../$1
tar xvf banque.certif.tgz
cd ../$tmpdir
# Verification
openssl dgst -sha256 -verify $tmpdir/public.key -signature $tmpdir/facture.txt.sha256 $tmpdir/facture.txt >/dev/null 2>/dev/null
validate=$?
# Extraction des données
montant=`cat $tmpdir/facture.txt | head -n 1`
transactionID=`cat $tmpdir/facture.txt | tail -n 1`
HRid=`cat $tmpdir/banque.certif | head -n 1`
RIB=`cat $tmpdir/banque.certif | head -n 2 | tail -n 1`
rm -rf $tmpdir
# Exit si signature fausse
if ! $validate
then
    echo "facture mal signée"
    exit 2
fi
# Interrogation humain
reponse="caca"
while [ ($reponse = "oui") -a ($reponse = "non") ]
do
    read -p "voulez-vous payer $montant euros a $HRid ? (oui/non)" reponse
done
if [ $reponse = "non" ]
then
    echo "paiement annulé"
    exit 3
fi
# Creation cheque
echo "$RIB\n$montant\n$transactionID" > cheque.txt
cat cheque.txt | openssl dgst -sha256 -sign $2/private.key > cheque.txt.sha256
tar czf $2/cheque$RIB$transactionID.tgz cheque.txt cheque.txt.sha256 $2/banque.certif.tgz
# Nettoyage
rn cheque.txt cheque.txt.sha256