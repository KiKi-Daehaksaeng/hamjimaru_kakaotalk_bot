#-*- coding: utf-8 -*-
#!/usr/bin/env python3
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser
import pandas as pd
import datetime
from pandas import Series, DataFrame
import time
import schedule

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no--sandbox')
chrome_options.add_argument('--single-process')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-setuid-sandbox')
chrome_options.add_argument('--remote-debugging-port=9222')

def remove_residue(string):
	removed = ""
	for i in range(len(string)):
		if string[i] == '\n':
			if string[i + 1] == '\n':
				break
		removed += string[i]
	return removed

print("first command")

# chromedriver 경로설정
chromedriver = Service('./chromedriver')
print("first command")

driver = webdriver.Chrome(service=chromedriver, options=chrome_options)

print("ss")
def job():
	print("first command")

	driver.implicitly_wait(1)
	driver.get('https://www.kw.ac.kr/ko/life/facility11.jsp')  # 스크래핑할 url 입력
	driver.implicitly_wait(1)

	print("first command")

	table = driver.find_element(By.XPATH,"//*[@id=\"item_body\"]/div[3]/div/div[1]/article/div[3]/div/section/div/table")
	thead = table.find_elements(By.TAG_NAME,"thead")
	tbody = table.find_elements(By.TAG_NAME,"tbody")


	print("first command")

	for tr in thead:
		th= tr.find_elements(By.TAG_NAME,"th")
		mon=th[1].text
		tue=th[2].text
		wed=th[3].text
		thu=th[4].text
		fri=th[5].text

		#print("first command")
		#print('월:{0}, 화:{1}, 수:{2}, 목:{3}, 금:{4}'.format(mon,tue,wed,thu,fri))
		diet1 =[mon, tue, wed, thu, fri]
		m1={mon,tue,wed,thu,fri}    
	print("first command")

	for tr in tbody:
		td= tr.find_elements(By.TAG_NAME,"td")
		mon=td[1].text
		tue=td[2].text
		wed=td[3].text
		thu=td[4].text
		fri=td[5].text


		#print("second command")
		#print('월:{0}, 화:{1}, 수:{2}, 목:{3}, 금:{4}'.format(mon,tue,wed,thu,fri))
		diet2 =[mon, tue, wed, thu, fri]

	data= [diet1,diet2]
	toSave = pd.DataFrame(data)
	toSave.to_csv("./table.csv", index=False, header=False, encoding="utf-8")

	now =datetime.datetime.now()
	now =str(now)
	with open("./log.txt",'a') as f:
		f.write("["+now+"] "+"update the diet!\n")
		f.close()

job()
driver.close()