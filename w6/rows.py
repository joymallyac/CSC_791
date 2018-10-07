
from num import Num
from testFile import O
from sym import Sym
import re, sys

class Data:
    
    def __init__(self):
        self.w = {}
        self.syms = {}
        self.nums = {}
        self._class = None
        self.rows = []
        self.name = []
        self._use = []
        self.indeps = []

    """ These are the independent columns """
    def indep(self, c):
        return self.w.get(c) is not None and self._class != c

    """ These are the dependent columns """
    def dep(self, c):
        return not self.indep(c)
        
    """ Reads and processes special symbols that define a table """
    def header(self, cells):
        for c0, x in enumerate(cells):
            if "?" not in x:
                c = len(self._use)
                self._use.append(c0)
                self.name.append(x)
                if re.search("[<>$]", x):
                    self.nums[c] = Num([])
                else: 
                    self.syms[c] = Sym([])
            if re.search("<", x):
                self.w[c] = -1
            elif re.search(">", x):
                self.w[c] = 1
            elif re.search("!", x):
                self._class = c
            else:
                self.indeps.append(c)
        return self
    
    """ function to add row (doing the number conversion and discarding the cells with unknown values)"""
    def row(self, cells):
        r = len(self.rows)
        self.rows.append([])
        for c, c0 in enumerate(self._use):
            x = cells[c0]
            if x != "?":
                if c in self.nums:
                    x = float(x)
                    self.nums[c].numInc(x)
                else:
                    self.syms[c].symInc(x)
            self.rows[r].append(x)
        return self

""" Loading data from Ram """
def lines(source):
    if source[-3:] in ["csv"]:
        with open(source) as fs:
            for line in fs:
                yield line

""" Prints the result """
def rows1(source):
    data = Data()
    first = True
    for line in source:        
        line = re.sub(r'[\t\r\n ]', '', line)
        line = re.sub(r'#.*', '', line)
        cells = line.split(",")
        if len(cells) > 0:
            if first: 
                data.header(cells)
            else: 
                data.row(cells)
            first = False
    print("#\tName\t\t n \t       mode \t       frequency")
    for k,v in data.syms.items():        
        print ("%d   %16s \t %d \t %10s \t %10.2f" % (k+1, data.name[k], v.n, v.mode, v.most))
    print("#\tName\t\t n \t       mu \t       sd")
    for k,v in data.nums.items():        
        print ("%d   %16s \t %d \t %10.2f \t %10.2f" % (k+1, data.name[k], v.n, v.mu, v.sd))
    return data


""" Reading data from disk and calling the print function """
def rows(source):
    _lines = lines(source)
    return rows1(_lines)

"""@O.k
def testRows():
    print("--------------------------weather.csv------------------------------")
    rows("data\weather.csv")
    print("--------------------------weatherLong.csv--------------------------")
    rows("data\weatherLong.csv")
    print("--------------------------auto.csv---------------------------------")
    rows('data\auto.csv')"""