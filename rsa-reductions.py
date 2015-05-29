# -*- coding:utf-8 -*-

"""
TP5 PAC - réductions RSA
"""

from client import *

NAME = 'monbailly'

URL = 'http://pac.bouillaguet.info/TP5/RSA-reductions/'
server = Server(URL)

def isqrt(n):
    """ 
    renvoie le plus grand entier k tel que k^2 <= n. Méthode de Newton.
    """
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x
                                                                              
def factoriserN(n,phi):
    """
    Retrouve les facteurs de n à partir du système :
    p + q = n - phi + 1
    p * q = n
    """
    b = n - phi + 1
    sqrt = isqrt(b*b - 4*n)
    res1 = (-b - sqrt) // 2
    res2 = (-b + sqrt) // 2
    return res1,res2


# ----------------------------------------------------------------------------
# Récupération du challenge phi
# -------------------------
response = server.query('phi/challenge/'+ NAME)
print(response)

# ----------------------------------------------------------------------------
# Factorisation de n
# -------------------------
f1, f2 = factoriserN(response['n'], response['phi'])
dic = {'p': abs(f1)}
response = server.query('phi/check/' + NAME, dic)
print(response)


# ----------------------------------------------------------------------------
# Récupération du challenge d
# -------------------------
response = server.query('d/challenge/'+ NAME)
print(response)

d = response['d']
e = response['e']
n = response['n']
x = (d * e) - 1

i = 1
while(True):
    if(x % i == 0):
        phi = x % 1
        f1, f2 = factoriserN(n, phi) 
        if(f1 * f2 == n):
            dic = {'p': abs(f1)}
            try:
                response = server.query('d/check/' + NAME, dic)
            except ServerError:
                continue

            print(response)
            break

            
    i += 1


