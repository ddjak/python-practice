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
print(mo.groups())'''
areaCode, mainNumber = mo.groups()
#print(areaCode)

phoneNumRegexParens = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegexParens.search('My phone number is (415) 555-4242.')
mo.group(1)

