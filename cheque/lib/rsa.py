#!/usr/bin/env python

from prime import *
from mod import *
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

def _bourrer(message, chunk):
    nb_pad = chunk - (len(message)%chunk)
    for i in xrange(0,nb_pad):
        message = message + chr(0)
    return message

def _chiffrer_octet(message, kPub):
   return pow(message, kPub[1], kPub[0])

def _int_to_string(integer, chunk):
    buffer = ''
    while integer>0:
        char = integer % pow(2,8)
        if not char == 0: buffer = buffer + chr(char)
        integer = integer / pow(2,8)
    if len(buffer)>chunk:
        raise Exception("Trop d'informations a extraire de cet integer !!")
    return buffer[::-1]

def _string_to_int(phrase, chunk):
    if len(phrase)>chunk:
        raise Exception("La taille de la phrase est plus grande que chunk (="+str(chunk)+")")
    buffer = 0
    for c in phrase:
        buffer = buffer + ord(c)
        buffer = buffer * pow(2, 8)
    return buffer

def _split_string(message, chunk):
    buffer = list()
    index = 0
    while index < len(message):
        buffer.append(message[index:index+chunk])
        index = index+chunk
    return buffer

def _chiffrer_string(message, kPub, chunk):
    buffer = ''
    index = 0
    message = _split_string(message, chunk)
    for morceau in message:
        in_buffer = _string_to_int(morceau, chunk)
        buffer = buffer + unichr(_chiffrer_octet(in_buffer, kPub))
        index = index+chunk
    return buffer

def chiffrer(message, kPub, chunk=4):
   if isinstance(message, (str,unicode)):
       message = _bourrer(message, chunk)
       return _chiffrer_string(message, kPub, chunk)
   if isinstance(message, int):
       return _chiffrer_octet(message, kPub)
   raise Exception('Arrete de me passer n\'importe quoi a chiffrer')

def _dechiffrer_octet(message, kPriv):
   return pow(message, kPriv[1], kPriv[0])

def _dechiffrer_string(message, kPriv, chunk):
   buffer = ''
   for c in message:
       output = _dechiffrer_octet(ord(c), kPriv)
       output_buffer = _int_to_string(output, chunk)
       buffer = buffer + output_buffer
   return buffer 

def dechiffrer(message, kPriv, chunk=4):
   if isinstance(message, (str,unicode)):
       return _dechiffrer_string(message, kPriv, chunk)
   if isinstance(message, int):
       return _dechiffrer_octet(message, kPriv)
   raise Exception('Arrete de me passer n\'importe quoi a dechiffrer')
