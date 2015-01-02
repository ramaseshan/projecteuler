if __name__ == '__main__':
	a,b = 1,2
	sum = 0
	for i in xrange(1000):
		b,a =  a+b, b
		if a < 4000000 and a%2 == 0:
			sum += a		
		if a > 4000000:
			break
	print sum
