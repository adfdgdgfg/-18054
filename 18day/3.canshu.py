list = [1,2,3,4,5,6,7]

min = 0
max = len(list) - 1
shu = 6 

while True:
	center =int((min + max) /2)
	if list[center] > shu:
		max = max - 1
	elif list[center] < shu:
		min = min + 1
	elif list[center] == shu:
		print("%d"%center)
		break
