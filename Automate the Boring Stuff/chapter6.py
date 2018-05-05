###CHAPTER 6

#Manipulating Strings

#Create a password manager and something to format pieces of text

print('''
	wow 
	multiline text


	Very cool''')
#raw string is good for regex
print(r'That\'s good\nWhat\'s new?')

import pyperclip
pyperclip.copy('Hello')
pyperclip.paste() ###Doesn't work. try installing pyperclip on computer. Appendix B