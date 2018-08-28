from __future__ import division
from collections import Counter
from functools import partial
import traceback
import re
import random


class O:
  y=n=0
  @staticmethod
  def report():
    print("\n# pass= %s fail= %s %%pass = %s%%"  % (
          O.y,O.n, int(round(O.y*100/(O.y+O.n+0.001)))))
  @staticmethod
  def k(f):
    try:
      print("\n-----| %s |-----------------------" % f.__name__)
      if f.__doc__:
        print("# "+ re.sub(r'\n[ \t]*',"\n# ",f.__doc__))
      f()
      print("# pass")
      O.y += 1
    except:
      O.n += 1
      print(traceback.format_exc()) 
    return f


@O.k
def testingFailure():
  """this one must fail.. just to
  test if the  unit test system is working"""
  assert 1==2

@O.k
def testingSuccess():
  """if this one fails, we have a problem!"""
  assert 1==1

@O.k
def checkWhiteSpace():
	arr1 = [1,2,3]
	arr2 = [1,2,             3]
	sum1 = sum2 =0
	for i in range(0,len(arr1)):
		sum1 += arr1[i]
	for i in range(0,len(arr2)):
		sum2 += arr2[i]	
	assert sum1==sum2

@O.k
def regexSearch():
	flag = False
	string = "I like icecream"
	search = re.search(r'like', string)
	if search:
		flag = True
	assert flag == True

@O.k
def checkDivision():
	assert 5/2 == 2.5

@O.k
def checkStringoperations():
	str1 = "abc"
	str2 = "def"
	assert str1 < str2

@O.k
def checkException():
	flag = False
	try:
		x =  0 / 0
	except ZeroDivisionError:
		flag = True
	assert flag == True

@O.k
def checkLists():
	list1 = [1,2,3]
	list2 = ['a','b','c']
	list3 = list1 + list2	
	assert len(list3) == 6

@O.k
def checkTuples():
	a,b = 2+3,2*3
	assert a == 5 and b == 6

@O.k
def checkDictionary():
	tweet = {
				"user" : "joelgrus",
				"text" : "Data Science is Awesome",
				"retweet_count" : 100,
				"hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
			}
	tweet_keys = tweet.keys()
	assert len(tweet_keys) == 4 and len(tweet['hashtags']) == 5

@O.k
def checkCounter():
	c = Counter(['Dog','Cat','Rat','Dog','Eagle','Sparrow','Snake','Cat','Rat','Dog','Dog'])	
	assert c['Dog'] == 4 and c['Cat'] == 2

@O.k
def checkSets():
	list = [1,2,3,4,1,2,7,8,3,0,1,2,7]
	list_set = set(list)
	assert len(list_set) == 7

@O.k
def checkLoops():	
	for i in range(5,10):
		if (i % 2 == 0):
			break
	assert i == 6

@O.k
def checkBoolean():
	assert all([True, 1, {}]) is False and any([True, 1, {}]) is True


@O.k
def checkSorted():
	x = [1,5,6,3,2,8,9,0,6,7,4]
	x.sort()
	assert x[len(x) - 1] == 9

@O.k
def checkListComprehension():
	pairs = [(x,y)
			for x in range(5)
			for y in range(5)]
	assert len(pairs) == 25

@O.k
def checkGenerator():
	n = 1
	while True:
		yield n
		n += 1
		if n == 10:
			break
	assert n == 10

@O.k
def checkRandom():
	list1 = [0,1,2,3,4,5]
	random.shuffle(list1)
	assert list1[0] != 0

@O.k
def regexSearch():
	flag = False
	string = "I like icecream"
	search = re.search(r'like', string)
	if search:
		flag = True
	assert flag == True

class Set:
    def __init__(self, values=None):
        self.dict = {}

        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        return "Set: " + str(self.dict.keys())

    def add(self, value):
        self.dict[value] = True

    def contains(self, value):
        return value in self.dict

   

s = Set([10,20,30,40])
s.add(50)

@O.k
def checkOop():    
    assert s.contains(50) == True

def multiply(x, y): return x * y

@O.k
def checkMap():	
	p = map(multiply, [1, 2], [4, 5])
	for i in p:		
		assert i == 4
		break


documents = ['Dog','Cat','Rat','Dog','Eagle','Sparrow','Snake','Cat','Rat','Dog','Dog']

for i, document in enumerate(documents):
    if i == 5:
        tuple_test = (i, document)

@O.k
def checkEnumerate():    
    assert tuple_test == (5, "Sparrow")



if __name__== "__main__":
  O.report()