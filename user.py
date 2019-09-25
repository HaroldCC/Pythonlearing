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