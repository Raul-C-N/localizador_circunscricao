# Generated by Selenium IDE
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

class TestTeste3():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_teste3(self):
    # Test name: teste3
    # Step # | name | target | value | comment
    # 1 | open | /maps/d/viewer?mid=1Cn5198YTPrwcJEoVW4B1RIkr1Sc&shorturl=1&ll=-23.6585768689163%2C-46.65878045507815&z=11 |  | 
    self.driver.get("https://www.google.com/maps/d/viewer?mid=1Cn5198YTPrwcJEoVW4B1RIkr1Sc&shorturl=1&ll=-23.6585768689163%2C-46.65878045507815&z=11")
    # 2 | setWindowSize | 1936x1056 |  | 
    self.driver.set_window_size(1936, 1056)
    # 3 | click | css=.mU4ghb-G0jgYd-LgbsSe-Bz112c |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".mU4ghb-G0jgYd-LgbsSe-Bz112c").click()
    # 4 | click | css=.whsOnd |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".whsOnd").click()
    # 5 | runScript | window.scrollTo(0,0) |  | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 6 | type | css=.whsOnd | alameda gabriel monteiro da silva, 1000 | 
    self.driver.find_element(By.CSS_SELECTOR, ".whsOnd").send_keys("alameda gabriel monteiro da silva, 1000")
    # 7 | sendKeys | css=.whsOnd | ${KEY_ENTER} | 
    self.driver.find_element(By.CSS_SELECTOR, ".whsOnd").send_keys(Keys.ENTER)
    # 8 | click | css=.nJjxad-bEDTcc-LgbsSe |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".nJjxad-bEDTcc-LgbsSe").click()
    # 9 | runScript | window.scrollTo(0,0) |  | 
    self.driver.execute_script("window.scrollTo(0,0)")
    # 10 | click | css=.nJjxad-bEDTcc-LgbsSe |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".nJjxad-bEDTcc-LgbsSe").click()
    # 11 | click | css=.nJjxad-bEDTcc-LgbsSe |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".nJjxad-bEDTcc-LgbsSe").click()
    # 12 | click | css=.nJjxad-bEDTcc-LgbsSe |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".nJjxad-bEDTcc-LgbsSe").click()
    # 13 | click | css=.nJjxad-bEDTcc-LgbsSe |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".nJjxad-bEDTcc-LgbsSe").click()
    # 14 | click | css=.nJjxad-bEDTcc-LgbsSe |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".nJjxad-bEDTcc-LgbsSe").click()
    # 15 | click | css=.nJjxad-bEDTcc-LgbsSe |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".nJjxad-bEDTcc-LgbsSe").click()
    # 16 | click | css=.nJjxad-bEDTcc-LgbsSe |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".nJjxad-bEDTcc-LgbsSe").click()
    # 17 | click | css=.nJjxad-bEDTcc-LgbsSe |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".nJjxad-bEDTcc-LgbsSe").click()
    # 18 | click | css=.gm-style > div:nth-child(2) > div:nth-child(2) |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".gm-style > div:nth-child(2) > div:nth-child(2)").click()
    # 19 | click | css=.qqvbed-tJHJj |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".qqvbed-tJHJj").click()
  
