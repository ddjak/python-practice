###Chapter 3

###functions

def hello():
	print('Hey, please type in your name:')

def greetings(name):
	print('Hello, ' + name)

#hello()
#name = input()

#greetings(name)

###Closure
def adder(number):
	def sum(otherNumber):
		return number + otherNumber
	return sum

addTwo = adder(2)
#can also do adder(2)(3) to get similar result. result = 5
#print(addTwo(3))

def multiplier(number):
	def mult(otherNumber):
		return number*otherNumber
	return mult

multiplyThree = multiplier(3)
#print(multiplyThree(4))

# your code goes here
def multiplier_of(number):
    def multiply(other):
        return number*other
    return multiply

multiplywith5 = multiplier_of(5)
multiplywith5(9)