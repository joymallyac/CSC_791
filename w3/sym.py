from __future__ import division
from testFile import O
import math

class Sym:    
    
    def __init__(self,symbolList):
        self.counts = {}
        self.mode = None
        self.most = 0
        self.n = 0
        self._ent = None
        [self.symInc(x) for x in symbolList]

        
    def symInc(self,x):
        if x == '?':
            return x
        self._ent = None
        self.n += 1
        old = self.counts.get(x)
        new = old and old + 1 or 1
        self.counts[x] = new
        if new > self.most:
            self.most = new
            self.mode = x
        return self

    def symDec(self, x):
        self._ent= None
        if self.n > 0:
            self.n -= 1
            self.counts[x] = (self.counts.get(x) - 1)
        return x
    
    def symEnt(self):
        if not self._ent:
            self._ent = 0
        for x, n in self.counts.items():
            p = n / self.n
            self._ent = self._ent - p * math.log(p,2)
            
        return self._ent    
    
    
@O.k
def testSym():    
    s = Sym(['y','y','y','y','y','y','y','y','y','n','n','n','n','n'])
    print (s.counts)
    assert (round(s.symEnt(), 2) == 0.94)