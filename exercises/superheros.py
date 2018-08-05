# Write your solutions for 1.5 here!
class Superheros:
	def __init__(self, name, superpower, strength):
		self.name= name
		self.superpower= superpower
		self.strength= strength
	def save_civillian(self,work):
		strength=strength-work
		print("Superhero is not strong enough! :(")

super=Superheros("Spiderman", "Cobwebs", 10)
print(super.name)
print(super.strength)


