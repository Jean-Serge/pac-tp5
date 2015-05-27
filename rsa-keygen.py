# -*- coding:utf-8 -*-

"""
TP5 PAC - génération de clé RSA
"""

from client import *
from rsa import RSA


NAME = 'monbailly'

URL = 'http://pac.bouillaguet.info/TP5/RSA-keygen/'
server = Server(URL)

# ----------------------------------------------------------------------------
# Récupération du challenge
# -------------------------
response = server.query('challenge/'+ NAME)
print(response)

e = response['e']
print('e : ' + str(e))
rsa = RSA(e)
rsa.keyGen()
print(rsa.p)
print(rsa.q)
