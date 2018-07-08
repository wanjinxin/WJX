class User():
	def __init__(self,first_name,last_name,username,email,location):
		self.first_name=first_name
		self.last_name=last_name
		self.username=username
		self.email=email
		self.location=location
		self.login_attempts=0
		
	def describe_user(self):
		print("\n" + self.first_name + " " + self.last_name)
		print("  Username: " + self.username)
		print("  Email: " + self.email)
		print("  Location: " + self.location)
		
	def greet_user(self):
		print("\nWelcome back, " + self.username + "!")
		
	def increment_login_sttempts(self,increase):
		self.login_attempts+=increase
		
	def reset_login_attempts(self):
		self.login_attempts=0
		
		
users=User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
users.describe_user()
users.greet_user()

users.increment_login_sttempts(1)
print(str(users.login_attempts))

users.reset_login_attempts()
print(str(users.login_attempts))
