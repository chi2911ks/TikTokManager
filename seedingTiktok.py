import random
import traceback
from autoselenium import AutoSelenium
from time import sleep, perf_counter
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
class SeedingTiktok(AutoSelenium):
    def __init__(self, driver):
        super().__init__()
        self.setDriver(driver)
    def followUser(self, link):
        self.driver.get(link)
        sleep(random.randint(5,10))
        self.ClickJsWebElement("xpath", '//button[@data-e2e="follow-button"]')
        sleep(1)
    def commentVideo(self, nd):
        # self.driver.get(link)
        sleep(random.randint(5,10))

        # self.MoveElementClick("xpath", '//div[@data-e2e="comment-input"]', nd)
        self.driver.implicitly_wait(30)
        self.driver.find_element('xpath', '//*[@data-text="true"]').send_keys(nd)
        sleep(1)
        self.ClickJsWebElement("xpath", '//div[@data-e2e="comment-post"]')
        sleep(1)
    def commentLive(self, nd):
        # self.driver.get(link)
        sleep(random.randint(5,10))

        # self.MoveElementClick("xpath", '//div[@data-e2e="comment-input"]', nd)
        self.driver.implicitly_wait(30)
        # self.driver.find_element('xpath', '//*[@contenteditable="true"]').send_keys(nd)
        el = self.driver.find_element('xpath', '//*[@contenteditable="true"]')
        self.driver.execute_script('''arguments[0].scrollIntoView({ behavior: 'smooth' });''', el)
        el.send_keys(nd)
        sleep(1)
        self.ClickJsWebElement("xpath", '//div[@data-e2e="comment-post"]')
        sleep(1)
    def shareLive(self):
        sleep(random.randint(5,10))
        self.driver.implicitly_wait(30)

        el = self.driver.find_element("xpath", '//*[@data-e2e="share-icon"]')
        self.driver.execute_script('''var evObj = document.createEvent('MouseEvents');
evObj.initMouseEvent("mouseover", true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
arguments[0].dispatchEvent(evObj);''', el)
        self.ClickJsWebElement("xpath", '//*[@data-e2e="share-link"]', index=3)

    def viewLive(self, link, nd, delay, comment, share):
        self.driver.set_window_size(700, 500)
        self.driver.get(link)
        if share: self.shareLive()
        if nd != "" and comment: self.commentLive(nd)
        sleep(delay)
    
    def likeVideo(self, delay):
        # self.driver.get(link)
        sleep(delay)
        self.ClickJsWebElement("xpath", '//*[@data-e2e="like-icon"]')
        sleep(1)
    def saveVideo(self):
        # self.driver.get(link)
        sleep(random.randint(5,10))
        self.ClickJsWebElement("xpath", '//*[@data-e2e="undefined-icon"]')
        sleep(1)
    def shareVideo(self):
        # self.driver.get(link)
        sleep(random.randint(5,10))
        # self.ClickJsWebElement("xpath", '//*[@data-e2e="share-icon"]')
        el = self.driver.find_element("xpath", '//*[@data-e2e="share-icon"]')
        self.driver.execute_script('''var evObj = document.createEvent('MouseEvents');
evObj.initMouseEvent("mouseover", true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
arguments[0].dispatchEvent(evObj);''', el)
        self.ClickJsWebElement("id", 'icon-element-copy')
        
        sleep(1)
    def story(self, timeout, like=False, save=False):
        print(timeout*60)
        def likeRandom():
            return random.choice([True, False])
        def saveRandom():
            return random.choice([True, False])
        self.driver.get("https://www.tiktok.com/")
        if "https://www.tiktok.com/explore" in self.driver.current_url: self.driver.get("https://www.tiktok.com/")
        a = 0
        
        while True:
            self.driver.implicitly_wait(30)
            videos = self.driver.find_elements('xpath', '//div[contains(@class, "DivVideoWrapper")]')
            if len(videos) < 5:
                for i in videos:
                    self.driver.execute_script('''arguments[0].scrollIntoView({ behavior: 'smooth' });''', i)
                    sleep(1)
                continue

            for index, video in enumerate(videos):
                
                perf = perf_counter()
                if a >= timeout*60: return
                self.driver.execute_script('''arguments[0].scrollIntoView({ behavior: 'smooth' });''', video)
                if likeRandom() and like: 
                    sleep(random.randint(5,10))

                    print("like")
                    el = self.driver.find_elements('xpath', '//*[@data-e2e="like-icon"]')[index]
                    try:  self.driver.execute_script('''arguments[0].click();''', el)
                    except Exception as e: print(e)
                if saveRandom() and save: 
                    sleep(random.randint(5,10))

                    print("undefined")
                    el = self.driver.find_elements('xpath', '//*[@data-e2e="undefined-icon"]')[index]
                    try:  self.driver.execute_script('''arguments[0].click();''', el)
                    except Exception as e: print(e)
                sleep(random.randint(5,10))
                
                a += round(perf_counter() - perf)
            self.driver.refresh()