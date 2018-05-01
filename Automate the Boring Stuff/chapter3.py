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

print('Hello', 'hey', 'wow', end=' ')
print('World')

def spam(divideBy):
    try:
        return 42 / divideBy
    #except calls out the specific error you're having
    #and allows you to make it an exception
    except ZeroDivisionError:
        print('Error: Invalid argument.')

'''print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))'''

### Practice Projects

### The Collatz Sequence

def collatz(number):
	while(number != 1):
		if(number%2 == 0):
			print(number//2)
			return number//2
		else:
			print(3*number+1)
			return 3*number+1

number = int(input())

collatz(number)