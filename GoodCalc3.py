'''Imports'''
import math
from fractions import gcd
import random

'''Auxiliary Functions'''

def choose(x,y):
	return math.factorial(x)//((math.factorial(x-y)) * math.factorial(y))

def distl(array):
	return list(set(array))

'''Still slow, will fix later'''
def factor(number):
	return sorted([1,number] + list(map(int, ' '.join([str(i) + ' ' + str(n//i) for i in range(2,int(math.sqrt(number)) + 1) if n%i == 0]).split())))

def prime(n):
	if n%2 == 0: return 0
	for i in range(3,int(math.sqrt(n)) + 1,2):
		if n%i == 0:
			return 0
	return 1 if (n > 2) else 0

def pollardRho(N):
        if N%2==0:
                return 2
        x = random.randint(1, N-1)
        y = x
        c = random.randint(1, N-1)
        g = 1
        while g==1:
                x = ((x*x)%N+c)%N
                y = ((y*y)%N+c)%N
                y = ((y*y)%N+c)%N
                g = gcd(abs(x-y),N)
        return g


def pfactor(n):
	thelist = []
	while not(prime(n)):
		last = n
		while n == last:
			last = pollardRho(n)
		thelist.append(last)
		n//= last

	return sorted(thelist + [n])

rprime = lambda x,y: gcd(x,y) == 1
lcm = lambda x,y: x*y//gcd(x,y)

'''Main'''
vargs = {'answer':0 ,'e':math.e,'pi':math.pi}



class Main:

	def __init__(self, vargs, enter):
		self.input = enter
		self.vars = vargs

	def ParseP(self):
		start = 0
		end = -1
		while '(' in self.input:
			for n,i in enumerate(self.input):
				if i == '(':
					start = n
				elif i == ')':
					end = n
					break
			self.input = self.input.replace(self.input[start:end+1],str(Main.Eval(self, self.input[start+1:end])))
		return Main.Eval(self,self.input)
	
	def Eval(self,origin):
		if '/' not in origin:
			return eval(origin, self.vars)
		array = [eval(i,self.vars) if ('/' not in i) else i for i in origin.split()]
		beg = array[0][1:]
		if beg == 'aprime':
			return len(filter(prime, array[1:])) == len(a)
		elif beg == 'choose':
			return choose(array[1],array[2])
		elif beg == 'count':
			newlist = Main.listFunct(self,array[2:])
			return newlist.count(array[1])
		elif beg == 'distl':
			a = Main.listFunct(self, array[1:])
			return list(set(a))
		elif beg == 'factor':
			return factor(array[1])
		elif beg == 'prime':
			a = Main.listFunct(self, array[1:])
			return prime(a[0])
		elif beg == 'rprime':
			a = Main.listFunct(self, array[1:])
			return rprime(a[0],a[1])
		elif beg == 'pfactor':
			return pfactor(array[1])
	def listFunct(self,array):
		return [eval(str(i)) for i in array]



while 1:
	calculation = Main(vargs,input(">>> "))
	vargs['answer']= Main.ParseP(calculation)
	print(vargs['answer'])
