from user_User import User

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