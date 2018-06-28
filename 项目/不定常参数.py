def d_sum(a,b,*args,**k):
	print(a)
	print(b)
	print(args)
	print(k)
	sum = 0
	sum = a + b

	for i in args:
		sum+=i
	for v in k.values():
		sum+=v
	return sum




