#8-1
'''
def display_message():
	print("这是一个函数！")

display_message()
'''
#8-2
'''
def favorite_book(title):
	print("我最喜欢的书是《"+title.title()+"》。")

favorite_book('三国演义')
'''
#8-3
'''
def make_shirt(shirt_size,shirt_text):
	print("T恤的尺码为"+shirt_size+"，上面印有"+shirt_text+"字样！")

make_shirt('m','NO.1')#位置实参
make_shirt(shirt_text = 'NO.1',shirt_size = 'xl')#关键字实参
'''
#8-4
'''
def make_shirt(shirt_size,shirt_text = 'I love Python'):
	print("T恤的尺码为"+shirt_size+"，上面印有"+shirt_text+"字样！")

make_shirt('L')
make_shirt('M')
make_shirt('XL','NO')
'''
#8-5
'''
def describe_city(city_name,city_country = 'china'):
	print(city_name.title()+" in "+city_country.title()+"!")

describe_city('bei jing')
describe_city('tian jin')
describe_city('hua sheng dun','america')
'''
#8-6
'''
def city_country(city_name,city_country):
	print('"'+city_name.title()+","+city_country.title()+'"')

city_country('bei jing','china')
city_country('dong jing','japan)
city_country('hua sheng dun','america')
'''
#8-7
'''
def make_album(singer_name,album_name):
	album_list = {
		'singer_name':singer_name.title(),
		'album_name':album_name.title(),
	}
	return album_list

album = make_album("zhou jie lun",'ting mama de hua')
print(album)

def make_album(singer_name,album_name,album_count):
	album_list = {
		'singer_name':singer_name.title(),
		'album_name':album_name.title(),
	}
	if album_count:
		album_list['album_count'] = album_count
	return album_list

album = make_album("zhou jie lun",'ting mama de hua',10)
print(album)
'''
#8-8
'''
def make_album(singer_name,album_name,album_count=0):
	album_list = {
		'singer_name':singer_name.title(),
		'album_name':album_name.title(),
	}
	if album_count:
		album_list['album_count'] = album_count
	return album_list

while True:
	print("输入歌手名字和专辑")
	print("\t输入q退出")
	singer_name = input("singer name:")
	if singer_name == 'q':
		break
	album_name = input("album name:")
	if album_name == 'q':
		break
	album_count = input("album count:")
	if album_count == 'q':
		break
	album = make_album(singer_name,album_name,album_count)
	print(album)
'''
#8-9
'''
def show_magicians(name_list):
	for name in name_list:
		print(name.title())

name_list = ['zahng san','li si','wangwu']
show_magicians(name_list)
'''
#8-10
'''
def show_magicians(name_list):
	for name in name_list:
		print(name.title())

def make_grate(name_list):
	grate_magicians = []
	while name_list:
		current_name = name_list.pop()
		current_name = "the Grate "+current_name.title()
		grate_magicians.append(current_name)
	
	for magician in grate_magicians:
		name_list.append(magician)

name_list = ['zahng san','li si','wangwu']
show_magicians(name_list)
make_grate(name_list)
show_magicians(name_list)
'''
#8-11
'''
def show_magicians(name_list):
	for name in name_list:
		print(name.title())

def make_grate(name_list):
	grate_magicians = []
	while name_list:
		current_name = name_list.pop()
		current_name = "the Grate "+current_name.title()
		grate_magicians.append(current_name)
	for magician in grate_magicians:
		name_list.append(magician)
	return name_list

name_list = ['zahng san','li si','wangwu']
show_magicians(name_list)

print("grate_magicians:")
grate_magician = make_grate(name_list[:])
show_magicians(grate_magician)

print("name_list:")
show_magicians(name_list)
'''
#8-12
'''
def sandwich_toopings(*toopings):
	for tooping in toopings:
		print("三明治的配料有："+tooping.title())

sandwich_toopings('hot dog','zhi shi')
sandwich_toopings('hot dog')
sandwich_toopings('hot dog','zhi shi','nai you')
'''
#8-13
'''
def build_profile(first, last, **user_info):
	"""创建一个字典，其中包含我们知道的有关用户的一切"""
	profile = {}
	profile['first_name'] = first 
	profile['last_name'] = last 
	for key, value in user_info.items(): 
		profile[key] = value 
	return profile 

user_profile = build_profile('zhang','san', location='bei jing', field='student') 

print(user_profile)
'''
#8-14
'''
def make_car(car_maker,car_num,**car_info):
	profile = {}
	profile['car_maker'] = car_maker
	profile['car_num'] = car_num
	for key,value in car_info.items():
		profile[key] = value
	return(profile)

car = make_car('subaru','outback',color = 'blue',two_package = True)
print(car)
'''
#8-15
'''
import printing_functions as pf

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

pf.print_models(unprinted_designs,completed_models)
pf.show_completed_models(completed_models)
'''
#8-16
#01
import my_print_func

my_print_func.print_func('zahng san')

#02
from my_print_func import print_func

print_func('zhang san')

#03
from my_print_func import print_func as pf
pf('zahng san')

#04
import my_print_func as mf
mf.print_func('zahng san')

#05
from my_print_func import *
print_func('zahng san')