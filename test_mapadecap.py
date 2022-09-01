# Generated by Selenium IDE
from lib2to3.pgen2 import driver
from webbrowser import Chrome
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# biblioteca para clique em coordenadas
from selenium.webdriver.common.action_chains import ActionChains
#from selenium import webdriver

PATH = 'C:\\chromedriver_win32\\chromedriver.exe'

def click_at(self,locator,coordString):
    """
    Clicks on a link, button, checkbox or radio button. If the click action
    causes a new page to load (like a link usually does), call
    waitForPageToLoad.

    'locator' is an element locator
    'coordString' is specifies the x,y position (i.e. - 10,20) of the mouse      event relative to the element returned by the locator.
    """
    self.do_command("clickAt", [locator,coordString,])


class TestMapadecap():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(PATH)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_mapadecap(self,endereco):
    atraso = 1
    # Test name: mapa_decap
    # Step # | name | target | value | comment
    # 1 | open | https://www.google.com/maps/d/viewer?mid=1Cn5198YTPrwcJEoVW4B1RIkr1Sc&shorturl=1&ll=-23.6585768689163%2C-46.65878045507815&z=11 |  | 
    self.driver.get("https://www.google.com/maps/d/viewer?mid=1Cn5198YTPrwcJEoVW4B1RIkr1Sc&shorturl=1&ll=-23.6585768689163%2C-46.65878045507815&z=11")
    time.sleep(atraso)
    # 2 | setWindowSize | 1936x1056 |  | 
    self.driver.set_window_size(1936, 1056)
    
    # ZOOM
    for vezes in range(6):
      self.driver.find_element(By.CSS_SELECTOR, ".nJjxad-bEDTcc-LgbsSe").click()
    ##ZOOM
    
    # 3 | click | css=.mU4ghb-G0jgYd-LgbsSe-Bz112c |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".mU4ghb-G0jgYd-LgbsSe-Bz112c").click()
    time.sleep(atraso)
    # 4 | click | css=.whsOnd |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".whsOnd").click()
    time.sleep(atraso)
    # 5 | type | css=.whsOnd | rua santo amaro, 468 | 
    self.driver.find_element(By.CSS_SELECTOR, ".whsOnd").send_keys(endereco)
    time.sleep(atraso)
    # 6 | sendKeys | css=.whsOnd | ${KEY_ENTER} | 
    self.driver.find_element(By.CSS_SELECTOR, ".whsOnd").send_keys(Keys.ENTER)
    time.sleep(atraso)
    
    #7 #click de área 
    actionChains = ActionChains(driver)
    button_xpath  = "//*[@id='map-canvas']/div[1]/div/div[2]/div[2]/div/div[3]/div" 
    button = driver.find_element_by_xpath(button_xpath)
    actionChains.move_to_element(button).move_by_offset(5,0).click().perform()
    #click de área
    


endereco = 'rua santo amaro, 468'
bot = TestMapadecap()
bot.setup_method(1)
bot.test_mapadecap(endereco)



#bot.teardown_method(1)
#bot.test_mapadecap('Av Gabriel Monteiro da Silva, 1000')

driver = webdriver.Chrome(PATH)

atraso=.5
driver.get("https://www.google.com/maps/d/viewer?mid=1Cn5198YTPrwcJEoVW4B1RIkr1Sc&shorturl=1&ll=-23.6585768689163%2C-46.65878045507815&z=11")
driver.set_window_size(1936, 1056)
time.sleep(1)
# ZOOM
for vezes in range(6):
  driver.find_element(By.CSS_SELECTOR, ".nJjxad-bEDTcc-LgbsSe").click()
##ZOOM
time.sleep(atraso)
driver.find_element(By.CSS_SELECTOR, ".mU4ghb-G0jgYd-LgbsSe").click()
time.sleep(atraso)
driver.find_element(By.CSS_SELECTOR, ".whsOnd").click()
time.sleep(atraso)
#driver.execute_script("window.scrollTo(0,0)")
#time.sleep(atraso)
driver.find_element(By.CSS_SELECTOR, ".whsOnd").send_keys("R. Dep. Lacerda Franco, 372")
time.sleep(atraso)
driver.find_element(By.CSS_SELECTOR, ".whsOnd").send_keys(Keys.ENTER)
time.sleep(atraso)


#click de área 
actionChains = ActionChains(driver)
button_xpath  = "//*[@id='map-canvas']/div[1]/div/div[2]/div[2]/div/div[3]/div" 
button = driver.find_element_by_xpath(button_xpath)
actionChains.move_to_element(button).move_by_offset(5,0).click().perform()
#click de área

driver.find_element(By.CSS_SELECTOR, ".gm-style > div:nth-child(2) > div:nth-child(2)").click()
# 9 | pega o nome do distrito responsável e salva na variável 'distrito'
time.sleep(atraso)
distrito = driver.find_element_by_class_name("qqvbed-tJHJj-fmcmS").text
print(distrito)
driver.close()
