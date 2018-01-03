# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 17:04:34 2017

@author: v-beshi
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from bs4 import BeautifulSoup
import time
import re

def qunar(FD,TD,FC,TC):
    global cheapest
    driver=webdriver.Firefox()
    driver.get("http://www.qunar.com")
    time.sleep(3)
    roundt=driver.find_element_by_id("js_searchtype_roundtrip")
    roundt.click()
    time.sleep(3)
    fromcity=driver.find_element_by_name("fromCity")
    fromcity.send_keys(FC)
    time.sleep(3)
    tocity=driver.find_element_by_name("toCity")
    tocity.send_keys(TC)
    time.sleep(3)
    fromDate=driver.find_element_by_name("fromDate")
    fromDate.clear()
    fromDate.send_keys(FD)
    toDate=driver.find_element_by_name("toDate")
    toDate.clear()
    toDate.send_keys(TD)
    submit=driver.find_element_by_class_name('button-search')
    time.sleep(5)
    submit.click()
    time.sleep(30)
    html=driver.page_source
    soup=BeautifulSoup(html)
    cheapest=soup.findAll(class_='b-airfly')[0]
    b=cheapest.attrs['data-reactid']
    flightname=b[len(b)-15:]
    num=cheapest.find(class_='rel').findAll(style='width: 18px;')
    cal=[]
    for i in num:
        cal.append(i.get_text())
    sin=cheapest.find(class_='rel').find(style='width: 18px;left:-18px')
    ten=cheapest.find(class_='rel').find(style='width: 18px;left:-36px')
    hun=cheapest.find(class_='rel').find(style='width: 18px;left:-54px')
    tho=cheapest.find(class_='rel').find(style='width: 18px;left:-72px')
    if len(cal)==3:
        if sin:
            sinact=sin.get_text()
        else:
            sinact=cal[0]
        if ten:
            tenact=ten.get_text()
        else:
            tenact=cal[1]
        if hun:
            hunact=hun.get_text()
        else:
            hunact=cal[2]
        print('flight name={f}'.format(f=flightname))
        print('price={h}{t}{s}'.format(h=hunact,t=tenact,s=sinact))
    elif len(cal)==4:
        if sin:
            sinact=sin.get_text()
        else:
            sinact=cal[0]
        if ten:
            tenact=ten.get_text()
        else:
            tenact=cal[1]
        if hun:
            hunact=hun.get_text()
        else:
            hunact=cal[2]
        if tho:
            thoact=tho.get_text()
        else:
            thoact=cal[3]
        print('flight name={f}'.format(f=flightname))        
        print('price=￥{th}{h}{t}{s}'.format(h=hunact,t=tenact,s=sinact,th=thoact))
    
    