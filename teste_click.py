from selenium import webdriver
from selenium.webdriver import ActionChains
PATH = 'C:\\chromedriver_win32\\chromedriver.exe'

driver = webdriver.Chrome(PATH)


actionChains = ActionChains(driver)
button_xpath  = '//xapth...' 
button = driver.find_element_by_xpath(button_xpath)
actionChains.move_to_element(button).click().perform()