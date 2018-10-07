from __future__ import division
from collections import defaultdict
from testFile import O
from rows import rows
import random, math, re, sys, operator

samples = 50


""" Selects any random row inside the range of the data"""
def anotherRow(x,t):	
	y = math.floor(random.random()*len(t))
	if x==y:
		return anotherRow(x,t)
	if t[y]:
		return t[y]
	return anotherRow(x,t)


""" function to calculate the dom score"""
def dom(data,row1,row2):
	s1,s2 = 0,0
	n = len(data.w)	
	for c,w in data.w.items():
		a0  = row1[c]
		b0  = row2[c]
		a   = data.nums[c].numNorm(a0)
		b   = data.nums[c].numNorm(b0)
		s1 -= 10**(w * (a-b)/n)
		s2 -= 10**(w * (b-a)/n)
	return s1/n < s2/n

""" Add the dom column and display the output """
def doms(data,onlyTen):
	if len(data.w) == 0: return
	n = samples
	c = len(data.name)	
	data.name.append(">dom")
	for r1,row1 in enumerate(data.rows):
		row1.append(0)
		for i in range(n):
			row2 = anotherRow(r1,data.rows) 
			s = dom(data,row1,row2) and 1/n or 0
			row1[c] += s
	return data

"""Print function """
def dump(a,sep = "\t"):
	for i in a:
		i[len(i)-1] = str("%.2f" % i[len(i)-1])
		print(sep.join(str(e) for e in i))


""" function to sort according to last column(dom score)"""
def sortByDom(row):
    return row[-1]


"""def mainDom(csv,onlyTen=False):
	doms(rows(csv),onlyTen)

@O.k
def test1():	
	print("\nweatherLong.csv\n")
	mainDom("data/weatherLong.csv",False)

@O.k
def test2():	
	print("\nauto.csv\n")
	mainDom("data/auto.csv",True)"""