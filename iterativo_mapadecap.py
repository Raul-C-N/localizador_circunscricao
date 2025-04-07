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

endereco = str(input("digite o endereço desejado \n digite 'sair' para encerrar "))

while endereco != 'sair':  
  
  PATH = 'C:\\chromedriver-win64\\chromedriver.exe'
  driver = webdriver.Chrome(PATH)


  atraso=1
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
  driver.find_element(By.CSS_SELECTOR, ".whsOnd").send_keys(endereco)
  time.sleep(atraso)
  driver.find_element(By.CSS_SELECTOR, ".whsOnd").send_keys(Keys.ENTER)
  time.sleep(atraso)


  #click de área 
  actionChains = ActionChains(driver)
  button_xpath  = "//*[@id='map-canvas']" #xpath atualizado em 24/05/2024
  button = driver.find_element_by_xpath(button_xpath)
  actionChains.move_to_element(button).move_by_offset(5,0).click().perform()
  
  #click de área

  #driver.find_element(By.CSS_SELECTOR, ".gm-style > div:nth-child(2) > div:nth-child(2)").click()
  # 9 | pega o nome do distrito responsável e salva na variável 'distrito'
  time.sleep(atraso)
  #metodo deprecado // distrito = driver.find_element_by_class_name("qqvbed-tJHJj-fmcmS").
  distrito = driver.find_element(By.CLASS_NAME, "qqvbed-tJHJj-fmcmS").text #novo metodo
  #print(distrito)

  # verificando a seccional  
  Sec_1= [1,2,3,4,5,6,8,12,77,78]
  Sec_2= [16,17,26,27,35,36,83,95,96,97]
  Sec_3= [7,14,15,23,33,34,37,46,51,75,87,89,91,93]
  Sec_4= [9,13,19,20,28,38,39,40,45,72,73,74,90]
  Sec_5= [10,18,21,29,30,31,42,52,56,57,58,81]
  Sec_6= [11,25,43,47,48,80,85,92,98,99,100,101,102]
  Sec_7= [22,24,32,50,59,62,63,64,65,67,68,103]
  Sec_8= [41,44,49,53,54,55,66,69,70]
  tit_Sec_1='Ana Paula Medeiros Monteiro de Barros'
  tit_Sec_2='Danilo Morais Correia'
  tit_Sec_3='Fabio Guedes Rosa'
  tit_Sec_4='Rodrigo Gonçalves da Silva'
  tit_Sec_5='Juliana Souto Cruz'
  tit_Sec_6='Renata Rivero da Silva Leite'
  tit_Sec_7='Daniel Juns dos Santos'
  tit_Sec_8='Guilherme Leonel Santos'
  
  #normatiza o número do distrito para teste posterior
  teste = distrito
  try:
    teste_temp = int(teste.replace('º DP',''))
  except:
    try: 
      teste_temp = int(teste.replace('ºDP',''))
    except:
      print ('erro no módulo de normatização dos DPs')
  #/normatiza o número do distrito para teste posterior
  

  if teste_temp in Sec_1:
    seccional = '1ª Delegacia Seccional de Polícia - Centro'
    titular = tit_Sec_1
    tit_gen = 'f'
  if teste_temp in Sec_2:
    seccional = '2ª Delegacia Seccional de Polícia - Sul'
    titular = tit_Sec_2
    tit_gen = 'm'
  if teste_temp in Sec_3:
    seccional = '3ª Delegacia Seccional de Polícia – Oeste'
    titular = tit_Sec_3
    tit_gen = 'm'
  if teste_temp in Sec_4:
    seccional = '4ª Delegacia Seccional de Polícia - Norte'
    titular = tit_Sec_4
    tit_gen = 'm'
  if teste_temp in Sec_5:
    seccional = '5ª Delegacia Seccional de Polícia - Leste'
    titular = tit_Sec_5
    tit_gen = 'f'
  if teste_temp in Sec_6:
    seccional = '6ª Delegacia Seccional de Polícia – Santo Amaro'
    titular = tit_Sec_6
    tit_gen = 'm'
  if teste_temp in Sec_7:
    seccional = '7ª Delegacia Seccional de Polícia - Itaquera'
    titular = tit_Sec_7
    tit_gen = 'm'
  if teste_temp in Sec_8:
    seccional = '8ª Delegacia Seccional de Polícia – São Mateus'
    titular = tit_Sec_8
    tit_gen = 'm'
  
  texto = ''  
  texto_f =" Excelentíssima Senhora Doutora \n "+titular+" \n DD. Delegada de Polícia do \n Centro de Inteligência Policial – CIP \n "+seccional+" \n Encaminho a V. Exª. denúncia oriunda da Ouvidoria Nacional de Direitos Humanos, para conhecimento e providências pertinentes, servindo-se informar diretamente ao Órgão interessado, com brevidade. \n \n Atenciosamente,"
  texto_m = " Excelentíssimo Senhor Doutor \n "+titular+" \n DD. Delegado de Polícia do \n Centro de Inteligência Policial – CIP \n "+seccional+" \n Encaminho a V. Exª. denúncia oriunda da Ouvidoria Nacional de Direitos Humanos, para conhecimento e providências pertinentes, servindo-se informar diretamente ao Órgão interessado, com brevidade. \n \n Atenciosamente,"
  
  if tit_gen == 'm':
    texto = texto_m
  if tit_gen == 'f':
    texto = texto_f
    
  print(distrito+' da '+seccional)
  print (texto)
  # verificando a seccional
  
  time.sleep(15)
  driver.close()
      
  endereco = input("digite o endereço desejado \n digite 'sair' para encerrar ")  
  
  

