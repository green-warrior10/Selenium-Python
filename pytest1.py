import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Funciones.Archivo_Funciones import Tests_Funciones

t = 1

@pytest.fixture(scope="module")
def setup_Login1():
    global driver, f
    print("Inicia test: \n")
    ser = Service("C:/Program Files/Python312/chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    f = Tests_Funciones(driver)
    f.Navegar("https://practicetestautomation.com/practice-test-login/", t)
    yield
    print("########### Test finalizado #############")

@pytest.fixture(scope="module")
def setup_Login2():
    global driver, f
    print("Inicia test: \n")
    ser = Service("C:/Program Files/Python312/chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    f = Tests_Funciones(driver)
    f.Navegar("https://practice.expandtesting.com/login", t)
    yield
    print("########### Test finalizado #############")


def test_Login1(setup_Login1):
    f = Tests_Funciones(driver)
    f.Texto("xpath", "//input[@id='username']", "student", t)
    f.Texto("xpath", "//input[@id='password']", "Password123", t)
    f.Click("xpath", "//button[@id='submit']", t)

@pytest.mark.usefixtures("setup_Login2")
def test_Login2():
    f = Tests_Funciones(driver)
    f.Texto("xpath", "//input[@id='username']", "practice", t)
    f.Texto("xpath", "//input[contains(@id,'password')]", "SuperSecretPassword!", t)
    f.Click("xpath", "//button[contains(@class,'btn btn-bg btn-primary d-block w-100')]", t)


