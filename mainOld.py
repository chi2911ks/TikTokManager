# -*- coding: utf-8 -*-
import datetime
import json
from time import sleep
from captchaTiktok import CapchaTiktok
from uploadVideo import UploadVideoTiktok
import os
from PyQt5 import QtCore
semaWrite = QtCore.QSemaphore(1)
class TikTok(CapchaTiktok):
    
    def __init__(self, this, row, username, password, cookie, api_key, x, y, proxy) -> None:
        super().__init__(api_key, "Omocaptcha")
        self.this = this
        self.row = row
        self.username = username
        self.password = password
        self.cookie = cookie
        self.x = x
        self.y = y
        this.show.emit(self.row, 3, "Đang mở chrome...")
        
        self.profile = os.path.abspath(os.path.join("profile", username))
        # if not os.path.exists(self.profile):
        #     gologin = Gologin()
        #     gologin.createProfile(username)
        paths = []
        for path in os.listdir("extensions"):
            cc = os.path.abspath("extensions")
            paths.append(os.path.join(cc, path))
        self.getDriver(profile=self.profile, extensions=",".join(paths), x=self.x, y=self.y, width=500, height=700, version=self.this.this.version_main.value(), proxy=proxy)
        # self.driver.set_window_size(500, 700)
        self.driver.set_window_position(self.x, self.y)
        # self.driver.get("https://gleam.io")
       
        # sleep(100)
        self.SetSizeWeb()
    # def addCookie(self):
    #     self.driver.get("https://www.tiktok.com/")
    #     cookie_list = self.cookie.split(';')
    #     for cookie in cookie_list:
    #         cookie_parts = cookie.strip().split('=')
    #         if len(cookie_parts) == 2:
    #             cookie_name, cookie_value = cookie_parts[0], cookie_parts[1]
    #             one_year_from_now = datetime.datetime.now() + datetime.timedelta(days=365)
    #             expiry_timestamp = int(one_year_from_now.timestamp())
    #             self.driver.add_cookie({'name': cookie_name, 'value': cookie_value, 'expiry': expiry_timestamp})
              
    #     self.driver.get("https://www.tiktok.com/")
    #     sleep(1)
    #     return self.checkLogin()
 
    def addCookieJ2Team(self):
        path = self.this.this.locationCookie.text()
        self.driver.get("https://www.tiktok.com/")
        # cc = {}
        # cc.pop()
        if os.path.exists(path):
            for c in os.listdir(path):
                if self.username in c:
                    cookies = json.loads(open(os.path.join(path, c), encoding="utf-8").read())["cookies"]
                    for cookie in cookies: 
                        # cookie.pop("sameSite")
                        # cookie["sameSite"] = "None"
                        one_year_from_now = datetime.datetime.now() + datetime.timedelta(days=365)
                        expiry_timestamp = int(one_year_from_now.timestamp())
                        # cookie.update({"expire": expiry_timestamp })
                        self.driver.add_cookie({'name': cookie["name"], 'value': cookie["value"], "expire": expiry_timestamp})
                        # self.executeCookie(cookie["name"], cookie["value"])
            self.driver.get("https://www.tiktok.com/")
            # sleep(10)
            return self.checkLogin()
                
        else: self.this.show.emit(self.row, 3, "Không có cookie này trong thư mục!")
    def addCookie(self):
        self.driver.get("https://www.tiktok.com/")
        # cookie_list = self.cookie.split(';')
        self.driver.execute_script('''var cookie = "%s"
var cookies = cookie.split(";");
for (var i = 0; i < cookies.length; i++) {
    document.cookie = cookies[i];
}'''%self.cookie)
        # for cookie in cookie_list:
        #     cookie_parts = cookie.strip().split('=')
        #     if len(cookie_parts) == 2:
        #         cookie_name, cookie_value = cookie_parts[0], cookie_parts[1]
        #         one_year_from_now = datetime.datetime.now() + datetime.timedelta(days=365)
        #         expiry_timestamp = int(one_year_from_now.timestamp())
        #         self.driver.add_cookie({'name': cookie_name, 'value': cookie_value, 'expiry': expiry_timestamp})
              
        self.driver.get("https://www.tiktok.com/")
        sleep(1)
        return self.checkLogin()
    def createJ2Team(self):
        if not os.path.exists("cookiej2team"): os.mkdir("cookiej2team")
        with open("cookiej2team\\%s.json"%self.username, 'w') as file:
            file.write(self.ConvertCookieJ2Team())
    def ConvertCookieJ2Team(self):
        # self.driver.get("https://www.tiktok.com/")
        
        dm = '{"url":"https://www.tiktok.com","cookies":[{"domain":".tiktok.com","expirationDate":1710170623.193059,"hostOnly":false,"httpOnly":false,"name":"_ttp","path":"/","sameSite":"no_restriction","secure":true,"session":false,"storeId":"0","value":"2LBlgV8K5FSfN7cKBGs2wpsxm3C"},{"domain":"www.tiktok.com","expirationDate":1707585694.968242,"hostOnly":true,"httpOnly":true,"name":"ttwid","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"1%7CarBCrmd9ppNI68pOGD3o0qzW9KGPzIxFao9k4y0VykA%7C1676049690%7C01e9cdbc94d306782c6cf60c4be3938513898e36b858c49e2f76be40eff0e407"},{"domain":".www.tiktok.com","expirationDate":1702567076,"hostOnly":false,"httpOnly":false,"name":"tiktok_webapp_theme","path":"/","sameSite":"unspecified","secure":true,"session":false,"storeId":"0","value":"light"},{"domain":".tiktok.com","expirationDate":1681233703.89739,"hostOnly":false,"httpOnly":false,"name":"passport_csrf_token","path":"/","sameSite":"no_restriction","secure":true,"session":false,"storeId":"0","value":"7bbe64c343db91f85b9b0225be3dee24"},{"domain":".tiktok.com","expirationDate":1681233703.897422,"hostOnly":false,"httpOnly":false,"name":"passport_csrf_token_default","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"7bbe64c343db91f85b9b0225be3dee24"},{"domain":".tiktok.com","expirationDate":1678812190.711985,"hostOnly":false,"httpOnly":true,"name":"passport_auth_status","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"97c0a98a240cf26bd570f92e224b4292%2C"},{"domain":".tiktok.com","expirationDate":1678812190.711997,"hostOnly":false,"httpOnly":true,"name":"passport_auth_status_ss","path":"/","sameSite":"no_restriction","secure":true,"session":false,"storeId":"0","value":"97c0a98a240cf26bd570f92e224b4292%2C"},{"domain":".www.tiktok.com","expirationDate":1677251876,"hostOnly":false,"httpOnly":false,"name":"__tea_cache_tokens_1988","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"{%22_type_%22:%22default%22%2C%22user_unique_id%22:%227198578561794491947%22%2C%22timestamp%22:1676531181818}"},{"domain":".tiktok.com","expirationDate":1676668675.878273,"hostOnly":false,"httpOnly":true,"name":"tt_chain_token","path":"/","sameSite":"unspecified","secure":true,"session":false,"storeId":"0","value":"XuLIUuI5dWJb8ZY5KvdkKA=="},{"domain":".tiktok.com","hostOnly":false,"httpOnly":true,"name":"tt_csrf_token","path":"/","sameSite":"lax","secure":true,"session":true,"storeId":"0","value":"Qml3zgYh-tEZE0sMkwoMgj-Gh-6GavHVdJJ0"},{"domain":".tiktok.com","expirationDate":1708183011.903075,"hostOnly":false,"httpOnly":false,"name":"_abck","path":"/","sameSite":"unspecified","secure":true,"session":false,"storeId":"0","value":"A71FB20D73F2955FA09C1473F0C6FEBB~0~YAAQUhBFdj4qZjiGAQAAkA7zXwkLUkFg696VRoa6lncyOQXQA0Sr0bzhUnE5ZDUgJhEcXXfRDL4WBftHVNNtGvb8JlXCKiu4bkWR1fZunB0rj9kHl0u1+89FUQu9oJQcQxm5h5Kb1mSAzqkdMHM4NGiLDsB65jW7M1HDWvKbRh8ZuF1XExTcVAyOnZpl9un5YXxCnhojGA2HaU4mT41iJR2OCVK8mISTGS3ZButJdHURdzUzVBVoWlsMhyjRg3LNZEBHoGQKVvlG8GBuGrKZ3+c9oT6ADBAZTc3vNQRN0J3pJo6BL0Dyo9DYspdWokG6ohaT24PUQu/lqE/B+skelEU5/lcfBXX1yFZiFpndTiDnwl5bVV0Srx/HNkSQeXhJCPvEdW0tOFlhl7xRnAvblDjcYFOJfjTQ~-1~-1~-1"},{"domain":".tiktok.com","expirationDate":1676661411.90311,"hostOnly":false,"httpOnly":false,"name":"bm_sz","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"057C65E30B768E15E12D3FB43F965842~YAAQUhBFdkEqZjiGAQAAkA7zXxL1RVxIzltmpf/4NNzhmdbjRqyxgkacQxx9qTnKeMGmtpTBoO7TP0vOBZEm2UhKuKHcPI4X/edPUqt98PpBTLxS0ncY+pkVDocRe4ffVlWYIXkr2sbHBafiGxM/y9QS9BRMJfarAl23oZc3UgNfcTn1JUb2qlFwwx/dEwLMrcmZ/sE4RaC61985btOirV0ffDOaWGWODhawCP+TrkZg3U94arnqWtiiLiHr56n77fmhmpneDqOqV5Ft8yNZXBEzZiUw7hhbfTGfNzZQ75MBN/U=~3617840~4535107"},{"domain":".tiktok.com","expirationDate":1676654211.641581,"hostOnly":false,"httpOnly":true,"name":"ak_bmsc","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"56A8E3A4E891540EEF2E654D3D4FAA73~000000000000000000000000000000~YAAQUhBFdk0qZjiGAQAAWxXzXxI8/aZg/2QuEB1gl5MBXACADmYnDPIW6n6cQCIAwCBcWQXAzX4ZcdkhiFEkiUYQ6kkTTQknTSG0+yKBTyH0zLELjUSVc460RVs5pRV6JxBJbNp2r52xT56wK2P5lSpsgugLJNRBTUT/TOXcTW5sjNLAi6g0FcvpCkD5ZhQNZn5xcpN2DEEku16f92q/r+oY/22WzTNoX+bmxqsbaJkBx0Vg2ZETDAuv0BNRMqMmyNauykI7ZF0OvvFk9mWP5Hi2ECunOA+cR1JTkhBoTTPJ1U1eFBCZAfF5mi8R4yVzg2jwQPp71gk0ITdKGmrS8fqPSpdN3Ro0rm/17HqKlkUW+/NnF066TmgSPJakDZx4+GOqogWA/8Yz6pS0n5tztHifeXjQrExlvgNS3ku2Bq1mP26JUxVZSjGBuV6dfWs6fapSJpX41cXBkL168nEyapSe+96+0SuzRdFaR52SGG4a2yfh84ChCd8NQw=="},{"domain":".tiktok.com","hostOnly":false,"httpOnly":false,"name":"s_v_web_id","path":"/","sameSite":"no_restriction","secure":true,"session":true,"storeId":"0","value":"verify_le8oddkq_xFWp20RM_ZdpO_48wR_BKkO_ParJG6R0AAKq"},{"domain":".tiktok.com","expirationDate":1681831073.704403,"hostOnly":false,"httpOnly":true,"name":"cmpl_token","path":"/","sameSite":"unspecified","secure":true,"session":false,"storeId":"0","value":"AgQQAPOFF-RO0rLVHnuj-d0i-YfkDvRa_4MOYMn8QQ"},{"domain":".tiktok.com","expirationDate":1707751073.704432,"hostOnly":false,"httpOnly":true,"name":"sid_guard","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"29aa9c7bb66a7c8a20d4a96c34ef662e%7C1676647071%7C5184000%7CTue%2C+18-Apr-2023+15%3A17%3A51+GMT"},{"domain":".tiktok.com","expirationDate":1681831073.704443,"hostOnly":false,"httpOnly":true,"name":"uid_tt","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"fa4ca849af69fae2f6c269d908c2724714fd89fe93421bbdb5fdd295637d48d4"},{"domain":".tiktok.com","expirationDate":1681831073.704454,"hostOnly":false,"httpOnly":true,"name":"uid_tt_ss","path":"/","sameSite":"no_restriction","secure":true,"session":false,"storeId":"0","value":"fa4ca849af69fae2f6c269d908c2724714fd89fe93421bbdb5fdd295637d48d4"},{"domain":".tiktok.com","expirationDate":1681831073.704464,"hostOnly":false,"httpOnly":true,"name":"sid_tt","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"29aa9c7bb66a7c8a20d4a96c34ef662e"},{"domain":".tiktok.com","expirationDate":1681831073.704473,"hostOnly":false,"httpOnly":true,"name":"sessionid","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"29aa9c7bb66a7c8a20d4a96c34ef662e"},{"domain":".tiktok.com","expirationDate":1681831073.704483,"hostOnly":false,"httpOnly":true,"name":"sessionid_ss","path":"/","sameSite":"no_restriction","secure":true,"session":false,"storeId":"0","value":"29aa9c7bb66a7c8a20d4a96c34ef662e"},{"domain":".tiktok.com","expirationDate":1681831073.704495,"hostOnly":false,"httpOnly":true,"name":"sid_ucp_v1","path":"/","sameSite":"unspecified","secure":true,"session":false,"storeId":"0","value":"1.0.0-KDkwZDgxYmU3NjBhZDc3ZTZlOTVjN2QzNmM3ZmFlZDBiZWY3ZTlhYTAKIAibiKzewpv89WIQn7W-nwYYswsgDDDl4q-XBjgEQOoHEAMaBm1hbGl2YSIgMjlhYTljN2JiNjZhN2M4YTIwZDRhOTZjMzRlZjY2MmU"},{"domain":".tiktok.com","expirationDate":1681831073.704505,"hostOnly":false,"httpOnly":true,"name":"ssid_ucp_v1","path":"/","sameSite":"no_restriction","secure":true,"session":false,"storeId":"0","value":"1.0.0-KDkwZDgxYmU3NjBhZDc3ZTZlOTVjN2QzNmM3ZmFlZDBiZWY3ZTlhYTAKIAibiKzewpv89WIQn7W-nwYYswsgDDDl4q-XBjgEQOoHEAMaBm1hbGl2YSIgMjlhYTljN2JiNjZhN2M4YTIwZDRhOTZjMzRlZjY2MmU"},{"domain":".tiktok.com","expirationDate":1681831073.983148,"hostOnly":false,"httpOnly":true,"name":"store-idc","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"useast2a"},{"domain":".tiktok.com","expirationDate":1681831073.983181,"hostOnly":false,"httpOnly":true,"name":"store-country-code","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"vn"},{"domain":".tiktok.com","expirationDate":1681831073.9832,"hostOnly":false,"httpOnly":true,"name":"store-country-code-src","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"uid"},{"domain":".tiktok.com","expirationDate":1681831073.983216,"hostOnly":false,"httpOnly":true,"name":"tt-target-idc","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"alisg"},{"domain":".tiktok.com","expirationDate":1708183074.142736,"hostOnly":false,"httpOnly":true,"name":"tt-target-idc-sign","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"iRm3zvttyfrbFxAA-U31OGuartgNEyud2bOapLsGrN4EOsPYm1JEdTLsuStMYL43NpGa9Y2ePACyexVQxdzXKd2KNWA762cFH8vVUHegGvfEi0bKLyh_95etTeIwZuClgS_CzO6KRGpmBGXrNdJrdPx4hKk5U776DS8GcAQb12hxUPj1ZuZQWUc5u9AQmj-Ve3IWAuZUiazeIpUdPBlNQihdisE1X6rlpAUcOinjwpG-5P7rlqcQqtddIuEZFNQ8yrwsXi0zdMPhIEJBtM5CJ_AaqWahmf7PDVYTpOrdJuI3_X6gBDI6CeK0WoaOZF7R-9zVUsG4xOKZ0SvEMKMRVAWf3dgtuRxDEenK9X8M5DUve-atuhP3hymqy6W88BGKwFPfKADCaLMUKEFSkG1WV5Ey8T2fnLKZOKF7bw7MphT9NODtIEGaDTBTyMVJle09kVfJ7MFEPOfD9Dew9jJgXxuIUX3OhD41-sFStTiDWrMqMv52PKSHywTA8dwivk2H"},{"domain":".www.tiktok.com","hostOnly":false,"httpOnly":false,"name":"passport_fe_beating_status","path":"/","sameSite":"unspecified","secure":false,"session":true,"storeId":"0","value":"true"},{"domain":".tiktok.com","expirationDate":1708183078.629616,"hostOnly":false,"httpOnly":true,"name":"ttwid","path":"/","sameSite":"no_restriction","secure":true,"session":false,"storeId":"0","value":"1%7Cw6soajNXYudsZ_F5su59vPy3jjjXbVSUf2rf6ASr-Oc%7C1676647076%7C41bc704aea99f95c155d89207050ae5d2e598008ee084d9d1512a3933b9f7964"},{"domain":".tiktok.com","expirationDate":1708183079.407064,"hostOnly":false,"httpOnly":true,"name":"odin_tt","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"2aaebdc5ecf0fccdff6b293c176e63ac11b881db017d5e5460a9b2e67193206f0da5b41d871483644216727f1c33a81ad52a75709a6c7e698085ae4462e1e08b4d6c6b316dd3caf6bca71eb3b2fe3ee6"},{"domain":".tiktok.com","expirationDate":1676654215.409467,"hostOnly":false,"httpOnly":false,"name":"bm_sv","path":"/","sameSite":"unspecified","secure":true,"session":false,"storeId":"0","value":"76B00AEB44BD7C57990CAEE3069456A7~YAAQIhFFdgHk5CWGAQAAJBr0XxKlBCAuDubsc5k/7pxamD+oZZ6hI0J1ydMwxjpyJhSdZOc2uoy5TDfoF6/Pg1cAr6YGuvN5leeHSyF1RUHGfCVP1ssik3y+wCGhQqn/mdFmWXaKehrkqNJuCQQgEx1b4qrYuJbSJzhPaL/TgEASZUl0k6HhYYWZ/LCsG6E8ChzBn9AVOJldvEvPYaTKwmlaRaTP/cgiA77LTRgDzzlyt3v8S+8iNEIf4cPfZf4c~1"},{"domain":".tiktok.com","expirationDate":1677511081.85999,"hostOnly":false,"httpOnly":false,"name":"msToken","path":"/","sameSite":"no_restriction","secure":true,"session":false,"storeId":"0","value":"MqDUaPmu29XKrRRLWl6vTCDAmc074DGRDvC_nCC6oD03K5HMHDyg203pYNGZojwZJoNFjTtoVkeFhDjDnjH21fb20lk8Jr11MpgonB5yXP50Qr6D5ocbUTviQrgzuu70Q4fbdaPmWcw0gEys9g=="},{"domain":"www.tiktok.com","expirationDate":1684423081,"hostOnly":true,"httpOnly":false,"name":"msToken","path":"/","sameSite":"unspecified","secure":false,"session":false,"storeId":"0","value":"MqDUaPmu29XKrRRLWl6vTCDAmc074DGRDvC_nCC6oD03K5HMHDyg203pYNGZojwZJoNFjTtoVkeFhDjDnjH21fb20lk8Jr11MpgonB5yXP50Qr6D5ocbUTviQrgzuu70Q4fbdaPmWcw0gEys9g=="}]}'
        file =  json.loads(dm)["cookies"]
        cookie = {"url":"https://www.tiktok.com","cookies": ""}
        cc = []
        for i in file:
            for ii in self.driver.get_cookies():
                if i["name"] == ii["name"]:
                    if 'expiry' in ii:
                        i.update({'expirationDate': ii['expiry']})
                    i.update({"value": ii["value"]})
            cc.append(i)
        cookie.update({"cookies": cc})
        return str(cookie).replace("'", '"').replace(' ', '').replace('True', 'true').replace('False', 'false')
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
                self.this.show.emit(self.row, 3, "Bắt đầu giải captcha xoay...")
                self.captchaRotating()
                if not self.checkSuccessCaptcha(): return self.checkCaptcha()
            elif "Xác minh để tiếp tục:" in self.page_source:
                self.this.show.emit(self.row, 3, "Bắt đầu giải captcha kéo...")
                self.captchaSlide()
                if not self.checkSuccessCaptcha(): return self.checkCaptcha()
                # print("Vui lòng thêm captcha loại này!")
            elif "Chọn 2 đối tượng có hình dạng giống nhau:" in self.page_source:
                self.this.show.emit(self.row, 3, "Bắt đầu giải captcha 2 đối tượng...")

                self.captchaSameShape()
                if not self.checkSuccessCaptcha(): return self.checkCaptcha()
            elif "hCaptcha" in self.page_source: return "hcaptcha"
            sleep(1)
    def showCookie(self):
        self.this.show.emit(self.row, 2, self.cookieTiktok)
        self.this.this.updateRow(self.username, "cookie", self.cookieTiktok)

        # semaWrite.acquire()
        # # if os.path.exists("data.json"):
            
        # #     cf = Config()
        # #     data = cf.getDataFileJson("data.json")
        # #     data["accounts"][self.username.strip()]["cookie"] = self.cookieTiktok
        # #     cf.writeDataFileJson("data.json", data)
        # semaWrite.release()

    def checkLogin(self):
        self.this.show.emit(self.row, 3, "Kiểm tra đăng nhập...")
        self.driver.get("https://www.tiktok.com/profile")
        for i in range(15):
            if self.isLogged(): 
                self.this.show.emit(self.row, 3, "Đăng nhập thành công!")
                # self.saveDescription("Đã đăng nhập!")

                self.showCookie()
                return True
            elif self.isLogin(): 
                self.this.show.emit(self.row, 3, "Chưa đang nhập!")
                return False
            sleep(1)
    def loginSuccess(self):
        self.this.show.emit(self.row, 3, "Đăng nhập thành công!")
        # self.saveDescription("Đăng nhập thành công!")

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
                    self.this.show.emit(self.row, 3, "Hcaptcha không giải được, đăng nhập thất bại!")
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
        self.this.show.emit(self.row, 3, "Bắt đầu đăng nhập tài khoản...")

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
                self.this.show.emit(self.row, 3, status)
                # self.saveDescription(status)
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
                #     self.this.show.emit(self.row, 3, "Đăng nhập thất bại, do hcaptcha chưa hỗ trợ!")

                #     return False
                print("Đã tìm thấy captcha!")
                self.this.show.emit(self.row, 3, "Đã tìm thấy captcha!")
                if self.checkCaptcha() == "hcaptcha":
                    self.this.show.emit(self.row, 3, "Hcaptcha không giải được, đăng nhập thất bại!")
                    return False
                sleep(10)
            sleep(0.1)
        self.this.show.emit(self.row, 3, "Đăng nhập thất bại!")
        # self.saveDescription("Đăng nhập thất bại!")
        # self.this.statusTiktok.emit(self.row, 3, "Đăng nhập thất bại!")
        return False
    def uploadVideo(self, path, content, schedule=()):
        # self.addCookie()
        upload = UploadVideoTiktok(self.driver)
        self.this.show.emit(self.row, 3, "Đang upload video...")

        if upload.uploadVideo(path, content, schedule):
            self.this.show.emit(self.row, 3, "Upload thành công!")
            return True
        else:
            self.this.show.emit(self.row, 3, "Upload thất bại!")
            return False
    
        


        
# LoginTikTok("user2977286918288", "123456@a", "JGWKqGzssbNZEyxCF9NVywp8UzCVVwwNvGZA13IcK39kY0084yfJSpxZlDxzufSVVBmxdgqh6Qp77TZ3").run()
# Xác minh để tiếp tục:
# Kéo thanh trượt để ghép hình

# Rất tiếc, đã xảy ra lỗi, vui lòng thử lại sau