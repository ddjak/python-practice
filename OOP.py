class Dog:
	#pass only to leave blank and not cause error
	#Class attribute - same for all instances (all Dogs)
	species = 'mammal'
	#Constructor must have self and one argument
	#Instance attributes: what is made for each object
	def __init__(self, name, age):
		self.name = name
		self.age = age
	#this defines a dog, does not create it

philo = Dog('Philo', 2)
fido = Dog('Fido', 5)
feefa = Dog('Feefa', 3)

def get_biggest_number(*age):
	return max(age)

print(get_biggest_number(philo.age, fido.age, feefa.age))