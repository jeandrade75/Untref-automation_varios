import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Test_Google(unittest.TestCase):

    def test_hola(self):
        try:
            driver = webdriver.Firefox() #En esta línea creamos un driver que utiliza el webdriver de Firefox.
            driver.maximize_window()
            driver.implicitly_wait(5)
            driver.get('https://www.google.com/')
            driver.find_element(By.ID,'APjFqb').send_keys('Hola'+Keys.ENTER) #le decimos al driver que busque un elemento por el id “APjFgb”, que escriba el texto ‘Hola’ y presione enter.
            title= driver.find_element(By.CLASS_NAME,'VuuXrf').text
            self.assertEqual(title, '¡HOLA!') # --> Importante: si colcoamos ¡Chau! va a fallar la prueba y sino usamos el try/finally NO VA A CERRAR el browser y va traer problemas para las otras ejeccuciones
        
        finally:
            driver.close()
            driver.quit()