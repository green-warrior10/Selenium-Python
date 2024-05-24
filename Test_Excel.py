import unittest
import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Funciones.Archivo_Funciones import Tests_Funciones
from Funciones.Functions_Excel import *

t = .3
class MyTestCase(unittest.TestCase):

    def setUp(self):
        ser = Service("C:/Program Files/Python312/chromedriver.exe")
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)

    def test_excel(self):
        f = Tests_Funciones
        f_excel = Funcion_Excel
        f.Navegar(self, "https://demoqa.com/text-box", t)
        path = "C:/Users/mirad/Documentos/Cursos/test1.xlsx"
        filas = f_excel.getRowCount(self, path, "Hoja1")

        for i in range(2, filas+1):
            nombre = f_excel.readData(self, path, "Hoja1", i, 1)
            email = f_excel.readData(self, path, "Hoja1", i, 2)
            direccion1 = f_excel.readData(self, path, "Hoja1", i, 3)
            direccion2 = f_excel.readData(self, path, "Hoja1", i, 4)

            f.Texto(self, "id", "userName", nombre, t)
            f.Texto(self, "id", "userEmail", email, t)
            f.Texto(self, "id", "currentAddress", direccion1, t)
            f.Texto(self, "id", "permanentAddress", direccion2, t)
            f.Click(self, "id", "submit", t)

            validar = f.Validacion(self, "id", "name", t)
            if (validar == "True"):
                print("Elemento insertado correctamente")
                f_excel.writeData(self, path, "Hoja1", i, 5, "Insertado")
            else:
                print("Elemento no insertado")
                f_excel.writeData(self, path, "Hoja1", i, 5, "Error")


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()
