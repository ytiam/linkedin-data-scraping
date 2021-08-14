# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests, time, random
from bs4 import BeautifulSoup
from selenium import webdriver
import json


#username = input('Please give your linkedin Account email-id\n: ')
#password = input('Please give your linkedin Account password\n: ')

with open('config.json','r') as f:
    j = json.load(f)
j = j['credential']
username = j['u']
password = j['p']

### Download the chromedriver from https://chromedriver.chromium.org/downloads
### depending upon your chrome version and OS and extract the chromedriver 
### from the zip file. Once you have the file, just copy the path of the
### driver, say 'path_to_chromedriver'

browser = webdriver.Chrome('driver/chromedriver') # give the path_to_chromedriver here
browser.get('https://www.linkedin.com/uas/login')

elementID = browser.find_element_by_id('username')
elementID.send_keys(username)
elementID = browser.find_element_by_id('password')
elementID.send_keys(password)
elementID.submit()

link = input('Please pass the user linkedin profile link: ') #'https://www.linkedin.com/in/midhun-em89/detail/photo/'
link = link+'detail/photo/'
browser.get(link)
src = browser.page_source
soup = BeautifulSoup(src,'lxml')

ss = soup.find('div',{'class':'pv-member-photo-modal__content pv-member-photo-modal__content--padded'})

if ss == None:
    ss = soup.find('div',{'class':'pv-non-self-member-photo-modal__image-wrapper'})
s1 = ss.find_all('img')
s2 = s1[0]
print('\n profile picture image link is: ',s2['src'])
browser.close()