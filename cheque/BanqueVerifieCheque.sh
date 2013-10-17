#!/bin/bash

usage(){
    echo $0 " <fichier cheque>"
    exit 1
}

clean(){
    cd ..
    rm -r $tmpdir
}

if [ ! $# -eq 1 ]
then 
    usage
fi
if [ ! -d $1 ]
then
    usage
fi

tmpdir=tmp$RANDOM$RANDOM$RANDOM$RANDOM
mkdir $tmpdir
cd $tmpdir

# Extraction des fichiers
tar xzf ../$1
tar xzf banque.certif.tgz

# Convertion en variables
rib=`cat cheque.txt | head -n 1`
transactionID=`cat cheque.txt | tail -n 1`

# Verification
transaction=$rib$transactionID

touch ../banque/transactionsFile
if grep -e $transaction ../banque/transactionsFile >/dev/null
then
    echo "Ce chèque a déjà été encaissé !"
    clean
    exit 1
fi
echo $transaction >> ../banque/transactionsFile

# Nettoyage
clean

echo "Seems legit."
