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

if ! bash ../lib/evb.sh banque.certif.tgz $2
then
    exit 4
fi

if ! openssl dgst -sha256 -verify public.key -signature ./facture.txt.sha256 ./facture.txt >/dev/null
then
    echo "La facture a ete mofifie !"
    exit 2
fi
