#!/bin/bash

usage(){
    echo "$0 <montant> <nom vendeur>"
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

# Generation transactionID
if [ ! -e $2/transaction.id ]; then echo "0" >  $2/transaction.id; fi
transactionID=`cat $2/transaction.id`
transactionID=$(($transactionID+1))
echo $transactionID > $2/transaction.id

# Creation fichier
echo "$1\n$transactionID" > facture.txt
cat facture.txt | openssl dgst -sha256 -sign $2/private.key > facture.txt.sha256
tar czf $2/facture$transactionID.tgz facture.txt facture.txt.sha256 $2/banque.certif.tgz