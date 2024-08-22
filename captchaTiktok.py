import base64
import io
from time import sleep
from PIL import Image

import requests
from autoselenium import AutoSelenium
from captchaguru import CaptchaGuru
from omocaptcha import Omocaptcha
from selenium.webdriver.common.action_chains import ActionChains
class CapchaTiktok(AutoSelenium):
    def __init__(self, api_key, site="omocaptcha") -> None:
        super().__init__()
        self.site = site
        print(site)
        if site == "Omocaptcha": self.omocaptcha = Omocaptcha(api_key)
        elif site == "Captcha.guru": self.guru = CaptchaGuru(api_key)
        # self.tryCount = 0
    def isShowCaptcha(self):
        source = self.driver.page_source
        return 'role="dialog"' in source  and "captcha_verify_container" in source
    def isVerifySuccess(self):
        return 'captcha_verify_message captcha_verify_message-pass' in self.driver.page_source 
    def isVerifyFail(self):
        return 'captcha_verify_message captcha_verify_message-fail' in self.driver.page_source
    def isVerifyGoing(self):
        return 'captcha_verify_message captcha_verify_message-going' in self.driver.page_source
    def checkSuccessCaptcha(self):
        for j in range(10):
            print(j)
            if self.isVerifySuccess(): return True
            elif self.isVerifyFail(): 
                self.refreshCaptcha()
                sleep(5)
                return False
            elif 'data-e2e="profile-icon"' in self.driver.page_source: return True
            sleep(0.1)
        if self.isVerifyGoing(): 
            self.refreshCaptcha()
            sleep(5)

            return False
    def clickShape(self, x1, y1, x2, y2):
        driver = self.driver
        driver.implicitly_wait(20) 
        el = driver.find_element('xpath', "//div[contains(@class, 'captcha_verify_img')]")
        w, h = -el.size["width"], el.size["height"]
        ActionChains(driver).move_to_element_with_offset(el, w/2, h/2).move_by_offset(x1, -h+y1).click().perform()
        ActionChains(driver).move_to_element_with_offset(el, w/2, h/2).move_by_offset(x2, -h+y2).click().perform()
    def slide(self, x):
        action = ActionChains(self.driver)
        self.driver.implicitly_wait(30)
        el = self.driver.find_element('xpath', '//*[@id="captcha_container"]/div/div[3]/div[2]/div[2]')
        action.move_to_element(to_element=el)
        action.click_and_hold(on_element=el)
        for i in range(5):
            action.move_by_offset(round(float(x/5)), 0)
            action.pause(0.3)
        action.release()
        action.perform()
    def refreshCaptcha(self):
        self.ClickJsWebElement('xpath', '//span[text()="Làm mới"]')
    def confirmCaptcha(self):
        self.ClickJsWebElement('xpath', '//div[text()="Xác nhận"]')
    def getBase64Url(self, url):
        return str(base64.b64encode(requests.get(url).content)).replace("b'", '').replace("'", '')
    def captchaSameShape(self):
        driver = self.driver
        driver.implicitly_wait(20)
        src = driver.find_element('xpath', '//img').get_attribute('src')
        image_base64 = self.getBase64Url(src)
        buffer = io.BytesIO()
        imgdata = base64.b64decode(image_base64)
        img = Image.open(io.BytesIO(imgdata))
        new_img = img.resize((340, 212))  # x, y
        new_img.save(buffer, format="PNG")
        img_b64 = str(base64.b64encode(buffer.getvalue()))[2:-1]
        x1, y1, x2, y2 = None, None, None, None
        if self.site == "Omocaptcha":
            data = {"type_job_id": "22","image_base64": img_b64,"width_view": 340,"height_view": 212}
            self.omocaptcha.createJob(data=data)
            if self.omocaptcha.id is not None:
                result = self.omocaptcha.getJobResult()
                if result is not None: 
                    x1, y1, x2, y2 = result.split("|")
        elif self.site == "Captcha.guru":
            data = {'textinstructions': "abc", 'click': 'geetest', 'key': self.guru.api_key, "now": "1", 'type': 'base64', 'body': img_b64}
            if self.guru.createJob(data):
                result = self.guru.getResult()
                print(result)
                if result is not None: 
                    postion = []
                    coordinates = result.split(":")[-1]
                    coordinate = coordinates.split(";")
                    for i in coordinate:
                        pos = i.split(",")
                        for p in pos: postion.append(p.split("=")[-1].strip())
                    x1, y1, x2, y2 = postion
        if x1 is not None:
            self.clickShape(int(x1),int(y1),int(x2),int(y2))
            self.confirmCaptcha()
        else:
            self.refreshCaptcha()
            sleep(5)
            self.captchaSameShape()
    def captchaRotating(self):
        # try:
            driver = self.driver
            self.driver.implicitly_wait(30)
           
            src = driver.find_elements('xpath', '//img')
            outside = src[0].get_attribute('src')
            inside = src[1].get_attribute('src')
            
          
            xofset = None
            if self.site == "Omocaptcha":
                image_base64_outside = self.getBase64Url(outside)
                image_base64_inside = self.getBase64Url(inside)
                data = {"type_job_id": "23","image_base64": "%s|%s"%(image_base64_inside, image_base64_outside)}
                self.omocaptcha.createJob(data=data)
                if self.omocaptcha.id is not None:
                    result = self.omocaptcha.getJobResult()
                    if result is not None: xofset = int(result)
            elif self.site == "Captcha.guru":
                print(outside)
                print(inside)
                ee1 = base64.b64encode((outside.encode('utf-8')))
                ee2 = base64.b64encode((inside.encode('utf-8')))
                data = {'textinstructions': 'koleso', 'click': 'geetest', 'key': self.guru.api_key, 'method': 'base64', 'body0': ee1, 'body1': ee2}
                if self.guru.createJob(data):
                    result = self.guru.getResult()
                    print(result)
                    if result is not None: 
                        xofset = int(result.split("y=")[-1])
            if isinstance(xofset, int): 
                self.slide(xofset)
            else:
                self.refreshCaptcha()
                sleep(5)
                self.captchaRotating()
        # except: 
        #     self.tryCount += 1
        #     return self.captchaRotating()
    def captchaSlide(self):
        driver = self.driver
        driver.implicitly_wait(20)
        src = driver.find_element('xpath', '//img').get_attribute('src')
        image_base64 = self.getBase64Url(src)
        buffer = io.BytesIO()
        imgdata = base64.b64decode(image_base64)
        img = Image.open(io.BytesIO(imgdata))
        new_img = img.resize((340, 212))  # x, y
        new_img.save(buffer, format="PNG")
        img_b64 = str(base64.b64encode(buffer.getvalue()))[2:-1]
        xofset = None
        if self.site == "Omocaptcha":
            data = {"type_job_id": "21","image_base64": img_b64,"width_view": 340}
            self.omocaptcha.createJob(data=data)
            if self.omocaptcha.id is not None:
                result = self.omocaptcha.getJobResult()
                if result is not None: 
                    xofset = int(result)
        elif self.site == "Captcha.guru":
            data = {'textinstructions': "silder", 'click': 'geetest', 'key': self.guru.api_key, "now": "1", 'type': 'base64', 'body': img_b64}
            if self.guru.createJob(data):
                result = self.guru.getResult()
                print(result)
                if result is not None: 
                    xofset = int(result.split("|")[-1])
        if isinstance(xofset, int):
            self.slide(int(result))
        else:
            self.refreshCaptcha()
            sleep(5)
            self.captchaSlide()