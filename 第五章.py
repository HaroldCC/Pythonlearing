'''
#5-1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("Is car == 'audi'? I predict False.")
print(car == 'audi')

num = 1
print("数字为1吗？")
print(num == 1)
'''
#5-2
'''
str1 = 'cheng'
str2 = 'Cheng'
print("两个字符串相等吗？")
print(str  == str2)
print(str1.lower() == str2.lower())
num1 = 1
num2 = 2
print("两个数字相等吗？")
print(num1 == num2)
print("两个数字不等吗？")
print(num1 != num2)
print("num1 大于 num2?")
print(num1 > num2)
print("num1 < num2 ?")
print(num1 < num2)
print("num1 >= num2 ?")
print(num1 >= num2)
print("num1 <= num2")
print(num1 <= num2)
num3 = 3
if num1 < num2 and num2 < num3:
	print("num3最大！")
if num1 > num2 or num2 < num3:
	print("done")
numbers = [1,2,3,4]
print(1 in numbers)
print(5 not in numbers)
'''
#5-3
'''
alien_color = 'green'
if alien_color == 'green':
	print("正确")
if alien_color == 'yellow':
	print("正确")
'''
#5-4
'''
alien_color = 'green'
if alien_color == 'green':
	print("正确")
alien_color = 'red'
if alien_color != 'green':
	print("正确")

alien_color = 'green'
if alien_color == 'green':
	print("正确")
else:
	print("错误")
'''
#5-5
'''
alien_color = 'green'
if alien_color == 'green':
	print("正确")
elif alien_color == 'yellow':
	print("正确")
elif alien_color == 'red':
	print("正确")

alien_color = 'yellow'
if alien_color == 'green':
	print("正确")
elif alien_color == 'yellow':
	print("正确")
elif alien_color == 'red':
	print("正确")

alien_color = 'red'
if alien_color == 'green':
	print("正确")
elif alien_color == 'yellow':
	print("正确")
elif alien_color == 'red':
	print("正确")
'''
#5-6
'''
age = 60
if age < 2:
	print("婴儿")
elif age >= 2 and age < 4:
	print("蹒跚学步")
elif age >= 4 and age < 13:
	print("儿童")
elif age >= 13 and age < 20:
	print("青少年")
elif age >= 20 and age < 65:
	print("成年人")
else:
	print("老年人")
'''
#5-7
'''
favorite_fruits = ['apple','banana','orange']
if 'apple' in favorite_fruits:
	print("苹果")
if 'banana' in favorite_fruits:
	print("香蕉")
if 'orange' in favorite_fruits:
	print("橘子")
if 'watermelon' in favorite_fruits:
	print("西瓜")
if 'tomato' in favorite_fruits:
	print("番茄")
'''
#5-8
'''
users = ['xiao ming','xiao qiang', 'admin','san','wang']
for user in users:
	print("你好"+user+"!")

print("\n")
for user in users:
	if user == 'admin':
		print("Hello "+user+",would you like to see a status report?")
	else:
		print("你好"+user+"!")
'''
#5-9
'''
users = []
if users:
	for user in users:
		print("你好"+user+"!")
else:
	print("列表为空!")
'''
#5-10
'''
current_users = ['xiao ming','xiao qiang', 'admin','san','wang']
new_users = ['qiang','ADMIN','liu','xiao ming','cheng']
for user in new_users:
	if user.lower() in current_users:
		print("用户名"+user+"已存在！请更换用户名！")
	else:
		print("用户名"+user+"可以使用！")
'''
#5-11
'''
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
	if number == 1:
		print(str(number)+"st")
	elif number == 2:
		print(str(number)+"nd")
	elif number == 3:
		print(str(number)+"rd")
	else:
		print(str(number)+"th")
'''
input_name = input("输入您的名字：")


file_name = 'guest.txt'

with open(file_name,w) as file_object:
	file_object.write(input_name)