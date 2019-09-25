#7-1
'''
message = input("Which car do you want? ")
print("Let me see if I can find you a "+message)
'''
#7-2
'''
message = int(input("有多少人需要用餐？"))
if message > 8:
	print("没有空桌！")
else:
	print("有空桌！")
'''
#7-3
'''
message = int(input("输入一个数字，判断它是否是10的整数倍？"))
if message % 10 == 0:
	print(str(message)+"是10的整数倍。")
else:
	print(str(message)+"不是10的整数倍。")
'''
#7-4
'''
#prompt提示
prompt = "输入你想要的披萨配料："
prompt += "\n输入'quite'退出。\n"
active = True
while active:
	#ingredient配料
	ingredient = input(prompt)
	if ingredient != 'quite':
		print("我们会在披萨中添加"+ingredient.title()+"\n")
	else:
		active = False
'''
#7-5
'''
prompt = "\n输入您的年龄，根据年龄不同进行收费："
prompt += "\n 输入'quite'退出\n"
active = True
while active:
	age = input(prompt)
	if age == 'quite':
		break
	age = int(age)
	if age < 3:
		print("不收费！")
	elif age >= 3 and age <= 12:
		print("收10美元")
	else:
		print("收15美元！")
'''
#7-8
'''
sandwich_orders = ['01 sandwich','02 sandwich','03 sandwich']
finished_sandwich = []
while sandwich_orders:
	finish_sandwich = sandwich_orders.pop()
	print("I made your "+finish_sandwich+".")
	finished_sandwich.append(finish_sandwich)

print("\n所有三明治都制作好了！")
for sandwich in finished_sandwich:
	print("\t"+sandwich)
'''
#7-9
'''
sandwich_orders = ['01 sandwich','pastrami','02 sandwich','pastrami','pastrami','03 sandwich']
finished_sandwich = []
print("pastrami全部卖完了！")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
while sandwich_orders:
	finish_sandwich = sandwich_orders.pop()
	print("I made your "+finish_sandwich+".")
	finished_sandwich.append(finish_sandwich)

print("\n所有三明治都制作好了！")
for sandwich in finished_sandwich:
	print("\t"+sandwich)
'''
#7-10
'''
name_prompt = "\n您的名字是？"
place_prompt = "您想去的度假胜地？"
prompt = "\n你想邀请别人来参加调查吗？"

responses = {}

active = True
while active:
	name = input(name_prompt)
	place = input(place_prompt)
	responses[name] = place
	repeat = input(prompt+"(yes/no)")
	if repeat == 'no':
		active = False

print("********结果***********")
for name,place in responses.items():
	print(name+",你愿意去"+place+"吗？")
'''
x = True
y = False
z = False

if x or y and z:
    print("yes")
else:
    print("no")