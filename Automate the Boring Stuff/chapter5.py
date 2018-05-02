###Dictionaries and Structuring Data

#Vernacular between JS and Python. Python = [Lists, Dictionaries] == JS = [Arrays, Objects]

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
'''
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
'''
#keys(), values(), items()

spam = {'color':'red', 'age':42}
for k, v in spam.items():
	print("Key: "+k+", Value: "+str(v))

#Get Method

picnicItems = {'apples':5, 'cups':2}
#get key in object, if not found, return 0.
#print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
###2 cups
#print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')
###0 eggs

#Set Default Method. If something doesn't exist, make it exist.
#If key already exists, setdefault() will not replace value.

#from pprint import pprint as pprint
#from pprint import pprint as pformat

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
	count.setdefault(character, 0)
	count[character] = count[character] + 1
#print(count)

#pprint(count) gives you value for terminal
#pformat(count) gives you a string value instead of displaying it on a screen