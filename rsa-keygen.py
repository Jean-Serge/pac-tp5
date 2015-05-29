# -*- coding:utf-8 -*-

"""
TP5 PAC - génération de clé RSA
"""

from client import *
from rsa import *



NAME = 'monbailly'

URL = 'http://pac.bouillaguet.info/TP5/RSA-keygen/'
server = Server(URL)

# ----------------------------------------------------------------------------
# Récupération du challenge et génération des clés RSA
# -------------------------
response = server.query('challenge/'+ NAME)
print(response)

rsa = RSA(response['e'])
rsa.keyGen()


dic = {'n':rsa.n, 'e':rsa.e}
response = server.query('PK/' + NAME, dic)

# ----------------------------------------------------------------------------
# Déchiffrement du message 
# -------------------------
cipher = response['ciphertext']


dic = {'m':rsa.decrypt(cipher)}
response = server.query('confirmation/' + NAME, dic)
print(response) # Status : OK

