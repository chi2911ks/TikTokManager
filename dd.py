from webdriver_manager.chrome import ChromeDriverManager

driver = ChromeDriverManager("127").install()
print(driver)