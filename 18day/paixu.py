list = [10,12,13,500,61,1,8,4]

for i in range(0,len(list)-1):
	for j in range(i+1,len(list)):
		if list[i] > list [j]:
			list[i] , list[j] = list[j] , list[i] 
print(list)
