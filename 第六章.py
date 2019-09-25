# 6-1
'''
friends = {
	'friend_name':'san',
	'last_name':'zahng',
	'age':13,
	'city':'shang hai',
}
print(friends['friend_name'])
print(friends['last_name'])
print(friends['age'])
print(friends['city'])
'''
# 6-2
'''
like_numbers = {
	'zhang':15,
	'li':20,
	'zhao':16,
	'cheng':40,
	'wang':8,
}
print("zhang:"+str(like_numbers['zhang']))
print("li:"+str(like_numbers['li']))
print("zhao:"+str(like_numbers['zhao']))
print("cheng:"+str(like_numbers['cheng']))
print("wang:"+str(like_numbers['cheng']))
print("wang:"+str(like_numbers['wang']))
'''
# 6-3
'''
codes = {
	'p':'python',
	'c':'c++',
	'j':'java',
	'r':'ruby',
	'h':'html',
}
print("'p':"+codes['p'])
print("'c':"+codes['c'])
print("'j':"+codes['j'])
print("'r':"+codes['r'])
print("'h':"+codes['h'])
'''
# 6-4
'''
codes = {
	'p':'python',
	'c':'c++',
	'j':'java',
	'r':'ruby',
	'h':'html',
	't':'title',
	's':'sort',
}
for words,languages in codes.items():
	print(words.title()+":"+languages.title())
'''
# 6-5
'''
river_country = {
	'nile':'egypt',
	'chang jiang':'china',
	'huang he':'china',
}
for river,country in river_country.items():
	print("The "+river.title()+" runs through "+country.title()+"." )
print(' ')
for river in river_country.keys():
	print(river)
print(' ')
for country in river_country.values():
	print(country)
'''
# 6-6
'''
favorite_languages = {
    'jan' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'c++'
}
Investigation_list = ['jan','xiao ming','zhang san','sarah']
for person in Investigation_list:
	if person in favorite_languages.keys():
		print(person.title()+"您已参加调研！")
	else:
		print(person.title()+"欢迎参加调研！")
'''
# 6-7
'''
person1 = {
	'first_name':'san',
	'last_name':'zhang',
	'age':13,
	'city':'shang hai',
	}
person2 = {
	'first_name':'si',
	'last_name':'zhang',
	'age':10,
	'city':'bei jing',
}
person3 = {
	'first_name':'wu',
	'last_name':'wang',
	'age':20,
	'city':'tian jin',
}
people = [person1,person2,person3]
for person in people:
	print("名字"+person['last_name'].title()+' '+person['first_name'].title())
	print("年龄"+str(person['age']))
	print("所在城市"+person['city'].title())
'''
# 6-8
'''
jan = {
	'name':'jan',
	'type':'cat',
	'master':'zhang san',
}
ame = {
	'name':'ame',
	'type':'dog',
	'master':'li si',
}
kor = {
	'name':'kor',
	'type':'pig',
	'master':'wang wu',
}
pets = [jan,ame,kor]
for pet in pets:
	print(pet['master'].title()+" have a "+pet['type']+" named "+pet['name'].title()+".")
'''
# 6-9
'''
favorite_places = {
	'zhang san':['shang hai','bei jing'],
	'li si':['shen zhen'],
	'wang wu':['cheng du','xiang gang','hai nan'],
}
for name, places in favorite_places.items():
	print(name.title()+"最喜欢去的城市有：")
	for place in places:
		print("\t"+place.title())
'''
# 6-10
'''
like_numbers = {
	'zhang':[15,13,10],
	'li':[20,0],
	'zhao':[16,14,1],
	'cheng':[40,159],
	'wang':[8],
}
for name,numbers in like_numbers.items():
	print("\n"+name.title()+"喜欢的数字有：")
	for number in numbers:
		print("\t"+str(number))
'''
# 6-11
'''
cities = {
'bei jing':{
		'country':'china',
		'population':100000000,
		'fact':'The capital of china.',
	},
'hua sheng dun':{
	'country':'america',
	'population':100000,
	'fact':'The capital of america.',
	},
'dong jing':{
	'country':'japan',
	'population':200000,
	'fact':'The capital of japan.'
	},
}
for city,city_info in cities.items():
	print("\n城市名："+city.title())
	country = city_info['country']
	population = city_info['population']
	fact = city_info['fact']
	print("  所属国家:"+country.title())
	print("  人口数量："+str(population))
	print("  相关事实："+fact)
'''
# 6-12
# pass
