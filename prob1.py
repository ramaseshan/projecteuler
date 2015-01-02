if __name__ == '__main__':
	sum = 0
	for num in xrange(1000):
		if num%3 ==0 or num%5 ==0:
			sum += num

	print sum
