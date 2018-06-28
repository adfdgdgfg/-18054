def print_q(y):
	if y%400 == 0 or y%4 == 0 and y%100 != 0:
		print("%d是润年"%y)
	else:	
		print("不是润年")
y = int(input("输入年号"))
print_q(y)
