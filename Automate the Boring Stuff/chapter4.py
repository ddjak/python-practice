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

spam = ['cat', 'dog', 'bat']
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

#references