from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait # --> Hace que nuestro webdriver espere un tiempo
from selenium.webdriver.support import expected_conditions as EC # --> Este les pone las condiciones a algo

driver = webdriver.Firefox() #En esta línea creamos un driver que utiliza el webdriver de Firefox.
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://untref.edu.ar/')
driver.find_element(By.CLASS_NAME, 'btn-search').click() #le decimos al driver que busque un elemento por el la clase “btn-search” , que escriba el texto ‘Hola’ y presione enter.

driver.find_element(By.NAME, 'q').send_keys('Diplomatura')
driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div[1]/div/nav/ul/li/div/form/input[3]').click()

#driver.find_element(By.XPATH,'/html/body/div[1]/section/section/div[2]/div/div[1]/a').click()

#Todo esto que vemos a continuacion es un Web Element que le agregamos una condicion y un timeout
link_diplomatura = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/section/div[2]/div/div[1]/a')))
link_diplomatura.click()