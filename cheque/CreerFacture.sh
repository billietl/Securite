#!/bin/bash

usage(){
    echo "$0 <montant> <nom vendeur>"
    exit 1
}

if [ ! $# -eq 2 ]
then 
    usage
fi
if [ ! -d $2 ]
then
    usage
fi

tmpdir=tmp$RANDOM$RANDOM$RANDOM$RANDOM
mkdir $tmpdir
cd $tmpdir

# Generation transactionID
if [ ! -e ../$2/transaction.id ]; then echo "0" >  ../$2/transaction.id; fi
transactionID=`cat ../$2/transaction.id`
transactionID=$(($transactionID+1))
echo $transactionID > ../$2/transaction.id

# Creation fichier
echo $1 > facture.txt
echo $transactionID >> facture.txt
cat facture.txt | openssl dgst -sha256 -sign ../$2/private.key > facture.txt.sha256
cp ../$2/banque.certif.tgz .
tar czf ../$2/facture$transactionID.tgz facture.txt facture.txt.sha256 banque.certif.tgz

# Nettoyage
cd ..
rm -r $tmpdir
