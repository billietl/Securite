#!/bin/bash

usage(){
    echo $0 "<fichier facture> <nom client>"
    exit 1
}

clean(){
    cd ..
    rm -r $tmpdir
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
cd ./$tmpdir

# Extraction de la facture
if ! bash ../lib/evf.sh ../$1 ../banque/public.key
then
    clean
    exit 4
fi

# Extraction des donnees
montant=`cat ./facture.txt | head -n 1`
transactionID=`cat ./facture.txt | tail -n 1`
HRid=`cat ./banque.certif | head -n 1`
RIB=`cat ./banque.certif | head -n 2 | tail -n 1`

# Interrogation humain
reponse="caca"
while [ ! $reponse = "oui" -a ! $reponse = "non" ]
do
    read -p "voulez-vous payer $montant euros a $HRid ? (oui/non) " reponse
done
if [ $reponse = "non" ]
then
    echo "paiement annule"
    clean
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
clean
