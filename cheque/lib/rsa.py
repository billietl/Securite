#!/usr/bin/env python

from prime import *
from mod import *
import struct

class NotImplementedYetError(Exception):
    pass

def generer_cles(taille):
   '''TODO : generer une paire de cles et renvoyer le tuple'''
   p = generate_prime(taille/2)
   q = generate_prime(taille/2)
   while p == q:
       q = generate_prime(taille/2)
   n = p*q
   phi = (p-1)*(q-1)
   e = 3
   while (not pgcd(e,phi) == 1) and (e < phi):
       e = e+2
   d = invMOD(e, phi)
   return ((n,e),(n,d))

def bourrer(message, chunk=4):
    nb_pad = chunk - (len(message)%chunk)
    for i in range(0,nb_pad):
        message = message + chr(0)
    return message

def _chiffrer_octet(message, kPub):
   return pow(message, kPub[1], kPub[0])

def _chiffrer_string(message, kPub, chunk=4):
    buffer = ''
    index = 0
    while index < len(message)
        i = 0
        for i in range (0,chunk):
            # Ajouter un octet au buffer
        # chiffrer buffer
        # ajout au buffer general
    # retour totalite

def chiffrer(message, kPub):
   if isinstance(message, (str,unicode)):
       message = bourrer(message)
       return _chiffrer_string(message, kPub)
   if isinstance(message, int):
       return _chiffrer_octet(message, kPub)
   raise Exception('Arrete de me passer n\'importe quoi a chiffrer')

def _dechiffrer_octet(message, kPriv):
   return pow(message, kPriv[1], kPriv[0])

def _dechiffrer_string(message, kPriv, chunk=4):
   buffer = ''
   for c in message:
       # on dechiffre
       # on decompose
       # on retourne

def dechiffrer(message, kPriv):
   if isinstance(message, (str,unicode)):
       return _dechiffrer_string(message, kPriv)
   if isinstance(message, int):
       return _dechiffrer_octet(message, kPriv)
   raise Exception('Arrete de me passer n\'importe quoi a dechiffrer')
