# -*- coding:utf-8 -*-

"""
TP5 PAC - Signature basée sur l'identité
"""

from client import *
from random import randint

import base64
import hashlib

NAME = 'monbailly'

URL = 'http://pac.bouillaguet.info/TP5/id-based-signature/'
server = Server(URL)


# ----------------------------------------------------------------------------
# Récupération du challenge
# -------------------------
response = server.query('KDC/PK')
print(response)

n = response['n']
e = response['e']

response = server.query('KDC/keygen/' + NAME)
print(response)

# ----------------------------------------------------------------------------
# Calcul de la signature
# -------------------------
key = response['secret-key']
r = randint(1, n-1)
t = pow(r, e, n)

# Octets de t
tmp_t = "{0:0512x}".format(t)
tmp_t = base64.b16decode(tmp_t, casefold=True)

# Octets du message
m = 'Hello world!'

hashe = m.encode() + tmp_t
hashe = hashlib.sha256(hashe).hexdigest()

s = (key * pow(r, int(hashe, base = 16), n)) % n

# Envoyer s, t et m
dic = {'s': s, 't':t, 'm':m}
response = server.query('check/' + NAME, dic)
print(response) # Status : OK
