from __future__ import division
from collections import defaultdict
from testFile import O
from rows import rows
from num import Num
from operator import itemgetter
import random, math, re, sys


unsuper_enough = 0.5
unsuper_margin = 1.05


def unsuper(data):
	rows = data.rows
	enough = len(rows)**unsuper_enough

	def band(c,lo,hi):
		if lo == 0:
			return ".." + str(rows[hi][c])
		elif hi == most:
			return str(rows[lo][c]) + ".."
		else:
		  return str(rows[lo][c]) + ".." + str(rows[hi][c])
 
	def argmin(c,lo,hi):
		cut  = None
		if (hi - lo > 2*enough):
			l,r = Num(), Num()
			for i in range(lo,hi+1): r.numInc(rows[i][c])
			best = r.sd
			for i in range(lo,hi+1):
				x = rows[i][c]
				l.numInc(x)
				r.numDec(x)
				if l.n >= enough and r.n >= enough:
					tmp = Num.numXpect(l,r) * unsuper_margin
					if tmp < best:
						cut,best = i, tmp
		return cut

	
	def cuts(c,lo,hi,pre):
		txt = pre + str(rows[lo][c]) + ".. " + str(rows[hi][c])
		cut = argmin(c,lo,hi)
		if cut:
			print(txt)
			cuts(c,lo,   cut, pre + "|.. ")
			cuts(c,cut+1, hi, pre + "|.. ")
		else:
			b = band(c,lo,hi)
			print(txt + " (" + b + ")")
			for r in range(lo,hi+1):
				rows[r][c]=b

	def stop(c,t):
		for i in range(len(t)-1,-1,-1): 
			if t[i][c] != "?" : return i
		return 0
	
	for c  in data.indeps:
		if c in data.nums:			
			rows.sort(key=itemgetter(c))
			most = stop(c,rows)			
			print("\n---- " + data.name[c] + ": " + str(most + 1) + "---------------\n")
			cuts(c,0,most,"|.. ")
	print(", ".join(data.name).replace("$","")) 
	dump(rows)	



def dump(a,sep = "\t"):
	for i in a:
		print(sep.join(str(b) for b in i))

def mainUnsuper(s):
	unsuper(rows(s))

@O.k
def test():
	print("\nweatherLong.csv\n")
	mainUnsuper("data/weatherLong.csv")