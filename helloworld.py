from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox() #En esta línea creamos un driver que utiliza el webdriver de Firefox.
driver.implicitly_wait(5)
driver.get('http://www.google.com')
driver.find_element(By.ID,'APjFqb').send_keys('Hola'+Keys.ENTER) #le decimos al driver que busque un elemento por el id “APjFgb”, que escriba el texto ‘Hola’ y presione enter.
driver.find_element(By.LINK_TEXT, "Actualidad").click() #En esta línea le decimos al driver que busque un elemento por el texto de link “Actualidad” y luego haga click.
#driver.close()

