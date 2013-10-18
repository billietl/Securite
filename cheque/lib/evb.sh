#!/bin/bash

usage(){
    echo $0 "<archive> <cle publique banque>"
    exit 1
}

if [ ! $# -eq 2 ]
then 
    echo "1"
    usage
fi
if [ ! -e $1 ]
then
    echo "2"
    usage
fi
if [ ! -e $2 ]
then
    echo "3"
    usage
fi

tar xvf $1 >/dev/null

evb_HRid=`cat banque.certif | head -n 1`
evb_RIB=`cat banque.certif | head -n 2 | tail -n 1`

echo $evb_HRid >> ./banque.certif.bis
echo $evb_RIB >> ./banque.certif.bis
cat public.key >> ./banque.certif.bis

if ! diff -q banque.certif banque.certif.bis # les fichiers sont differents
then
    echo "La cle publique dans le certificat n'est pas celle signee !"
    exit 1
fi

if ! openssl dgst -sha256 -verify $2 -signature ./banque.certif.sha256 ./banque.certif >/dev/null
then
    echo "Le certificat a ete mofifie !"
    exit 2
fi
