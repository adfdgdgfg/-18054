def print_s():
	for i in range(100,201):
		flag = 1
		for j in range(2,i):
			if i%j == 0:
				flag = 0
				break
		if flag == 1:
			print(i)
print_s()

