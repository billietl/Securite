#!/bin/bash

usage(){
    echo "$0 <nom>"
    exit 1
}

if [ ! $# -eq 1 ]
then 
    usage
fi
if ! ls $1 >/dev/null
then
    usage
fi

tmpdir="tmp$RANDOM$RANDOM$RANDOM$RANDOM"
mkdir $tmpdir
cd $tmpdir

# Creation d'un nouveau RIB
newrib=$RANDOM$RANDOM
while grep -e $newrib ../banque/ribsFile >/dev/null
do
    newrib=$RANDOM$RANDOM
done
echo $newrib >> ../banque/ribsFile

# Creation du fichier
if [ -e ../$1/banque.certif.tgz ]; then rm ../$1/banque.certif.tgz; fi
echo "$1\n$newrib\n$cle" > ./banque.certif
cp ../$1/public.key .
cat ./banque.certif | openssl dgst -sha256 -sign ../banque/private.key > ./banque.certif.sha256
tar czf ../$1/banque.certif.tgz ./banque.certif ./banque.certif.sha256 ./public.key

# Nettoyage
cd ..
rm -r $tmpdir
