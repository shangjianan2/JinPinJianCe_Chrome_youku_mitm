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

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--proxy-server=9.92.212.45:443')


driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='./chromedriver')

# go to the google home page
#driver.get("https://www.iqiyi.com/v_19rrdh6354.html")
driver.get("https://v.youku.com/v_show/id_XMzE0NDQxNTg4.html?spm=a2h0k.11417342.soresults.dposter")

print '1' 
driver.refresh()
with open('./youku_cookie.txt', 'r') as f:
    cookies = f.read()
    cookies = json.loads(cookies)

for mem in cookies:
    driver.add_cookie(mem)
driver.refresh()
print '2'

driver.save_screenshot('loadedc.png')

print("successful operation\r\n")

print("waiting for the advertising\r\n")
time.sleep(40)
print("advertising is over\r\n")
test_play = video_play_youku(driver)
test_play.play('480p')



time.sleep(20)
print 'game over'
driver.save_screenshot('over.png')
driver.close()
driver.quit()
