# -*- coding:utf-8 -*-

"""
TP5 PAC - signature de Rabin
"""

from rsa import *
from client import Server


NAME = 'monbailly'
URL = 'http://pac.bouillaguet.info/TP5/Rabin-signature/'

server = Server(URL)
rsa = RSA()
rsa.keyGen()

# ----------------------------------------------------------------------------
# Récupération du challenge
# -------------------------
dic = {'n': rsa.n}
response = server.query('challenge/' + NAME, dic)
print(response)
