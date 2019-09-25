#9-1
'''
class Restaurant():
	#__init__这里init两边是2个下划线
	def __init__(self,restaurant_name,restaurant_type):
		self.restaurant_name = restaurant_name.title()
		self.restaurant_type = restaurant_type.title()

	def describe_restaurant(self):
		print(self.restaurant_name+"主营"+self.restaurant_type+"!")

	def open_restaurant(self):
		print(self.restaurant_name+"正在营业！")

restaurant = Restaurant('张三烧烤','烧烤')
print(restaurant.restaurant_name)
print(restaurant.restaurant_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
'''
#9-2
'''
class Restaurant():
	#__init__这里init两边是2个下划线
	def __init__(self,restaurant_name,restaurant_type):
		self.restaurant_name = restaurant_name.title()
		self.restaurant_type = restaurant_type.title()

	def describe_restaurant(self):
		print(self.restaurant_name+"主营"+self.restaurant_type+"!")

	def open_restaurant(self):
		print(self.restaurant_name+"正在营业！")

#01
zhangsan = Restaurant('张三烧烤','烧烤')
zhangsan.describe_restaurant()

#02
lisi = Restaurant('李四水产','海鲜')
lisi.describe_restaurant()

#03
kendeji = Restaurant('肯德基','快餐')
kendeji.describe_restaurant()
'''
#9-3
'''
class User():
	def __init__(self,first_name,last_name,user_age,phone_number):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.user_age = user_age
		self.phone_number = phone_number

	def describe_user(self):
		print("\n"+self.first_name+" "+self.last_name)
		print("Age:"+str(self.user_age))
		print("Phone number:"+self.phone_number)

	def greet_user(self):
		print("Hello "+self.first_name+" "+self.last_name+".")

zhangsan = User('zhang','san',18,'11234')
zhangsan.describe_user()
zhangsan.greet_user()

lisi = User('li','si',20,'1326206')
lisi.describe_user()
lisi.greet_user()
'''
#9-4
'''
class Restaurant():
	#__init__这里init两边是2个下划线
	def __init__(self,restaurant_name,restaurant_type):
		self.restaurant_name = restaurant_name.title()
		self.restaurant_type = restaurant_type.title()
		self.number_served = 0

	def describe_restaurant(self):
		print(self.restaurant_name+"主营"+self.restaurant_type+"!")

	def open_restaurant(self):
		print(self.restaurant_name+"正在营业！")

	#设置就餐人数
	def set_number_served(self,number):
		self.number_served = number

	#就餐人数递增
	def increment_number_served(self,increment_number):
		self.number_served += increment_number

restaurant = Restaurant('肯德基','快餐')
restaurant.describe_restaurant()

#原本服务人数
print("Number served（原）:"+str(restaurant.number_served))

#修改后
restaurant.number_served = 20
print("Number served（改）:"+str(restaurant.number_served))

#设置
restaurant.set_number_served(36)
print("Number served（设）:"+str(restaurant.number_served))

#增涨
restaurant.increment_number_served(10)
print("Number served（增）:"+str(restaurant.number_served))
'''
#9-5
'''
class User():
	def __init__(self,first_name,last_name,user_age,phone_number):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.user_age = user_age
		self.phone_number = phone_number
		self.login_attempts = 0

	def describe_user(self):
		print("\n"+self.first_name+" "+self.last_name)
		print("Age:"+str(self.user_age))
		print("Phone number:"+self.phone_number)

	def greet_user(self):
		print("Hello "+self.first_name+" "+self.last_name+".")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

zhangsan = User('zhang','san',18,'11234')
zhangsan.describe_user()
zhangsan.greet_user()

print(zhangsan.login_attempts)

zhangsan.increment_login_attempts()
zhangsan.increment_login_attempts()
zhangsan.increment_login_attempts()
zhangsan.increment_login_attempts()
zhangsan.increment_login_attempts()
print(zhangsan.login_attempts)

zhangsan.reset_login_attempts()
print(zhangsan.login_attempts)
'''
#9-6
'''
class Restaurant():
	#__init__这里init两边是2个下划线
	def __init__(self,restaurant_name,restaurant_type):
		self.restaurant_name = restaurant_name.title()
		self.restaurant_type = restaurant_type.title()
		self.number_served = 0

	def describe_restaurant(self):
		print(self.restaurant_name+"主营"+self.restaurant_type+"!")

	def open_restaurant(self):
		print(self.restaurant_name+"正在营业！")

class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,restaurant_type = 'icecream'):
		super().__init__(restaurant_name,restaurant_type)
		self.flavors = []

	def show_flavors(self):
		print("冰淇淋口味有：")
		for flavor in self.flavors:
			print(flavor.title())

icehouse = IceCreamStand('ICEHOUSE')
icehouse.flavors = ['chocolate','milk','black cherry']

icehouse.describe_restaurant()
icehouse.show_flavors()
'''
#9-7
'''
class User():
	def __init__(self,first_name,last_name,user_age,phone_number):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.user_age = user_age
		self.phone_number = phone_number

	def describe_user(self):
		print("\n"+self.first_name+" "+self.last_name)
		print("Age:"+str(self.user_age))
		print("Phone number:"+self.phone_number)

	def greet_user(self):
		print("Hello "+self.first_name+" "+self.last_name+".")

class Admin(User):
	def __init__(self,first_name,last_name,user_age,phone_number):
		super().__init__(first_name,last_name,user_age,phone_number)
		self.privileges = []

	def show_privileges(self):
		for privilege in self.privileges:
			print(self.first_name.title()+" "+self.last_name.title()+
				" "+privilege+".")

manage = Admin('xiao','ming',20,'1326206')
manage.describe_user()
manage.greet_user()
manage.privileges = ['can add post','can delete post','can ban user']
manage.show_privileges()
'''
#9-8
'''
class User():
	def __init__(self,first_name,last_name,user_age,phone_number):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.user_age = user_age
		self.phone_number = phone_number

	def describe_user(self):
		print("\n"+self.first_name+" "+self.last_name)
		print("Age:"+str(self.user_age))
		print("Phone number:"+self.phone_number)

	def greet_user(self):
		print("Hello "+self.first_name+" "+self.last_name+".")

class Admin(User):
	def __init__(self,first_name,last_name,user_age,phone_number):
		super().__init__(first_name,last_name,user_age,phone_number)
		self.privileges = Privileges()


class Privileges():
	def __init__(self):
		self.privileges = ['can add post','can delete post','can ban user']

	def show_privileges(self):
		if self.privileges:
			for privilege in self.privileges:
				print(privilege+".")
		else:
			print("用户没有该特权！")

manage = Admin('xiao','ming',20,'1326206')
manage.describe_user()
manage.greet_user()

print("added:")
manage.privileges.show_privileges()
'''
#9-9
'''
class Car():
	def __init__(self,manufacturer,model,year):
		self.manufacturer = manufacturer
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		full_name = str(self.year)+' '+self.manufacturer+' '+self.model
		return full_name.title()

	def read_odometer(self):
		print("This car has "+str(self.odometer_reading)+" miles on it.")

	def update_odometer(self,mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self,miles):
		self.odometer_reading += miles

class Battery():
	def __init__(self,battery_size = 60):
		self.battery_size = battery_size

	def describe_battery(self):
		print("This car has a "+str(self.battery_size)+"-kwh battery.")

	def get_range(self):
		if self.battery_size == 60:
			range = 140
		elif self.battery_size == 85:
			range = 185
		print("This car can go approximately"+str(range)+
			"miles on a full charge.")

	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85
			print("Upgraded the battery to 85 kWh.")
		else:
			print("The battery is already upgraded.")

class ElectricCar(Car):
	def __init__(self,manufacturer,model,year):
		super().__init__(manufacturer,model,year)
		self.battery = Battery()


my_tesla = ElectricCar('tesla','model s',2018)
print(my_tesla.get_descriptive_name())
my_tesla.read_odometer()
my_tesla.battery.describe_battery()

print("\n更新后：")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\n再次更新后：")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
'''
#9-10
'''
from restaurant import Restaurant

zhangsan = Restaurant('zhang san BBQ','BBQ')
zhangsan.describe_restaurant()
zhangsan.open_restaurant()
'''
#9-11
'''
import user

xiaoming = user.Admin('xiao','ming',20,'1326206')
xiaoming.privileges.show_privileges()
'''
#9-12
'''
from privileges_admin import Admin

xiaoming = Admin('xiao','ming',20,'1326206')
xiaoming.privileges.show_privileges()
'''
#9-13
'''
from collections import OrderedDict

codes = OrderedDict()

codes['p'] = 'python'
codes['c'] = 'c++'
codes['j'] = 'java'
codes['r'] = 'ruby'
codes['h'] = 'html'
codes['t'] = 'title'
codes['s'] = 'sort'

for words,languages in codes.items():
	print(words.title()+":"+languages.title())
'''
#9-14
from random import randint

class Die():
	def __init__(self,sides=6):
		self.sides = sides

	def roll_die(self):
		return randint(1,self.sides)

die6 = Die()
results = []
for roll_num in range(10):
	result = die6.roll_die()
	results.append(result)
print(results)

die10 = Die(sides=10)
results = []
for roll_num in range(10):
	result = die10.roll_die()
	results.append(result)
print(results)

die20 = Die(sides=20)
results = []
for roll_num in range(10):
	result = die20.roll_die()
	results.append(result)
print(results)