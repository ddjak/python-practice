### Data Structures
'''
for i in [0, 12, 2, 3]:
    print(i)
'''
'''
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)
'''
'howdy' in ['hello', 'hi', 'howdy', 'heyas'] #True

spam = ['cat', 'dog', 'bat', 'hello']
spam.append('moose')
#print(spam)

spam.insert(1, 'chicken')
#print(spam)

spam.remove('hello')

spam.sort() #sorts alphabetically AND numerically (uppercase first)
			#to not make it uppercase first, make it .sort(key=str.lower)
spam.sort(reverse=True) #sorts opposite

#print('Four score and seven ' + \
#      'years ago...')			How to legally break lines to make code more readable

#Tuple is like a list EXCEPT 1) tuples are typed with parentheses instead of square brackets
#2)They are immutable like strings

eggs = ('hello', 42, 0.5)
#print(eggs[0])

#eggs[1] = 99 ### Causes an error. Can't be changed

###You can caste lists in tuples or vice versa, you can caste a string as a list too
#list('hello') ==> ['h', 'e', 'l', 'l', 'o']

###references
#Data structures like arrays, functions, and objects are stored in memory,
#then the variable assigned to the structure contains a reference to the address in memory
#That reference is copied, not the actual structure

#To make a copy of an array with reference AND address, use copy() and deepcopy()

spam = [2, 2, 2, 2, 2]
cheese = spam
cheese[1] = 42
#both variables will print changed value array

import copy
spam = [1, 2, 3, 4, 5]
cheese = copy.copy(spam)
cheese[1] = 42
#only cheese array will have changed value
##If your copy contains lists, use copy.deepcopy() to copy the inner lists as well.

###EXERCISES

arr = ['apples', 'bananas', 'beverage', 'tofu', 'cats', 'tacos']
sentence = ''
for stuff in arr:
	sentence = sentence + stuff
	if stuff != arr[-1]:
		sentence = sentence + ', '
	else:
		sentence = sentence + '.'
print(sentence)


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


#Solution works, but messy. Fix later
'''rows = ''
increment = 0
for row in grid:
	for j in grid: 
		rows = rows + j[increment]
	rows = rows + "\n"
	increment = increment+1
	print(rows)'''