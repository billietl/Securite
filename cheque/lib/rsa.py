#!/usr/bin/env python

from prime import *
from mod import *
from string_utils import _bourrer, _int_to_string, _string_to_int, _split_string
import struct

class NotImplementedYetError(Exception):
    pass

def generer_cles(taille):
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

def _chiffrer_octet(message, kPub):
   return pow(message, kPub[1], kPub[0])

def _chiffrer_string(message, kPub, chunk):
    output_buffer = ''
    message = _split_string(message, chunk)
    for morceau in message:
        in_buffer = _string_to_int(morceau, chunk)
        if in_buffer == 0:
            continue
        in_buffer = _chiffrer_octet(in_buffer, kPub)
        output_buffer = output_buffer + str(in_buffer) + ','
    return output_buffer[:-1]

def chiffrer(message, kPub, chunk=4):
   if isinstance(message, (str)):
       message = _bourrer(message, chunk)
       return _chiffrer_string(message, kPub, chunk)
   if isinstance(message, int):
       return _chiffrer_octet(message, kPub)
   raise Exception('Arrete de me passer n\'importe quoi a chiffrer')

def _dechiffrer_octet(message, kPriv):
   return pow(message, kPriv[1], kPriv[0])

def _dechiffrer_string(message, kPriv, chunk):
   retour = ''
   message = message.split(',')
   print "dechiffrage de :"
   print message
   for c in message:
       output_buffer = int(c)
       output_buffer = _dechiffrer_octet(output_buffer, kPriv)
       output_buffer = _int_to_string(output_buffer, chunk)
       retour = retour + output_buffer
   return retour 

def dechiffrer(message, kPriv, chunk=4):
   if isinstance(message, (str)):
       return _dechiffrer_string(message, kPriv, chunk)
   if isinstance(message, int):
       return _dechiffrer_octet(message, kPriv)
   raise Exception('Arrete de me passer n\'importe quoi a dechiffrer')
