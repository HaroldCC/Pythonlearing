#10-1
'''
file_name = 'C:\\Users\\19211\\Desktop\\python\\.vscode\\learning_python.txt'

#第一次打印
print("第1次：")
with open(file_name) as file_object:
	message = file_object.read()
	print(message)

#第二次
print("第2次：")
with open(file_name) as file_object:
	for line in file_object:
		print(line.strip())

#第三次
print("第3次：")
with open(file_name) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.strip())
'''
#10-2
'''
file_name = r'C:\\Users\\19211\\Desktop\\python\\.vscode\\learning_python.txt'

print("第1次：")
with open(file_name) as file_object:
	lines = file_object.readlines()

for line in lines:
	line = line.strip()
	print(line.replace('Python','C'))
'''
#10-3
'''
input_name = input("输入您的名字：")


file_name = 'guest.txt'

with open(file_name,'w') as file_object:
	file_object.write(input_name)
'''
#10-4
'''
file_name = 'guest_book.txt'

while True:
	input_name = input("输入您的名字：")
	if input_name == 'quite':
		break
	else:
		with open(file_name,'a') as file_object:
			file_object.write(input_name+"\n")
		print("Hello "+input_name+"!")
'''
#10-5
'''
file_name = 'all_resons.txt'

print("\n输入'quite'退出")
while True:
	name = input("输入您的名字：")
	if name == 'quite':
		break
	resons = input("您为何喜欢编程？")
	if name == 'quite':
		break
	else:
		with open(file_name,'a') as file_object:
			file_object.write(name+":"+resons+"\n")
		print(name+resons)
'''
#10-6
'''
print("输入2个数字进行相加！")
try:
	first_num = input("first_num:")
	first_num = int(first_num)
	second_num = input("second_num:")
	second_num = int(second_num)
except ValueError:
		print("非数值！重新输入！")
else:
	sum = first_num + second_num
	print("结果为："+str(sum))
'''
#10-7
'''
print("输入2个数字进行相加！输入'quite'退出！")
while True:
	try:
		first_num = input("first_num:")
		if first_num == 'quite':
			break
		first_num = int(first_num)
		second_num = input("second_num:")
		if second_num == 'quite':
			break
		second_num = int(second_num)
	except ValueError:
		print("数值类型错误！")
	else:
		sum = first_num + second_num
		print(sum)
'''
#10-8
'''
file_names = ['cats.txt','dogs.txt']
for file_name in file_names:
	print("\nReading file:"+file_name)
	try:
		with open(file_name) as file_object:
			message = file_object.read()
			print(message)
	except FileNotFoundError:
		print(file_name+"不存在！")
'''
#10-9
'''
file_names = ['cats.txt','dogs.txt','dogs1.txt']
for file_name in file_names:
	try:
		with open(file_name) as file_object:
			message = file_object.read()
	except FileNotFoundError:
		pass
	else:
		print("\nReading file:"+file_name)
		print(message)
'''
#10-10
'''
file_name = 'Text.txt'
try:
	with open(file_name) as file_object:
		contents = file_object.read()
except FileNotFoundError:
	print(file_name+"文件不存在！")
else:
	#计算文件中单词个数
	words = contents.split()
	num_words = len(words)
	print("文件"+file_name+"包含"+str(num_words)+"个单词！")

	#计算文件中某单词出现次数
	word_times = contents.lower().count('the')
	print("单词'the'在文件"+file_name+"中出现了"+str(word_times)+"次。")
'''
#10-11
'''
import json

#写入
like_number = input("输入您喜欢的数字：")

with open('favorite_number.json','w') as file_object:
	json.dump(like_number,file_object)
	print("喜欢的数字已保存！")

#读取
file_name = 'favorite_number.json'
with open(file_name) as file_object:
	number = json.load(file_object)

print("最喜欢的数字是"+str(number))
'''
#10-12
'''
import json

try:
	with open('favorite_number.json') as file_object:
		number = json.load(file_object)
except FileNotFoundError:
	number = input("您最喜欢的数字是：")
	with open('favorite_number.json','w') as file_object:
		json.dump(number,file_object)
	print("数字已保存!")
else:
	print("您最喜欢的数字是"+str(number))
'''
#10-13
import json 

def get_sorted_username():
	"""如果存储了用户名，就获取它"""
	file_name = 'user_name.json'
	try:
		with open(file_name) as target:
			user_name = json.load(target)
	except FileNotFoundError:
		return None
	else:
		return user_name

def get_new_username():
	"""提示用户输入新的用户名"""
	user_name = input("What's your name?")
	file_name = 'user_name.json'
	with open(file_name,'w') as target:
		json.dump(user_name,target)
	return user_name

def greet_user():
	"""问候用户，并指出其名字"""
	user_name = get_sorted_username()
	if user_name:
		current = input("Hello, "+user_name+"."+"That's your name?(y/n)")
		if current == 'y':
			print("Welcome back, "+user_name+"!")
		else:
			user_name = get_new_username()
			print("We'll remember you when you back, "+user_name+"!")
	else:
		user_name = get_new_username()
		print("We'll remember you when you back, "+user_name+"!")

greet_user()