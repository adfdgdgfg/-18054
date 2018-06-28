list = []
def print_s(a,p):
	user={}
	if len(accout) == 11 and len(p) > 6 and a.starswith("1"):
		print("注册成功")
		user["a"]=a
		user["p"]=p
		list.append(user)
	else:
		print("注册失败")

def login(a,p):
	for i in list:
		if a == i["a"] and p == i["p"]:
			print("登录成功")
		else:
			print("登录失败")
a = input("请输入注册帐号")
p = input("请输入注册密码")
print_s(a,p)

if list:
	a = input("请输入帐号")
	p = input("请输入密码")
print_s(a,p)
