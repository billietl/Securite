#!/bin/bash

usage(){
    echo $0 "<fichier facture> <fichier cheque>"
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
if [ ! -e $1 ]
then
    usage
fi
if [ ! -e $2 ]
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
if ! bash ../../lib/evb.sh banque.certif.tgz ../../banque/public.key
then
    cd ..
    clean
    exit 4
fi
cd ..

# Extraction cheque
mkdir cheque
cd cheque
tar xzf ../../$2
if ! bash ../../lib/evb.sh banque.certif.tgz ../../banque/public.key
then
    cd ..
    clean
    exit 4
fi
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
    echo "Le cheque ne t'es pas addresse !"
    clean
    exit 1
fi
if [ $tid_cheque != $tid_facture ]
then
    echo "Le cheque concerne une autre vente !"
    clean
    exit 1
fi
if [ $montant_cheque != $montant_facture ]
then
    echo "Le cheque n'a pas le bon montant !"
    clean
    exit 1
fi

# Nettoyage
clean

echo "Seems legit."
