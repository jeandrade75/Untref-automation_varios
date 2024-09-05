import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Test_Infobae(unittest.TestCase):

    def test_search2(self):
        driver = webdriver.Firefox() #En esta línea creamos un driver que utiliza el webdriver de Firefox
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get('https://www.infobae.com/')
        close_button = driver.find_element(By.ID,'onesignal-slidedown-cancel-button').click()
        close_button = driver.find_element(By.ID,'onesignal-slidedown-container').click()
        title= driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div[1]/div[1]/div[2]/a[7]').text
        self.assertEqual(title, 'Inteligencia Artificial')
        driver.quit()

if __name__ == '__main__':
    unittest.main()



