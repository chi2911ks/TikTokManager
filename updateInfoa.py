import os
import random
from time import sleep
from selenium.webdriver import Chrome


class UpdateInfo:
    def setDiver(self, driver: Chrome):
        self.__driver = driver
    def clickEditProfile(self):
        self.__driver.implicitly_wait(30)
        self.__driver.find_element('xpath', '//div[@data-e2e="edit-profile-entrance"]//button').click()
    def updateAvatar(self, path):
        self.__driver.implicitly_wait(30)
        file = random.choice(os.listdir(path))
        img = os.path.join(path, file)
        self.__driver.find_element('xpath', "//input[contains(@class, 'InputUpload')]").send_keys(img)
        sleep(2)
        self.__driver.execute_script("arguments[0].click();", self.__driver.find_element('xpath', '//*[text()="Đăng ký"]'))
        sleep(2)
        self.__driver.execute_script("arguments[0].click();", self.__driver.find_element('xpath', '//*[text()="Lưu"]'))
    def updateTikTokID(self, tiktokID):
        self.__driver.find_element('xpath', '//input[@placeholder="TikTok ID"]').clear()
        sleep(1)
        self.__driver.find_element('xpath', '//input[@placeholder="TikTok ID"]').send_keys(tiktokID)
    def updateName(self, name):
        self.__driver.find_element('xpath', '//div[@data-e2e="edit-profile-name-input"]//input').clear()
        sleep(1)
        self.__driver.find_element('xpath', '//div[@data-e2e="edit-profile-name-input"]//input').send_keys(name)
    def updateBio(self, bio):
        self.__driver.find_element('xpath', '//*[@data-e2e="edit-profile-bio-input"]').clear()
        sleep(1)
        self.__driver.find_element('xpath', '//*[@data-e2e="edit-profile-bio-input"]').send_keys(bio)