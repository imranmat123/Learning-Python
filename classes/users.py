import privledge as p
class Users:
	def __init__(self, first_name, last_name, age, location, sex):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location
		self.sex = sex
		self.login_attempts = 0
	def describe_user(self):
		user = (f'information about the user: '
				f'\n\t{self.first_name}'
				f'\n\t{self.last_name}'
				f'\n\t{self.location}'
				f'\n\t{self.age}'
				f'\n\t{self.sex}')
		return user

	def greet_user(self):
		hi = f'hi {self.first_name}, its nice to meet you!'
		return hi

	def incorment_login_attemps(self):
		self.login_attempts = self.login_attempts + 1

	def	reset_login_attempts(self):
		self.login_attempts = 0

	def print_login_attempts(self):
		return print(f'{self.login_attempts}')

class Admin(Users):
	def __init__(self, first_name, last_name, age, location, sex):
		super().__init__(first_name, last_name, age, location, sex)
		self.privledge = p.privledge()

