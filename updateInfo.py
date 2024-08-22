import os
import random
from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class UpdateInfo:
    def setDiver(self, driver: Chrome):
        self.__driver = driver
    def clickEditProfile(self):
        while True:
            try:
                self.__driver.implicitly_wait(1)
                self.__driver.find_element('xpath', '''//input[contains(@class, 'InputUpload')]''')
                break
            except:
                self.__driver.implicitly_wait(30)
                try:
                    self.__driver.find_element('xpath', '//div[@data-e2e="edit-profile-entrance"]//button').click()
                except: continue
            
    def move_to_click(self, by, value):
        self.__driver.implicitly_wait(30)
        el = self.__driver.find_element(by, value)
        self.__driver.execute_script('''arguments[0].scrollIntoView({ behavior: 'smooth' });''', el)
        self.__driver.execute_script('''arguments[0].click();''', el)
    def deleteText(self, element):
        while True:
            try:
                element.send_keys(Keys.CONTROL+"a")
                element.send_keys(Keys.DELETE)
                if element.text == "": break
            except: pass
    def updateAvatar(self, path):
        self.__driver.implicitly_wait(30)
        file = random.choice(os.listdir(path))
        img = os.path.join(path, file)
        self.__driver.find_element('xpath', "//input[contains(@class, 'InputUpload')]").send_keys(img)
        sleep(2)
        self.move_to_click('xpath', '//*[text()="Đăng ký"]')
        # sleep(2)
        # self.move_to_click('xpath', '//*[text()="Lưu"]')
    def updateTikTokID(self, tiktokID):
        child_elements = self.__driver.find_element('xpath', '//div[@data-e2e="edit-profile-username-input"]').find_elements('xpath', './/*')
        for child_element in child_elements:
            if child_element.tag_name == "input":
                self.deleteText(self.__driver.find_element('xpath', '//div[@data-e2e="edit-profile-username-input"]//input'))
                sleep(1)
                self.__driver.find_element('xpath', '//input[@placeholder="TikTok ID"]').send_keys(tiktokID)
                sleep(1)
                if self.checkValidTikTokID(): return tiktokID
                else: return self.updateTikTokID(tiktokID+str(random.randint(1, 10)))
    def checkValidTikTokID(self):
        self.__driver.implicitly_wait(1)
        while True:
            try:
                self.__driver.find_element('xpath', '//*[contains(@class, "InputError")]')
                return False
            except: pass
            try:
                self.__driver.find_element('xpath', '//*[contains(@class, "StyledTickBold")]')
                return True
            except: pass
    def updateName(self, name):
        child_elements = self.__driver.find_element('xpath', '//div[@data-e2e="edit-profile-name-input"]').find_elements('xpath', './/*')
        for child_element in child_elements:
            if child_element.tag_name == "input":
                self.deleteText(self.__driver.find_element('xpath', '//div[@data-e2e="edit-profile-name-input"]//input'))
                sleep(1)
                self.__driver.find_element('xpath', '//div[@data-e2e="edit-profile-name-input"]//input').send_keys(name)
        

    def updateBio(self, bio):
        self.deleteText(self.__driver.find_element('xpath', '//*[@data-e2e="edit-profile-bio-input"]'))
        sleep(1)
        self.__driver.find_element('xpath', '//*[@data-e2e="edit-profile-bio-input"]').send_keys(bio)