import pickle

class PrimeTester(object):
	'''As the name says,
	this is used for testing primality'''

	def __init__(self):
		self.__primes = [2,3,5,7,11,13]
		try:
			self.load(m = False)
		except:
			pass

	def __str__(self):
		'''showing how many prime numbers have been calculated'''
		length = len(self.__primes)
		last = self.__primes[-1]
		return "%s prime numbers have been calculated.\nThe last one is %s." %(length, last)

	def test(self, n):
		'''Test if n is a prime number'''

		if n == 1:
			return True
		elif n in self.__primes:
			return True
		elif int(n**0.5) <= self.__primes[-1]:
			for i in self.__primes:
				if n % i == 0:
					return False
			return True
		else:
			if n % 2 == 0: return False
			for i in range(3, int(n**0.5)+1, 2):
				if n % i == 0:
					return False
			return True

	def next(self, n = -1):
		'''Return next prime number
		if n is not given, starting from the last
		prime number in the [__primes] list.
		if n is given, starting from the given number'''

		if n < 0:
			num = self.__primes[-1] + 2
			while not self.test(num):
				num += 2
			self.end(num)
			return num
		else:
			if n <= self.__primes[-1]:
				if n % 2 == 0: n += 1
				else: n += 2
				while not self.test(n):
					n += 2
				return n
			else:
				while self.next() <= n: pass
				return self.__primes[-1]

	def qnext(self, n = -1):
		'''Quick next, not storing numbers
		to [primes]'''
		if n > 0:
			if n % 2 == 0: n += 1
			else: n += 2
			while not self.test(n):
				n += 2
			return n
		else:
			print("Argument required")

	def under(self, bound1 = 0, bound2 = 0):
		'''Return all numbers less than limit,
		minimum value can be specified'''

		if bound1 and bound2:
			return [i for i in self.__primes if bound1 <= i <= bound2]
		elif bound1:
			return [i for i in self.__primes if 0 <= i <= bound1]
		else:
			print("Limitation required")

	# def add(self, n):
	# 	'''Aid function
	# 	record result into the [__primes] list'''

	# 	self.__primes.append(n)
	# 	self.__primes.sort()

	def end(self, n):
		'''Aid function
		record result into the [__primes] list,
		knowing that n is just the next prime
		after the last element of [__primes]'''
		self.__primes.append(n)

	def save(self, s = "PTdata.pickle"):
		'''Aid function
		for reusability, [__primes] can be stored
		for later use'''

		f = open(s, "wb")
		pickle.dump(self.__primes, f)
		f.close()

	def load(self, s = "PTdata.pickle", m = True):
		'''Aid function
		load the [__primes] stored before'''
		try:
			f = open(s, "rb")
			self.__primes = pickle.load(f)
			f.close()
		except:
			if m: print("failed to load %s" %s)