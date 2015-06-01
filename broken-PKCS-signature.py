# -*- coding:utf-8 -*-

"""
TP5 PAC - broken-PKCS-signature
"""

from client import *

NAME = 'monbailly'

URL = 'http://pac.bouillaguet.info/TP5/broken-PKCS-signature/'
server = Server(URL)


# ----------------------------------------------------------------------------
# Récupération de la clé publique
# -------------------------
response = server.query('PK')
print(response)

e = response['e']
n = response['n']
