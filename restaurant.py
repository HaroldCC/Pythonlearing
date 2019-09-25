class Restaurant():
	def __init__(self,restaurant_name,restaurant_type):
		self.restaurant_name = restaurant_name
		self.restaurant_type = restaurant_type
		self.number_served = 0

	def describe_restaurant(self):
		print(self.restaurant_name+"主营"+self.restaurant_type+"。")

	def open_restaurant(self):
		print("Welcome to "+self.restaurant_name+"!")

	def set_number_served(self,number_served):
		self.number_served = number_served

	def increment_number_served(self,increment_number):
		self.number_served += increment_number