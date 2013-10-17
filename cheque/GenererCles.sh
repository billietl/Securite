#!/bin/bash

usage(){
    echo $0 "<taille de la cle> <dossier de sauvegarde>"
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

openssl genrsa $1 > "$2/private.key" 2>/dev/null
cat "$2/private.key" | openssl rsa -pubout > "$2/public.key" 2>/dev/null
