#11-1
'''
#导入测试模块
import unittest

#导入测试的函数
from city_functions import city_describe

class CitiesTestCase(unittest.TestCase):
	"""测试city_functions.py"""
	
	def test_city_country(self):
		"""测试能否处理'City,Country'这样的格式"""
		full_city_name = city_describe('bei jing','china')
		self.assertEqual(full_city_name,'Bei Jing,China')

unittest.main()
'''
#11-2
'''
#导入测试模块
import unittest

#导入测试的函数
from city_functions import city_describe

class CitiesTestCase(unittest.TestCase):
	"""测试city_functions.py"""
	
	def test_city_country(self):
		"""测试能否处理'City,Country'这样的格式"""
		full_city_name = city_describe('bei jing','china')
		self.assertEqual(full_city_name,'Bei Jing,China')

	def test_city_country_population(self):
		"""测试能否处理'City,Country - Population xxx'这样的格式"""
		full_city_name = city_describe('bei jing','china',10000)
		self.assertEqual(full_city_name,'Bei Jing,China - Population 10000')

unittest.main()
'''
#11-3
class Employee():
	def __init__(self,first_name,last_name,salary):
		self.first_name = first_name
		self.last_name = last_name
		self.salary = salary

	def give_raise(self,salary_increase=5000):
		self.salary += salary_increase

import unittest
#导入测试模块


class TestEmployee(unittest.TestCase):
	"""测试Employee类"""
	def setUp(self):
		"""创建setUp()来进行测试"""
		self.zhangsan = Employee('zhang','san',1000)

	def test_give_default_raise(self):
		"""测试默认增加年薪"""
		self.zhangsan.give_raise()
		self.assertEqual(self.zhangsan.salary,6000)

	def test_give_changed_raise(self):
		"""测试改变后的年薪增加数"""
		self.zhangsan.give_raise(1000)
		self.assertEqual(self.zhangsan.salary,2000)

unittest.main()