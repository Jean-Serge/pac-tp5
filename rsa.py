from rabin import millerRabin

import random


class RSA:
    def __init__(self, e, taille = 2048):
        self.e = e
        self.taille = taille

    def grand_premier(self):
        x = random.randint(1 << self.taille // 2, 1 << (self.taille // 2) + 1)
        while(True):
            if(millerRabin(x) == True):
                return x
            x = random.randint(1 << self.taille // 2, 1 << (self.taille // 2) + 1)
        
            
    def keyGen(self):
        p = self.grand_premier()
        q = self.grand_premier()

        self.p = p
        self.q = q
