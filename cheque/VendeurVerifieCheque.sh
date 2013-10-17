#!/bin/bash

usage(){
    echo $0 " <fichier facture> <fichier cheque>"
    exit 1
}

clean(){
    cd ..
    rm $tmpdir
}

if [ ! $# -eq 2 ]
then 
    usage
fi
if [ ! -d $1 ]
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

# Extraction facture
mkdir facture
cd facture
tar xzf ../../$1
tar xzf banque.certif.tgz
cd ..

# Extraction cheque
mkdir cheque
cd cheque
tar xzf ../../$2
tar xzf banque.certif.tgz
cd ..

# Convertion en variables
rib_cheque=`cat cheque/cheque.txt | head -n 1`
rib_facture=`cat facture/banque.certif | head -n 2 | tail -n 1`
montant_cheque=`cat cheque/cheque.txt | head -n 2 | tail -n 1`
montant_facture=`cat facture/facture.txt | head -n 1`
tid_cheque=`cat cheque/cheque.txt | tail -n 1`
tid_facture=`cat facture/facture.txt | tail -n 1`

# Verifications
if [ $rib_cheque != $rib_facture ]
then
    echo "Le chèque ne t'es pas addressé !"
    clean
    exit 1
fi
if [ $tid_cheque != $tid_facture ]
then
    echo "Le chèque concerne une autre vente !"
    clean
    exit 1
fi
if [ $montant_cheque != $montant_facture ]
then
    echo "Le chèque n'a pas le bon montant !"
    clean
    exit 1
fi

# Nettoyage
clean

echo "Seems legit."
