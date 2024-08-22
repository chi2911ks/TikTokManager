# -*- coding: utf-8 -*-
import datetime
from time import sleep
from autoselenium import AutoSelenium
from captchaTiktok import CapchaTiktok
from config import Config
from databasehandle import DataBaseHandleTikTok
from uploadVideo import UploadVideoTiktok
from omocaptcha import Omocaptcha
import os
from gologin import Gologin
from PyQt5 import QtCore
semaWrite = QtCore.QSemaphore(1)
class TikTok(CapchaTiktok):
    
    def __init__(self, this, row, username, password, cookie, api_key, x, y, proxy) -> None:
        super().__init__(api_key, this._this.fSetting.cbAPICaptcha.currentText())
        self.this = this
        self.row = row
        self.username = username
        self.password = password
        self.cookie = cookie
        self.x = x
        self.y = y
        this.show.emit(self.row, self.this._this.col_status, "Đang mở chrome...")
        
        self.profile = os.path.abspath(os.path.join("profile", username))
        if not os.path.exists(self.profile):
            gologin = Gologin()
            gologin.createProfile(username)
        self.getDriver(profile=self.profile, x=self.x, y=self.y, width=500, height=700, version=self.this.version_main, proxy=proxy, headless=self.this._this.fSetting.rbHidenChrome.isChecked(), chromedriver=os.path.abspath("ChromeDrivers\\chromedriver.exe"), binary_location=os.path.abspath("Data\\orbita-browser\\chrome.exe"))
        # self.driver.set_window_size(500, 700)
        self.driver.set_window_position(self.this.x, self.this.y)
        # self.driver.get("https://gleam.io")
       
        # sleep(100)
        self.SetSizeWeb(0.5)
    def addCookie(self):
        self.driver.get("https://www.tiktok.com/")
        cookie_list = self.cookie.split(';')
        for cookie in cookie_list:
            cookie_parts = cookie.strip().split('=')
            if len(cookie_parts) == 2:
                cookie_name, cookie_value = cookie_parts[0], cookie_parts[1]
                one_year_from_now = datetime.datetime.now() + datetime.timedelta(days=365)
                expiry_timestamp = int(one_year_from_now.timestamp())
                self.driver.add_cookie({'name': cookie_name, 'value': cookie_value, 'expiry': expiry_timestamp})
              
        self.driver.get("https://www.tiktok.com/")
        sleep(1)
        return self.checkLogin()
    @property
    def cookieTiktok(self):
        cookies = ""
        web = self.driver.get_cookies()
        for ck in web:
            cookies += "%s=%s;"%(ck["name"], ck["value"])
        return cookies
    @property
    def checkAttemptsReached(self):
        return 'Maximum number of attempts reached. Try again later.'
    @property
    def checkBanned(self):
        return 'Tài khoản của bạn đã bị đình chỉ.'
    @property
    def checkAttemptsAccess(self):
        return 'Bạn truy cập dịch vụ của chúng tôi quá thường xuyên.'
    @property
    def checkError(self):
        return 'Rất tiếc, đã xảy ra lỗi, vui lòng thử lại sau'
    @property
    def page_source(self):
        # try:
            return self.driver.page_source
        # except: return self.page_source
    def isLogged(self):
        return 'data-e2e="profile-icon"' in self.page_source
    def isLogin(self):
        return 'login-button' in self.page_source
    
    def statusLogin(self):
        try:
            self.driver.implicitly_wait(0.1)
            return self.driver.find_element('xpath', '//*[@role="status"]').text
        except: return None
    
    
    def checkCaptcha(self):
        for i in range(10):
            if not self.isShowCaptcha(): break
            if "Kéo thanh trượt để ghép hình" in self.page_source:
                self.this.show.emit(self.row, self.this._this.col_status, "Bắt đầu giải captcha xoay...")
                self.captchaRotating()
                if not self.checkSuccessCaptcha(): return self.checkCaptcha()
            elif "Xác minh để tiếp tục:" in self.page_source:
                self.this.show.emit(self.row, self.this._this.col_status, "Bắt đầu giải captcha kéo...")
                self.captchaSlide()
                if not self.checkSuccessCaptcha(): return self.checkCaptcha()
                # print("Vui lòng thêm captcha loại này!")
            elif "Chọn 2 đối tượng có hình dạng giống nhau:" in self.page_source:
                self.this.show.emit(self.row, self.this._this.col_status, "Bắt đầu giải captcha 2 đối tượng...")

                self.captchaSameShape()
                if not self.checkSuccessCaptcha(): return self.checkCaptcha()
            elif "hCaptcha" in self.page_source: return "hcaptcha"
            sleep(1)
    def showCookie(self):
        self.this.show.emit(self.row, 5, self.cookieTiktok)
        DataBaseHandleTikTok.updateRow(self.username, "cookie", self.cookieTiktok)
        # semaWrite.acquire()
        # # if os.path.exists("data.json"):
            
        # #     cf = Config()
        # #     data = cf.getDataFileJson("data.json")
        # #     data["accounts"][self.username.strip()]["cookie"] = self.cookieTiktok
        # #     cf.writeDataFileJson("data.json", data)
        # semaWrite.release()
    def saveDescription(self, text):

        self.this.show.emit(self.row, self.this._this.col_description, text)
        DataBaseHandleTikTok.updateRow(self.username, "description", text)
    def checkLogin(self):
        self.this.show.emit(self.row, self.this._this.col_status, "Kiểm tra đăng nhập...")
        self.driver.get("https://www.tiktok.com/profile")
        for i in range(15):
            if self.isLogged(): 
                self.this.show.emit(self.row, self.this._this.col_status, "Đăng nhập thành công!")
                self.saveDescription("Đã đăng nhập!")

                self.showCookie()
                return True
            elif self.isLogin(): 
                self.this.show.emit(self.row, self.this._this.col_status, "Chưa đang nhập!")
                return False
            sleep(1)
    def loginSuccess(self):
        self.this.show.emit(self.row, self.this._this.col_status, "Đăng nhập thành công!")
        self.saveDescription("Đăng nhập thành công!")

        self.showCookie()
        print("Đăng nhập thành công!")
        self.driver.get("https://www.tiktok.com/profile")
        sleep(5)
    def spamClickLogin(self, count: int=10):
        for i in range(count):
            print(i)
            if self.isLogged(): 
                self.loginSuccess()
                return True
            if self.isShowCaptcha(): 
                print("captcha")
                sleep(5)
                if self.checkCaptcha() == "hcaptcha":
                    self.this.show.emit(self.row, self.this._this.col_status, "Hcaptcha không giải được, đăng nhập thất bại!")
                    return False
                sleep(10)
                return
            try:
                self.ClickJsWebElement("xpath", "//button[@data-e2e=\"login-button\"]", timeout=0.1)
            except:pass
            sleep(1)
    def loginByUsername(self):
        if self.cookie != "":
            return self.addCookie()
        self.this.show.emit(self.row, self.this._this.col_status, "Bắt đầu đăng nhập tài khoản...")

        self.driver.get("https://www.tiktok.com/login/phone-or-email/email")
        while True:
            self.driver.implicitly_wait(1)
            try:
                self.driver.find_element('xpath', '//button[@data-list-item-value="email/username"]').click()
            except: pass
            try:
                self.driver.find_element("name", "username").send_keys(self.username)
                break
            except: pass
        # self.ClickJsWebElement("name", "username", self.username)
        sleep(1)
        self.ClickJsWebElement("xpath", "//input[@type=\"password\"]", self.password)
        sleep(1)
        self.ClickJsWebElement("xpath", "//button[@data-e2e=\"login-button\"]")
        chkStatus = False
        for i in range(40):
            isLogin = self.isLogged()
            status = self.statusLogin()
            if isLogin:
                self.loginSuccess()
                return True
            elif status:
                self.this.show.emit(self.row, self.this._this.col_status, status)
                self.saveDescription(status)
                # return False
                print(status+"!")
                if status == self.checkAttemptsAccess or status == self.checkError:
                    if not chkStatus:
                        self.spamClickLogin()
                        chkStatus = True
                    else: return False
                # elif status == self.checkAttemptsReached or status == self.checkBanned:
                #     return False
                else: return False
            elif self.isShowCaptcha(): 
                # if "hCaptcha" in self.page_source: 
                #     self.this.show.emit(self.row, self.this._this.col_status, "Đăng nhập thất bại, do hcaptcha chưa hỗ trợ!")

                #     return False
                print("Đã tìm thấy captcha!")
                self.this.show.emit(self.row, self.this._this.col_status, "Đã tìm thấy captcha!")
                if self.checkCaptcha() == "hcaptcha":
                    self.this.show.emit(self.row, self.this._this.col_status, "Hcaptcha không giải được, đăng nhập thất bại!")
                    return False
                sleep(10)
            sleep(0.1)
        self.this.show.emit(self.row, self.this._this.col_status, "Đăng nhập thất bại!")
        self.saveDescription("Đăng nhập thất bại!")
        # self.this.statusTiktok.emit(self.row, self.this._this.col_status, "Đăng nhập thất bại!")
        return False
    def uploadVideo(self, path, content, schedule):
        
        upload = UploadVideoTiktok(self.driver)
        self.this.show.emit(self.row, self.this._this.col_status, "Đang upload video...")

        if upload.uploadVideo(path, content, schedule):
            self.this.show.emit(self.row, self.this._this.col_status, "Upload thành công!")
            return True
        else:
            self.this.show.emit(self.row, self.this._this.col_status, "Upload thất bại!")
            return False
    
        


        
# LoginTikTok("user2977286918288", "123456@a", "JGWKqGzssbNZEyxCF9NVywp8UzCVVwwNvGZA13IcK39kY0084yfJSpxZlDxzufSVVBmxdgqh6Qp77TZ3").run()
# Xác minh để tiếp tục:
# Kéo thanh trượt để ghép hình

# Rất tiếc, đã xảy ra lỗi, vui lòng thử lại sau