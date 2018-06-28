import time 
def print_s():
	i = 0
	while True:
		i += 1
		if i%2 == 0:
			time.sleep(1)
			print("             我喜欢你             ")
		else:
			print_m()
def print_m():
	print("             爱你1314          ")
print_s()

