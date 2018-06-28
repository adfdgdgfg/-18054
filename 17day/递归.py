def print_sum(a):
	if a == 1:
		return 1
	else:
		return	a*print_sum(a-1)


n = print_sum(5)
print(n)
