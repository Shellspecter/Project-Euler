#Project Euler 7

#What is the 10 001st prime number?

def isPrime(n):
	if n == 1:
		return False
	#From 2 to n-1 	
	for i in range(2, n):
		if n%i == 0:
			return False
		
	return True
	
count = 0
n = 2
prime = 0

while count < 10001:
	if isPrime(n):
		count += 1
		prime = n
		print n
		
	n += 1
