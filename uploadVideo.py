import traceback
from utils.autoselenium import AutoSelenium
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# //*[@data-text="true"]
# //div[@class="tiktok-timepicker-option-item"]//span[@class="tiktok-timepicker-option-text tiktok-timepicker-left"]

# 

# //span[contains(@class, 'arrow')] #tháng
class UploadVideoTiktok(AutoSelenium):
    def __init__(self, driver):
        super().__init__()
        self.setDriver(driver)
    def __checkVideoUpload(self):
        while True:
            sleep(0.25)
            try:
                if self.driver.find_element('xpath', '//*[text()="Chỉnh sửa video" or text()="Edit video" or text()="Change video"]').is_displayed():
                    return True
            except: continue
    def __upload(self):
        chk = ["Your video has been uploaded", "Video đã được lên lịch!", "Việc bạn rời trang không gây gián đoạn cho quá trình đăng video"] 
        for i in range(10): 
            self.ClickJsWebElement('xpath', '//*[text()="Đăng" or text()="Lịch biểu" or text()="Post"]')
            sleep(0.5)
            if "Đã thử tải lên quá nhiều lần. Vui lòng thử lại sau." in self.driver.page_source:
                return False
            elif chk[0] in self.driver.page_source or chk[1] in self.driver.page_source or chk[2] in self.driver.page_source: 
                return True
        return False
    def __checkUploadSuccess(self):
        while True:
            
            sleep(0.25)
            self.driver.implicitly_wait(0.1)
            try:
                # self.driver.find_element('xpath', '//*[text()="Tách thành nhiều phần để tăng khả năng hiển thị"]')
                self.driver.find_element('xpath', '//*[text()="Để sau"]').click()
            except: pass
            try:
                self.driver.find_elements('xpath', '//*[text()="Tải video khác lên" or text()="Video của bạn đã được tải lên" or text()="Your video has been uploaded"]')[-1].click()
                self.driver.find_elements('xpath', '//*[text()="Tải lên" or text()="Upload"]')[-1].click()
                sleep(5)
                return True
            except: continue
            # Tiếp tục đăng video dài hơn 10 phút?
    def scheduleUpload(self, args):
        self.driver.implicitly_wait(30)
        day, hour, minute = args
        self.driver.find_element('xpath', '//input[@id="tux-3" and @type="checkbox"]').click()
        try:
            self.driver.implicitly_wait(1)
            self.driver.find_element('xpath', '//*[text()="Cho phép" or text()="Allow"]').click()
        except: pass
        self.driver.implicitly_wait(30)
        sleep(1)
        self.driver.find_element('xpath', '//div[contains(@class, "time-picker-input picker-input")]').click()

        # minuteValid = ["00", "05", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55"]
        # hourValid = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
        if len(str(hour)) == 1: hour = "0"+str(hour)
        if len(str(minute)) == 1: minute = "0"+str(minute)
        print(hour, minute)
        el = self.driver.find_element('xpath', '//*[text()="%s" and contains(@class, "left")]'%hour)
        self.driver.execute_script('''arguments[0].scrollIntoView({ behavior: 'smooth' });''', el)
        self.driver.execute_script('''arguments[0].click();''', el)

        el = self.driver.find_element('xpath', '//*[text()="%s" and contains(@class, "right")]'%minute)
        self.driver.execute_script('''arguments[0].scrollIntoView({ behavior: 'smooth' });''', el)
        self.driver.execute_script('''arguments[0].click();''', el)
        sleep(1)
        self.driver.find_element('xpath', '//div[contains(@class, "date-picker-input picker-input")]').click()
        sleep(1)
        self.driver.find_elements('xpath', '//div[contains(@class, "day-span-container")]//span[text()="%s"]'%day)[-1].click()
        sleep(1)
        if 'Lên lịch trước ít nhất 15 phút' in self.driver.page_source: return False
        # sleep(100)
        return True
    def tagUsername(self, username):
        while True:
            try:
                self.driver.implicitly_wait(0.1)
                self.driver.find_element('xpath', '//*[text()="Để sau"]').click()
            except: pass
            try:
                self.driver.implicitly_wait(30)
                self.driver.find_element('xpath', '//button[contains(@aria-label, "@")]').click()
                break
            except: continue
        
        # self.driver.find_element('xpath', '//input[contains(@class, "search-friends")]').send_keys(username.replace("@", ""))
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(('xpath', '//input[contains(@class, "search-friends")]'))).send_keys(username.replace("@", ""))

        # sleep(5)
        # inp.send_keys(Keys.ENTER)
        try:
            self.driver.implicitly_wait(5)
            self.driver.find_element('xpath', '//*[text()="%s"]'%username).click()
        except: 
            self.driver.find_element('xpath', '//input[contains(@class, "search-friends")]').send_keys(Keys.ENTER)
        # sleep(1)
    def hashTag(self, tag):
        while True:
            try:
                self.driver.implicitly_wait(0.1)
                self.driver.find_element('xpath', '//*[text()="Để sau"]').click()
            except: pass
            try:
                self.driver.implicitly_wait(30)
                self.driver.find_element('xpath', '//button[@aria-label="Hashtag"]').click()
                break
            except: continue
        # self.driver.find_element('xpath', '//*[@data-text="true"]').send_keys(tag.replace("#", ""))
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(('xpath', '//*[@data-text="true"]'))).send_keys(tag.replace("#", ""))
        try:
            self.driver.implicitly_wait(5)
            self.driver.find_element('xpath', '//*[@role="listbox"]')
            sleep(1)
        except: pass
        self.driver.find_element('xpath', '//*[@data-text="true"]').send_keys(Keys.ENTER)

        # sleep(1)
    def content(self, nd):
        sleep(1)
        # while True:
        #     try:
        #         self.driver.implicitly_wait(0.1)
        #         self.driver.find_element('xpath', '//*[text()="Để sau"]').click()
        #     except: pass
        #     try:
        #         # print(self.driver.find_element('xpath', '//*[@data-contents="true"]').text)
                
        #         self.driver.find_element('xpath', '//div[@aria-autocomplete="list"]').send_keys(Keys.CONTROL+"a")
        #         self.driver.find_element('xpath', '//div[@aria-autocomplete="list"]').send_keys(Keys.DELETE)
        #         if self.driver.find_element('xpath', '//*[@data-contents="true"]').text == "": break
                
        #     except: pass
        # ActionChains(self.driver).click(self.driver.find_element('xpath', '//*[@data-contents="true"]')).send_keys(Keys.DELETE).perform()
       
        sleep(3)
        for n in nd.split(" "):
            try:
                self.driver.implicitly_wait(0.1)
                self.driver.find_element('xpath', '//*[text()="Để sau"]').click()
            except: pass
            if "#" in n:
                self.hashTag(n)
            elif "@" in n:
                self.tagUsername(n)
            else: 
                WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(('xpath', '//*[@data-text="true"]'))).send_keys(n+" ")
                
    def uploadVideo(self, pathVideo, content, schedule):
        try:
            self.driver.get("https://www.tiktok.com/creator-center/upload")
            self.driver.implicitly_wait(30)
            # self.driver.switch_to.frame(self.driver.find_element('xpath', '//iframe[@data-tt="Upload_index_iframe"]'))
            # self.driver.implicitly_wait(30)
            self.driver.find_element('xpath', '//input[@accept="video/*"]').send_keys(pathVideo)
            print(self.__checkVideoUpload())
            if content != "":
                self.content(content)
                sleep(1)
            print(schedule)
            if schedule:
                if not self.scheduleUpload(schedule):return False
            sleep(1)
            if self.__upload():
                return self.__checkUploadSuccess()
            else: return False
        except:
            with open("error.txt", "a+", encoding="utf-8") as file:
                file.write(traceback.format_exc()+"\n")
            return False
# UploadVideoTiktok(None).content("ngon vl @chi2911ks #xuhuong #dexuat #gai #sexy")