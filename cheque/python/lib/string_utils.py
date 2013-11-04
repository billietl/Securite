#!/usr/bin/env python

def _bourrer(message, chunk):
    nb_pad = chunk - (len(message)%chunk)
    for i in xrange(0,nb_pad):
        message = message + chr(0)
    return message

def _int_to_string(integer, chunk):
    '''Fonctionne avec _string_to_int'''
    buffer = ''
    while integer>0:
        char = integer % pow(2,8)
        if not char == 0: buffer = buffer + chr(char)
        integer = integer / pow(2,8)
    if len(buffer)>chunk:
        raise Exception("Trop d'informations a extraire de cet integer !!")
    return buffer[::-1]

def _string_to_int(phrase, chunk):
    '''Fonctionne avec _int_to_string'''
    if len(phrase)>chunk:
        raise Exception("La taille de la phrase est plus grande que chunk (="+str(chunk)+")")
    buffer = 0
    for c in phrase:
        buffer = buffer + ord(c)
        buffer = buffer * pow(2, 8)
    return buffer

def _split_string(message, chunk):
    '''Fonctionne'''
    buffer = list()
    index = 0
    while index < len(message):
        buffer.append(message[index:index+chunk])
        index = index+chunk
    return buffer
