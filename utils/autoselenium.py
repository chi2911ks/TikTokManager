# -*- coding: utf-8 -*-
import shutil
import undetected_chromedriver as wb
from selenium.webdriver import Chrome
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
import os
import psutil
from subprocess import CREATE_NO_WINDOW
import win32gui

class AutoSelenium:

    def setDriver(self, driver):
        self.driver = driver 
    
    def stop(self, profile):
        try:
            userdata = '--user-data-dir='+profile
            for process in psutil.process_iter():
                if process.name() == 'chrome.exe' and userdata in process.cmdline():
                    process.kill()
        except: pass
    def deleteProfile(self):
        while True:
            try:
                shutil.rmtree(self.driver.user_data_dir)
                return
            except Exception as e: 
                if "cannot find the path" in str(e): return
    def getDriver(self, x: str=None, y: str=None, width: str=None, height: str=None, **kwargs):
        
        proxy = kwargs.get("proxy", "")
        ext = kwargs.get("extensions", "")
        binary_location = kwargs.get("binary_location", "")
        chromedriver = kwargs.get("chromedriver", None)
        headless = kwargs.get("headless", False)
        # app = kwargs.get("app", "https://nopecha.com/setup#{NOPECHA_KEY}")
        version = kwargs.get("version", 116)

        profile = kwargs.get("profile", "")
        options = wb.ChromeOptions()
        if ext:
            # options.add_extension(ext)
            options.add_argument('--load-extension=%s'%ext)
        # options.
        # options.add_argument('--headless')
        if binary_location != "":
            options.binary_location = binary_location
        if proxy != "":
            print(proxy)
            options.add_argument('--host-resolver-rules=\"MAP * 0.0.0.0 , EXCLUDE '+proxy.split(":")[0])
        options.add_argument("--force-device-scale-factor=0.7")

        options.add_argument('--lang=vi')
        options.add_argument('--proxy-server=%s'%proxy)
        prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-infobars")
        # options.add_argument("--disable-extensions")
        # options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument('--no-first-run')
        options.add_argument('--no-service-autorun') 
        options.add_argument('--password-store-basic')
        options.add_argument('--no-service-autorun')
        # options.add_argument('--lang=en-US') 
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-cpu') 
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2, 
            "download_restrictions": 3
        }
        options.add_experimental_option("prefs", prefs) 
        # options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--enable-main-frame-before-activation")
        options.add_argument("--display-capture-permissions-policy-allowed")
        # options.add_argument("-device-scale-factor-1")
        options.add_argument("--disable-web-security") 
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-plugins-discovery")
        options.add_argument('--disable-gpu-shader-disk-cache')
        options.add_argument("--disable-blink-features-AutomationControlled")

        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-infobars')
        # options.add_argument('--disable-dev-shm-usage')
        # options.add_argument('--disable-blink-features=AutomationControlled')
        # options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
        # options.add_argument('--disable-component-update')
        # # to support multiple instances
        # options.add_argument('--disable-backgrounding-occluded-windows')
        # options.add_argument('--disable-renderer-backgrounding')

        # options.add_argument('--disable-background-timer-throttling')
        # options.add_argument('--disable-renderer-backgrounding')
        # options.add_argument('--disable-background-networking')
        # options.add_argument('--no-pings')
        # options.add_argument('--disable-breakpad')
        # options.add_argument("--no-default-browser-check")
        # options.add_argument('--homepage=about:blank')
        if width != None and height != None:
            options.add_argument('--window-size=%s,%s'%(width, height))
        if x != None and y != None:
            options.add_argument('--window-position=%s,%s'%(x, y))
        self.driver = wb.Chrome(version_main=version, headless=headless, options=options, user_data_dir=profile, use_subprocess=True, driver_executable_path=chromedriver)
        # self.hidenCmd()
    def ClickAbleElement(self, by: By, value: str, index: int=0, timeout: int=30) -> WebElement:
        if index == 0:
            el = WebDriverWait(self.driver, timeout=timeout).until(EC.element_to_be_clickable((by, value)))
        else:
            self.driver.implicitly_wait(timeout)
            el = WebDriverWait(self.driver, timeout=timeout).until(EC.element_to_be_clickable(self.driver.find_elements(by, value)[index]))
        return el
    def ClickJsSelector(self, selector: str):
        self.driver.execute_script('document.querySelector("%s").click()'%selector)
    def ClickJsWebElement(self, by: By, value: str, text: str=None, index: int=0, timeout: int=30):
        driver = self.driver
        driver.implicitly_wait(timeout)
        el = driver.find_elements(by, value)[index]
        self.driver.execute_script('arguments[0].click();', el)
        if text != None:
            # self.SendKeys(el, text)
            el.send_keys(text)
    def MoveElementClick(self, by: By, value: str, text: str=None, index: int=0, timeout: int=30):
        driver = self.driver
        driver.implicitly_wait(timeout)
        el = driver.find_elements(by, value)[index]
        # ac = ActionChains(driver)
        # ac.move_to_element(el).click(el).perform()
        try:
            el.click()
        except ElementClickInterceptedException: return self.MoveElementClick(by, value, text, index, timeout)
        if text != None:
            el.send_keys(text)
            # self.SendKeys(el, text)
    
    def SendKeys(self, element: WebElement, text: str):
        ac = ActionChains(self.driver)
        ac.send_keys_to_element(element, text).perform()
    def SetSizeWeb(self, size: float=0.5):
        self.driver.get('chrome://settings/')
        self.driver.execute_script('chrome.settingsPrivate.setDefaultZoom(%s);'%size)
    