#CHAPTER 7
# PATTERN MATCHING WITH REGULAR EXPRESSIONS

import re

#\d{3}-\d{3}-\d{4} is phone number format in regex

phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 415-555-4242.')
#print('Phone number found: ' + mo.group())

#regexpal.com
phoneNumRegexGrouping = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegexGrouping.search('My number is 415-555-4242.')
'''print(mo.group(1))
print(mo.group(2))
print(mo.group() + ' ' + mo.group(0))
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode, mainNumber)'''

phoneNumRegexParens = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegexParens.search('My phone number is (415) 555-4242.')
mo.group(1)



### PROJECT

#Extract emails and phone numbers off a page.

#Get text from clipboard, find all numbers and emails, paste them
#create 2 regexes: one for email, one for phone
import pyperclip

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                     # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+
	@
	[a-zA-Z0-9.-]+
	(\.[a-zA-Z]{2,4})
	)''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []

for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	#print(groups)
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

#Other project ideas:
### Find website URLs that begin with http:// or https://
### Clean up dates in different date formats (3/14/2015, 03-14-15, 2015/3/14) by replacing
#	them with dates in a single, standard format
### Remove sensitive information such as Social Security or credit card numbers
### Find common typos such as multiple spaces between words, accidentally repeated words, 
#	multiple exclamation marks at the end of a sentence. Those are annoying!!!

 