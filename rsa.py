from rabin import millerRabin
from fractions import gcd

import random


def invmod(n,p):
    (n1,p1,u1,u2)=(n,p,1,0)
    while p1>0:
        q=n1//p1
        (n1,p1,u1,u2)=(p1,n1-q*p1,u2,u1-q*u2)
    return (u1%p)

    
class RSA:
    def __init__(self, e = None, taille = 2048):
        self.e = e
        self.taille = taille


    def grand_premier(self):
        """
        Génère un grand nombre premier (de taille / 2 bits)
        """
        x = random.randint(1 << self.taille // 2, 1 << (self.taille // 2) + 1)
        while(True):
            if(millerRabin(x) == True):
                return x
            x = random.randint(1 << self.taille // 2, 1 << (self.taille // 2) + 1)
        
            
    def keyGen(self):
        """
        Génère les clé RSA correspondant au e indiqué à la construction.
        """
        while(True):
            p = self.grand_premier()
            q = self.grand_premier()
            phi = (p - 1) * (q - 1)

            if(self.e != None):
                if(gcd(phi, self.e) == 1):
                    break
            else:
                for i in range (phi):
                    if(gcd(phi, i) == 1):
                        self.e = i
                        break
                break
            
        self.phi = phi
        self.d = invmod(self.e, self.phi)
        print(self.d)
        self.p = p
        self.q = q
        self.n = p * q

    def encrypt(self, m):
        """
        Retourne le chiffré du message m.
        """
        c = pow(m, self.e, self.n)
        return c
        
    def decrypt(self, c):
        """
        Retourne le message déchiffré du champs c.
        """
        m = pow(c, self.d, self.n)
        return m

