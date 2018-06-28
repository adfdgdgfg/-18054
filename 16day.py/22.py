import math
def isprime(n):
	j = 3
	while j <= math.sqrt(n):
		if n%j == 0:
			return False
		j+=2
	return True
prime=[2]
prime.extend([k for k in range(3,300,2)if isprime(k)])

print (prime)

