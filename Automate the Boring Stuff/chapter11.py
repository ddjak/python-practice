#Chapter 11

#WEB SCRAPING

###MapIt
import webbrowser, sys, pyperclip
'''
if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)
'''

###Ideas for similar programs
#	Open all links on a page in separate browser tabs
#	Open the browser to the URL for your local weather
#	Open several social network sites that you regularly check

###Downloading files from websites with REQUEST

import requests
'''
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))
print('------------------------------------------')
#print(res.status_code == requests.codes.ok)
res.raise_for_status()
print(len(res.text))

print(res.text[:250])
'''
### Using BeautifulSoup
import bs4

### Using Selenium
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.set_headless()
assert opts.headless
browser = Firefox(options=opts)
browser.get('https://duckduckgo.com')