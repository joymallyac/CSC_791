import math
from operator import itemgetter
from num import Num
from sym import Sym
from rows import Data


class cut:
    def __init__(self, n, c, lo, hi):
        self.stats = n
        self.mu = n.mu
        self.col = c
        self.lo = lo
        self.hi = hi

def withinCut(x, lo, hi):
    hi = hi or lo
    if x=="?":
        return False
    elif lo==hi:
        return x==lo
    else:
        return x>= lo and x<hi

def numBreaks(c, t):
    t.sort(key=itemgetter(c))
    lo, mid, hi = 0, math.floor(len(t)/2), len(t)-1
    return t[lo][c], t[mid][c], t[hi][c]

def numCuts(t, c, goal, cuts):
    lo,mid,hi = numBreaks(c,t.rows) 
    above     = Num()
    below     = Num()
    for _,cells in enumerate(t.rows):
        x = cells[c]
        y = cells[goal]
        what = withinCut(x,lo,mid) and below or above         
        what.numInc(y)
    cuts[len(cuts)-1] = cut(below,c,lo,mid)
    cuts[len(cuts)-1] = cut(above,c,mid,hi)

def symCuts(t, c, goal, cuts):
    tmp = {}
    for _,cells in enumerate(t.rows):
        x = cells[c]    
        y = cells[goal]
        try:            
            tmp[x].numInc(y)
        except:
            tmp[x] = Num()
            tmp[x].numInc(y)   
    for v,n in tmp.items():
      cuts.append(cut(n,c,v,v))


def bestCut(t):
    cuts = []
    goal = len(t.name)-1
    for c, name in enumerate(t.name):
        if t.indep(c):
            if (t.nums.get(c, 0) != 0):
                numCuts(t,c,goal,cuts)
            else:
                symCuts(t,c,goal,cuts)
    cuts.sort(key=lambda x: x.mu)
    return cuts[len(cuts)-1]



def fftClause(cut, t, pre):
    if(cut.lo == cut.hi):
        suffix = ""
    else:
        suffix = " < "  + str(cut.hi)    
    print ((pre or "if "), t.name[cut.col], "is", str(cut.lo) + suffix, "==>", math.floor(0.5+100*cut.mu))
