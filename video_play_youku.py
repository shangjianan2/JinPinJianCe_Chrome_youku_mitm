#!/usr/bin/env python
#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains

import time

class video_play_youku:
    def __init__(self, driver):
        self.driver = driver
        #查找必要的控件
        print("youku begin to find element")

        self.video = self.driver.find_element_by_xpath('//video')
        self.video_start = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div[14]/div/button')
        self.video_progress_bar = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/div/div[1]')
        self.video_progress_dot = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div/div/div[1]/div')

        self.definition = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div[4]/span[1]')
        self.definition_1080p = self.driver.find_element_by_xpath('//div[@data-val="1080p"]')
        self.definition_720p = self.driver.find_element_by_xpath('//div[@data-val="720p"]')
        self.definition_480p = self.driver.find_element_by_xpath('//div[@data-val="480p"]')
        #self.definition_320p = self.driver.find_element_by_xpath('//div[@data-val="320p"]')
        print("has find all the elements")

    def play(self, definition_youku):
        ActionChains(self.driver).click(self.video_start).perform()
        time.sleep(1)
        self.set_definition(definition_youku)
        self.reset_progress()


    def set_definition(self, definition_youku):
        time.sleep(1)
        ActionChains(self.driver).move_to_element(self.video).perform()#以下两行是为了呼叫出video控制面板
        ActionChains(self.driver).move_by_offset(0, (self.video.size['height'] / 2 - 20)).perform()
        time.sleep(1)
        ActionChains(self.driver).click(self.definition).perform()
        self.driver.save_screenshot('youku_set_definition.png')
        time.sleep(1)

        #切换清晰度
        if definition_youku == '1080p':
            ActionChains(self.driver).click(self.definition_1080p).perform()
        elif definition_youku == '720p':
            ActionChains(self.driver).click(self.definition_720p).perform()
        elif definition_youku == '480p':
            ActionChains(self.driver).click(self.definition_480p).perform()
        #elif definition_youku == '320p':
        #    ActionChains(self.driver).click(self.definition_320p).perform()
        else :
            print("param unvalid")
        time.sleep(1)

    def reset_progress(self):
        #优酷平台貌似自动从初始位置播放
        time.sleep(1)
        ActionChains(self.driver).move_to_element(self.video).perform()#以下两行是为了呼叫出video控制面板
        ActionChains(self.driver).move_by_offset(0, (self.video.size['height'] / 2 - 20)).perform()
        time.sleep(1)

        ActionChains(self.driver).move_to_element(self.video_progress_bar).perform()#将鼠标移动至进度条中部
        ActionChains(self.driver).move_by_offset(-(self.video_progress_bar.size['width'] / 2 - 1), 0).perform()#将鼠标移动至进度条头部
        ActionChains(self.driver).click().perform()#在鼠标当前位置点击
        time.sleep(1)


if __name__ == "__main__":
    driver = webdriver.Firefox(firefox_profile='./profile', executable_path='./geckodriver1.exe')#geckodriver的最新版本

    driver.implicitly_wait(30)#设置加载driver加载元素时所等待的最长的时间，
    driver.get("https://v.youku.com/v_show/id_XMzE0NDQxNTg4.html?spm=a2h0k.11417342.soresults.dposter")

    test_login = login_youku.login_youku(driver, '1978707987', '130103020152')
    test_login.login_with_QQ()
    time.sleep(1)
    test = video_play_youku(driver)
    time.sleep(35)
    test.play("720p")
    print("video_play_youku test over")
