#!/usr/bin/env python

from prime import *
from mod import *

class NotImplementedYetError(Exception):
    pass

def generer_cles(taille):
   '''TODO : generer une paire de cles et renvoyer le tuple'''
   p = generate_prime(taille/2)
   q = generate_prime(taille/2)
   while p == q:
       q = generate_prime(taille/2)
   print "p et q confirmes"
   n = p*q
   phi = (p-1)*(q-1)
   e = 3
   while (not pgcd(e,phi) == 1) and (e < phi):
       print "calcul de e et d"
       e = e+2
   print "e et d trouves"
   d = invMOD(e, phi)
   return ((n,e),(n,d))

def chiffrer(message, kPub):
   '''TODO : chiffrer le message (string) avec kPub'''
   return message

def dechiffrer(message, kPriv):
   '''TODO : dechiffrer le message (string) avec kPriv'''
   return message
