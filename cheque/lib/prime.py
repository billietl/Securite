import random
import math

def pgcd(p, q):
    while q != 0:
        if p < q: (p,q) = (q,p)
        (p,q) = (q, p % q)
    return p

# Les 4 prochaines fonctions sont reprises d'une bibliotheque mathematique et modifiee pour correspondre a notre utilisation
def jacobi(a, b):
    '''Calculates the value of the Jacobi symbol (a/b) where both a and b are
    positive integers, and b is odd

    :returns: -1, 0 or 1
    '''

    assert a > 0
    assert b > 0

    if a == 0: return 0
    result = 1
    while a > 1:
        if a & 1:
            if ((a-1)*(b-1) >> 2) & 1:
                result = -result
            a, b = b % a, a
        else:
            if (((b * b) - 1) >> 3) & 1:
                result = -result
            a >>= 1
    if a == 0: return 0
    return result

def jacobi_witness(x, n):
    '''Returns False if n is an Euler pseudo-prime with base x, and
    True otherwise.
    '''

    j = jacobi(x, n) % n

    f = pow(x, n >> 1, n)

    if j == f: return False
    return True

def randomized_primality_testing(n, k):
    '''Calculates whether n is composite (which is always correct) or
    prime (which is incorrect with error probability 2**-k)

    Returns False if the number is composite, and True if it's
    probably prime.
    '''

    # 50% of Jacobi-witnesses can report compositness of non-prime numbers

    # The implemented algorithm using the Jacobi witness function has error
    # probability q <= 0.5, according to Goodrich et. al
    #
    # q = 0.5
    # t = int(math.ceil(k / log(1 / q, 2)))
    # So t = k / log(2, 2) = k / 1 = k
    # this means we can use range(k) rather than range(t)

    for _ in range(k):
        x = int(random.uniform(1, n-1))
        if jacobi_witness(x, n): return False
    
    return True

def is_prime(number):
    '''Returns True if the number is prime, and False otherwise.

    >>> is_prime(42)
    False
    >>> is_prime(41)
    True
    '''

    return randomized_primality_testing(number, 6)

def generate_prime(size):
    n = int(random.uniform(pow(2,size-1),pow(2,size)))
    n |= 1 # on est sur que n est impair des le debut
    while not is_prime(n):
        n = n+2
    return n
