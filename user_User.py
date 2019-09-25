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
