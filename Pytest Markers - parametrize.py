import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Funciones.Archivo_Funciones import Tests_Funciones

t = 1

def get_Data():
    return [("User 1", "123"),
        ("User 2", "123"),
        ("User 3", "123"),
        ("User 4", "123"),
        ("User 5", "123"),
        ("student", "Password123")]

@pytest.mark.login
@pytest.mark.parametrize("user,pwd", get_Data())
def test_Login(user, pwd):
    global driver
    print("Inicia test: \n")
    ser = Service("C:/Program Files/Python312/chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    f = Tests_Funciones(driver)
    f.Navegar("https://practicetestautomation.com/practice-test-login/", t)
    f.Texto("xpath","//input[@id='username']", user, t)
    f.Texto("xpath", "//input[@id='password']", pwd, t)
    f.Click("xpath", "//button[@id='submit']", t)


def teardown_function():
    print("Fin del test")
    driver.close()
