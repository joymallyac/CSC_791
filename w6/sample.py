from __future__ import division
from testFile import O
from math import floor
import random

""" # in lua means len() in python """
""" [:1] can be used for shallow copying """

class Sample:
    def __init__(self, sampleMax=10**32):
        self.max = sampleMax
        self.n = 0
        self.sorted = False
        self.some = []
    
    def sampleInc(self, x):
        self.n += 1
        now = len(self.some)
        if (now < self.max):
            self.sorted = False
            self.some.append(x)
        elif (random.random() < now /self.n):
            self.sorted = False
            self.some[floor(0.5 + random.random() * now) - 1] = x            
        return x       
    
    def sampleSorted(self):
        if not self.sorted:
            self.sorted = True
            self.some.sort()
        return self.some
    
    
    def nth(self, n):
        s = self.sampleSorted()        
        return s[ min(len(s), max(1,floor(0.5 + len(s)*n))) ]

    def nths(self,ns):
        ns = [0.1,0.3,0.5,0.7,0.9]
        out = []
        for n in enumerate(ns):
            out[len(out)+1] = nth(n)        
        return out

    

""" -----Test case to check reservoir sampling ------"""
"""@O.k
def sampleTest():
    random.seed(1)
    s = []
    s.append(Sample(2**7))        
    for i in range (1,1001):        
        y = random.random()        
        for t in s:
            t.sampleInc(y)
    
    for t in s:
        print (t.max, t.nth(0.5))
        assert abs(t.nth(0.5)-0.5) < 0.2"""

