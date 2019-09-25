'''
#4-1
hobbies = ['basketball','running','football']
for hobby in hobbies:
	print("我喜欢"+hobby+"!")
print("我非常喜欢"+hobbies[0]+"!")
'''
'''
#4-2
anmials = ['cat','dog','pig']
for anmial in anmials:
	print(anmial + "是宠物！")
print("这些都可以是宠物！")
'''
'''
#4-3
for number in range(1,21):
	print(number)
'''
'''
#4-4
numbers = list(range(1,1000001))
for number in numbers:
	print(number)
'''
'''
#4-5
numbers = list(range(1,1000001))
print( min(numbers))
print(max(numbers))
print(sum(numbers))
'''
'''
#4-6
numbers = list(range(1,21,2))
for number in numbers:
	print(number)
'''
'''
#4-7
numbers = list(range(3,31,3))
for number in numbers:
	print(number
'''
# 4-8
'''
numbers = [number**3 for number in range(1,11)]
for number in numbers:
	print(number)
'''
# 4-9
'''
numbers = [number**3 for number in range(1,11)]
print(numbers)
'''
# 4-10
'''
numbers = [1,2,3,4,5,6,7,8,9]
print("前三个元素为："+str(numbers[0:3]))
print("中间三个元素为："+str(numbers[3:6]))
print("末尾三个元素为："+str(numbers[-3:]))
'''
'''
#4-11
my_numbers = [1,2,3,4]
friend_numbers = my_numbers[:]
my_numbers.append(5)
friend_numbers.append(6)
print("我的数字有：")
for number in my_numbers:
	print(number)

print("朋友的数字有：")
for number in friend_numbers:
	print(number)
'''
# 4-12
'''
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] 
print("My favorite foods are:") 
for food in my_foods:
	print(food)
print("\nMy friend's favorite foods are:") 
for food in friend_foods:
	print(food)
'''
# 4-13
foods = ('拍黄瓜','小米粥','红烧狮子头','烤鸭','烧鸡')
for food in foods:
	print(food)
print("\n更改后：")
foods = ('炒黄瓜','大米粥','红烧狮子头','烤鸭','烧鸡')
for food in foods:
	print(food)