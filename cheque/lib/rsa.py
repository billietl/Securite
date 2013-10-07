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

def _bourrer(message, chunk=4):
    nb_pad = chunk - (len(message)%chunk)
    for i in xrange(0,nb_pad):
        message = message + chr(0)
    return message

def _chiffrer_octet(message, kPub):
   return pow(message, kPub[1], kPub[0])

def _int_to_string(integer, chunk=4):
    print integer
    octet_array = []
    while integer > 0:
        octet_array.append(integer & 0xFF)
        integer >>= 8
    l = len(octet_array)
    if chunk >= 1:
        octet_array = [0]*(chunk-l) + octet_array
    print "-->" + str(octet_array)
    return octet_array

def _string_to_int(phrase):
    print phrase
    print "-->" + str(int(''.join(['%02x' % i for i in phrase]), 16))
    return int(''.join(['%02x' % i for i in phrase]), 16)

def _chiffrer_string(message, kPub, chunk=4):
    buffer = ''
    index = 0
    while index < len(message):
        in_buffer = list()
        i = 0
        for i in xrange(0,chunk):
            in_buffer.append(ord(message[index+i]))
        index = index+chunk
        in_buffer = _string_to_int(in_buffer)
        buffer = buffer + unichr(_chiffrer_octet(in_buffer, kPub))
    return buffer

def chiffrer(message, kPub):
   if isinstance(message, (str,unicode)):
       message = _bourrer(message)
       return _chiffrer_string(message, kPub)
   if isinstance(message, int):
       return _chiffrer_octet(message, kPub)
   raise Exception('Arrete de me passer n\'importe quoi a chiffrer')

def _dechiffrer_octet(message, kPriv):
   return pow(message, kPriv[1], kPriv[0])

def _dechiffrer_string(message, kPriv, chunk=4):
   buffer = ''
   for c in message:
       output = _dechiffrer_octet(ord(c), kPriv)
       output_buffer = _int_to_string(output)
       buffer = buffer + str(output_buffer)
   return buffer

def dechiffrer(message, kPriv):
   if isinstance(message, (str,unicode)):
       return _dechiffrer_string(message, kPriv)
   if isinstance(message, int):
       return _dechiffrer_octet(message, kPriv)
   raise Exception('Arrete de me passer n\'importe quoi a dechiffrer')
