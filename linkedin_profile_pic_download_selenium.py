# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 22:32:39 2021

@author: amaity
"""

from selenium import webdriver
import json
import time, random
import pyautogui
import pandas as pd


#username = input('Please give your linkedin Account email-id\n: ')
#password = input('Please give your linkedin Account password\n: ')

with open('config.json','r') as f:
    j = json.load(f)
j = j['credential']
username = j['u']
password = j['p']

df = pd.read_csv('data/linkedin_data.csv')
links = df['profile_link'].drop_duplicates().values.tolist()

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

def automate_save_image(link):
    profile_id = link.split('/')[-2]
    link = link+'detail/photo/'
    browser.get(link)
    action = webdriver.ActionChains(browser)
    elm1 = browser.find_element_by_xpath("//img")
    action.context_click(elm1).perform()
    time.sleep(2)
    pyautogui.typewrite(['down','down','enter'])
    time.sleep(3)
    pyautogui.write(profile_id)
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(2)

for l in links:
    automate_save_image(l)
    time.sleep(random.randint(4,10))
browser.close()