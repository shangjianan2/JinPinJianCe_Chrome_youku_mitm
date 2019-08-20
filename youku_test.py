#!/usr/bin/env python
#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time
import json
from video_play_youku import *

def t2s(t):
    if(str(t).count(":") == 2):
        h,m,s = t.strip().split(":")
        return int(h) * 3600 + int(m) * 60 + int(s)
    else:
        m,s = t.strip().split(":")
        return int(m) * 60 + int(s)

url = input("url: ")
print("please choose definition: 1 1080p, 2 720p, 3 480p")
qixidu = input("please input the num: ")
video_def = "480p"
if(qixidu == 1):
    print("1080p")
    video_def = "1080p"
elif(qixidu == 2):
    print("720p")
    video_def = "720p"
elif(qixidu == 3):
    print("480p")
    video_def = "480p"
#elif(qixidu == 4):
#    print("320p")
#    video_def = "320p"
else:
    print("error")

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--proxy-server=9.92.212.45:443')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='./chromedriver')

driver.implicitly_wait(30)#设置加载driver加载元素时所等待的最长的时间，
#driver.get("https://www.iqiyi.com/v_19rrdh6354.html")
#driver.get("https://v.youku.com/v_show/id_XMzE0NDQxNTg4.html?spm=a2h0k.11417342.soresults.dposter")
driver.get(url)

print '1' 
driver.refresh()
with open('./youku_cookie.txt', 'r') as f:
    cookies = f.read()
    cookies = json.loads(cookies)

for mem in cookies:
    driver.add_cookie(mem)
driver.refresh()
print '2'

print("successful operation\r\n")

print("waiting for the advertising\r\n")
time.sleep(40)
print("advertising is over\r\n")
test_play = video_play_youku(driver)
#test_play.play('GaoQing')
test_play.play(video_def)

during_second = t2s(driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div[3]/span[3]').get_attribute('textContent'))
print("the total time is %d second\r\n" % (during_second))
print("the video is playing......\r\n")

time.sleep(during_second - 5)
driver.save_screenshot('youku_test.png')

driver.close()
driver.quit()
print("game over")
