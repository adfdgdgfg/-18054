def cul(a,b,c):
	res = c(4,6)
	return res

c = lambda x,y : x+y

res = cul(1,2,c)

print(res)
