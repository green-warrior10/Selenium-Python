import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Funciones.Archivo_Funciones import Tests_Funciones
from Funciones.Functions_Excel import Funcion_Excel

class MyTestCase(unittest.TestCase):

    def setUp(self):
        ser = Service("C:/Program Files/Python312/chromedriver.exe")
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
