'''
#3-1
names = ['zhang san','li si','wang wu']
print(names[0])
print(names[1])
print(names[2])
'''
'''
#3-2
names = ['zhang san','li si','wang wu']
message = " how do you do?"
print(names[0] + message)
print(names[1] + message)
print(names[2] + message)
'''
'''
#3-3
vehicles = ['motorcycle','bus','car','plane']
message = "I want to by "
print(message + vehicles[0] + ' '+ '!')
print(message + vehicles[1] + ' ' + '!')
print(message + vehicles[2] + ' ' '!')
print(message + vehicles[3] + ' ' + '!')
'''
'''
#3-4
dinner_people = ['zhang san','li si','wang wu','king']
print("邀请名单：")
print("邀请"+dinner_people[0]+"!")
print("邀请"+dinner_people[1]+"!")
print("邀请"+dinner_people[2]+"!")
print("邀请"+dinner_people[3]+"!")
'''
'''
#3-5
dinner_people = ['zhang san','li si','wang wu','king']
print("邀请名单：")
print("邀请"+dinner_people[0]+"!")
print("邀请"+dinner_people[1]+"!")
print("邀请"+dinner_people[2]+"!")
print("邀请"+dinner_people[3]+"!")
print("很遗憾！"+dinner_people[2]+"无法赴约！")
del dinner_people[2]
dinner_people.insert(2,'wang lao wu')
print("邀请"+dinner_people[0]+"!")
print("邀请"+dinner_people[1]+"!")
print("邀请"+dinner_people[2]+"!")
print("邀请"+dinner_people[3]+"!")
'''
'''
#3-6
dinner_people = ['zhang san','li si','wang wu','king']
print("邀请名单：")
print("邀请"+dinner_people[0]+"!")
print("邀请"+dinner_people[1]+"!")
print("邀请"+dinner_people[2]+"!")
print("邀请"+dinner_people[3]+"!")
print("很遗憾！"+dinner_people[2]+"无法赴约！")
del dinner_people[2]
dinner_people.insert(2,'wang lao wu')
print("邀请"+dinner_people[0]+"!")
print("邀请"+dinner_people[1]+"!")
print("邀请"+dinner_people[2]+"!")
print("邀请"+dinner_people[3]+"!")
print("我找到了一张更大的餐桌，我将邀请另外三人。")
dinner_people_plus = ['朱老三','王老二','小翠花']
dinner_people.insert(0,dinner_people_plus[0])
dinner_people.insert(int(len(dinner_people)/2),dinner_people_plus[1])
dinner_people.append(dinner_people_plus[2])
print("邀请"+dinner_people[0]+"!")
print("邀请"+dinner_people[1]+"!")
print("邀请"+dinner_people[2]+"!")
print("邀请"+dinner_people[3]+"!")
print("邀请"+dinner_people[4]+"!")
print("邀请"+dinner_people[5]+"!")
print("邀请"+dinner_people[6]+"!")
'''
'''
#3-7
dinner_people = ['zhang san','li si','wang wu','king']
print("邀请名单：")
print("邀请"+dinner_people[0]+"!")
print("邀请"+dinner_people[1]+"!")
print("邀请"+dinner_people[2]+"!")
print("邀请"+dinner_people[3]+"!")
print("很遗憾！"+dinner_people[2]+"无法赴约！")
del dinner_people[2]
dinner_people.insert(2,'wang lao wu')
print("邀请"+dinner_people[0]+"!")
print("邀请"+dinner_people[1]+"!")
print("邀请"+dinner_people[2]+"!")
print("邀请"+dinner_people[3]+"!")
print("我找到了一张更大的餐桌，我将邀请另外三人。")
dinner_people_plus = ['朱老三','王老二','小翠花']
dinner_people.insert(0,dinner_people_plus[0])
dinner_people.insert(int(len(dinner_people)/2),dinner_people_plus[1])
dinner_people.append(dinner_people_plus[2])
print("邀请"+dinner_people[0]+"!")
print("邀请"+dinner_people[1]+"!")
print("邀请"+dinner_people[2]+"!")
print("邀请"+dinner_people[3]+"!")
print("邀请"+dinner_people[4]+"!")
print("邀请"+dinner_people[5]+"!")
print("邀请"+dinner_people[6]+"!")
print("非常抱歉！由于餐桌不够，只能邀请两人")
delete_people1 = dinner_people.pop()
print("非常抱歉"+delete_people1+"取消了晚餐！")
delete_people2 = dinner_people.pop()
print("非常抱歉"+delete_people2+"取消了晚餐！")
delete_people3 = dinner_people.pop()
print("非常抱歉"+delete_people3+"取消了晚餐！")
delete_people4 = dinner_people.pop()
print("非常抱歉"+delete_people4+"取消了晚餐！")
delete_people5 = dinner_people.pop()
print("非常抱歉"+delete_people5+"取消了晚餐！")
print(dinner_people[0]+"您仍在邀请队列！")
print(dinner_people[1]+"您仍在邀请队列！")
del dinner_people[0]
del dinner_people[0]
print(dinner_people)
'''
'''
#3-8
places = ['bei jing','shang hai','a li shan','cao yuan','he nan']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse = True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse = True)
print(places)
'''
'''
#3-9
dinner_people = ['zhang san','li si','wang wu','king']
print("邀请名单：")
print("邀请"+dinner_people[0]+"!")
print("邀请"+dinner_people[1]+"!")
print("邀请"+dinner_people[2]+"!")
print("邀请"+dinner_people[3]+"!")
print("很遗憾！"+dinner_people[2]+"无法赴约！")
del dinner_people[2]
dinner_people.insert(2,'wang lao wu')
print("邀请"+dinner_people[0]+"!")
print("邀请"+dinner_people[1]+"!")
print("邀请"+dinner_people[2]+"!")
print("邀请"+dinner_people[3]+"!")
print("邀请了"+ str(len(dinner_people)) + "位嘉宾进行晚宴！")
'''
#3-10
#pass
#3-11
#pass
