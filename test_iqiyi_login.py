import sys
reload(sys)
sys.setdefaultencoding('utf8')
print sys.getdefaultencoding()


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
driver.get("https://www.iqiyi.com/v_19rrdh6354.html")
time.sleep(35)

print 'start up'
driver.find_element_by_xpath('/html/body/div[2]/div/header/div/div/div[4]/div[6]/div[1]/div/a').click()
time.sleep(1)
switch_to_loginframe = driver.find_element_by_xpath('//iframe[@id="login_frame"]')
driver.switch_to_frame(switch_to_loginframe)
driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[4]/div[2]/p/span/a[2]').click()
driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[5]/div[1]/div/div/a[2]').click()

driver.switch_to_window(driver.window_handles[1])

driver.save_screenshot('s1.png')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="userId"]').send_keys("18203355025")
driver.save_screenshot('s2.png')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="passwd"]').send_keys("005448")
driver.save_screenshot('s3.png')
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/form/div/div[2]/div/p/a[1]').click()
time.sleep(5)
driver.find_element_by_xpath('//input[@tabindex="3"][@node-type="vcode"]').send_keys("005448")
time.sleep(5)
pincode = driver.find_element_by_xpath('//img[@node-type="pincode"]')
pincode.screenshot('pincode.png')
driver.save_screenshot('s3_1.png')


html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
driver.save_screenshot('s3_2.png')

print 'has login'
time.sleep(20)
driver.switch_to_window(driver.window_handles[0])
driver.refresh()
#driver.find_element_by_xpath('/html/body/div[2]/div/header/div/div/div[4]/div[6]/div[1]/div/a').perform()
#//*[@id="block-A"]/div/div/div[4]/div[6]/div[1]/div/a
time.sleep(30)
driver.save_screenshot('s4.png')


print 'game over'
driver.save_screenshot('s.png')

driver.close()
driver.quit()
