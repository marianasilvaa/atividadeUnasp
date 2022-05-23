from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://google.com')
driver.find_element_by_name("q").send_keys("UNASP")
driver.find_element_by_name("btnK").submit()
driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a").click()
driver.find_element_by_xpath(" /html/body/div[1]/div/a[2]").click()

time.sleep(5)

XPATH_VerCursos = '//*[@id="slider-135-slide-284-layer-28"]'
driver.find_element_by_xpath(XPATH_VerCursos).click()

time.sleep(5)

XPATH_ListaCursos = '//*[@id="listaDeCursosAncora"]/div/div/div[2]/a[1]'
driver.find_element_by_xpath(XPATH_ListaCursos).click()

time.sleep(5)

XPTAH_Inscrever = '/html/body/div[3]/div[2]/div[2]/div/div[2]/div/div/a[1]'
driver.find_element_by_xpath(XPTAH_Inscrever).click()

time.sleep(200)