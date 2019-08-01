from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')


driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='./chromedriver')

# go to the google home page
#driver.get("https://www.iqiyi.com/v_19rrdh6354.html")
driver.get("https://v.youku.com/v_show/id_XMzE0NDQxNTg4.html?spm=a2h0k.11417342.soresults.dposter")
time.sleep(35)
#by_ip = driver.find_element_by_xpath('//video')
#by_ip.click()

# the page is ajaxy so the title is originally this:
print 'game over'
driver.save_screenshot('s.png')

#time.sleep(20)
driver.close()
driver.quit()
