#!/usr/bin/env python

import random
import math
from gmpy import *
from mod import *

def generate_prime(size):
    n = int(random.uniform(pow(2,size-1),pow(2,size)))
    n |= 1 # on est sur que n est impair des le debut
    #n = Decimal(n)
    while not is_prime(n):
        n = n+2
    return n
