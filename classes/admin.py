from users import Users
from privledge import privledge
class Admin(Users, privledge):
	def __init__(self, first_name, last_name, age, location, sex):
		super().__init__(first_name, last_name, age, location, sex)
		self.priv = privledge()