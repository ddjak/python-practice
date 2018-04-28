###CHAPTER 2


###while loops and code blocks
'''
while True:
	print("Who are you?")
	name = input()
	if name != "Joe":
		continue
	print("Hey, Joe. What's your password?")
	password = input()
	if password == "swordfish":
		break
print("Acess granted")
'''
###for loops

#for i in range(5, -1, -2):
	#print(i)

###import statements, sys.exit(), pyperclip module
'''
import random, sys, os, math
for i in range(5):
	print(random.randint(1,10))
	'''
###or
'''
from random import randint
for i in range(5):
	print(randint(1,10))
	'''
import sys
while True:
	print('Type exit to exit')
	response = input()
	if response == 'exit':
		sys.exit()
	print('You typed ' + response + '.')