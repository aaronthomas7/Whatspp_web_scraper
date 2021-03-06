from selenium import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time 
import csv

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import pandas as pd
from gspread_dataframe import set_with_dataframe


from simon.accounts.pages import LoginPage
from simon.chat.pages import ChatPage
from simon.chats.pages import PanePage
from simon.header.pages import HeaderPage

gc = gspread.authorize(credentials)

wks = gc.open('universal adventures sheet').sheet1

wks.clear()


'''
#name of csv file
filename = 'output_whatsapp_web.csv'

#writing to csv file
f = open(filename, 'w')

# create the csv writer
writer = csv.writer(f)
'''

#creating a text file
filename = 'output_whatsapp_web.txt'
f = open(filename,'w+')



# Creating the driver (browser)

driver = webdriver.Firefox()
driver.maximize_window()
wait = WebDriverWait(driver, 600)
print("Window opened and maximized")

#driver.get("https://web.whatsapp.com/")
#wait = WebDriverWait(driver, 600)
login_page = LoginPage(driver)
login_page.load()
time.sleep(7)
print("Whatsapp opened")

#For getting messages from a known chat room to perform action
'''user_name = "Karthik Snist"
user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
user.click()
message = driver.find_elements_by_xpath("//span[@class='i0jNr selectable-text copyable-text']")
for i in message:
	print(i.text)'''

print("Opening the unread chats")

#When you don't know from whom you gonna receive the message
unread_chats = driver.find_elements_by_xpath("//span[@class='_23LrM']")
print(unread_chats)
print("Unread chats are gonna open")
wks.update_cell(1,1,'Names')
wks.update_cell(1,2,'Time')
wks.update_cell(1,3,'Chats')

userid = driver.find_elements_by_xpath("//span[@dir='auto'][@class='_ccCW FqYAR i0jNr']")
a = 2
b = 1
for j in userid:
	try:
		print(j.text)
		wks.update_cell(a,b,j.text)
		a = a+1
	except:
		pass

time = driver.find_elements_by_xpath("//div[@class='_1i_wG']")
a = 2 
b = 2
for k in time:
	try:
		print(k.text)
		wks.update_cell(a,b,k.text)
		a=a+1
	except:
		pass

for chat in unread_chats:
	'''userid = driver.find_elements_by_xpath("//span[@dir='auto'][@class='_ccCW FqYAR i0jNr']")
	a = 2
	b = 1
	for j in userid:
		print(j.text)
		wks.update_cell(a,b,j.text)
		a = a+1'''
	'''time = driver.find_elements_by_xpath("//span[@class='_1i_wG']")
	a = 2 
	b = 2
	for k in time:
		print(k.text)
		wks.update_cell(a,b,k.text)
		a=a+1'''
	#last_message_time = driver.find_elements_by_xpath("//span[@class='_1i_wG']")
	#print(last_message_time.text)
	#print("Reading")
	chat.click()
	a = 2 
	b = 3
	message = driver.find_elements_by_xpath("//span[@class='i0jNr selectable-text copyable-text']")
	for i in message:
		try:
			print(i.text)
			wks.update_cell(a,b,i.text)
			a = a+1
		except:
			pass

f.close()
'''
f = open('output_whatsapp_web.txt','r')

data = f.read()
words = data.split()
result = {}
for word in words:
	if word not in result:
		result[word]=0
	result[word]+=1
print(result)'''
