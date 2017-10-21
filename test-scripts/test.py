import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#trying to test the most baisc use case
#installed ChromeDriver via Homebew, which is why there is no directory in arguments

chrome_extension = webdriver.ChromeOptions()
chrome_extension.add_extension('TabStache.crx')
driver = webdriver.Chrome(chrome_options = chrome_extension)


driver.get('http://google.com')
time.sleep(5)
driver.execute_script("window.open('chrome-extension://bnfnaeocjbjbbfmhjdblnmbaeimbigid/html/popup.html');")
time.sleep(5) 
driver.quit()