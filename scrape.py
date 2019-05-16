#!/usr/bin/env python3
import time
import os
import sys
import re
from selenium import webdriver
from bs4 import BeautifulSoup
# from scrapy.selector import Selector


HOME = os.environ.get('HOME')
MARKUP_TIMEOUT = 20  # seconds
OUTPUT_FILE = './numbers.csv'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'user-data-dir={HOME}/Library/Application Support/Google/Chrome/Default')

browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('https://web.whatsapp.com/')

print('Waiting for WhatsApp source to render')

for i in range(MARKUP_TIMEOUT):
    soup = BeautifulSoup(browser.page_source, features='html.parser')
    if soup.select('#pane-side'):
        break
    time.sleep(1)
else:
    print(f'Did not receive correct whatsapp source within {MARKUP_TIMEOUT} second limit')
    browser.quit()
    sys.exit()


contacts = {}
old_length = -1

while len(contacts) != old_length:
    items = soup.select('#pane-side > div > div > div > div > div > div > div._3j7s9 > div._2FBdJ > div._25Ooe > span > span')
    print(items)
    old_length = len(contacts)
    contacts.update({ item.string: None for item in items })
    # Scroll the contact list by the container height
    browser.execute_script(
        "document.querySelector('#pane-side').scrollBy(0, document.querySelector('#pane-side').getBoundingClientRect().height)"
    )
    time.sleep(.5)
    soup = BeautifulSoup(browser.page_source, features='html.parser')

numbers = [item for item in contacts.keys() if re.search('\d', item)]

with open(OUTPUT_FILE, 'w') as fd:
    print(*numbers, file=fd, sep='\n')

print(f'Saved {len(numbers)} numbers to {OUTPUT_FILE}')

browser.quit()