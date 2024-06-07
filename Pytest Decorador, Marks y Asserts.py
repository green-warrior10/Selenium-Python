import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Funciones.Archivo_Funciones import Tests_Funciones

t = 1

@pytest.fixture(scope="module") #Decorador
def setup_Login1():
    global driver, f
    print("Inicia test: \n")
    ser = Service("C:/Program Files/Python312/chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    f = Tests_Funciones(driver)
    f.Navegar("https://practicetestautomation.com/practice-test-login/", t)
    f.Texto("xpath", "//input[@id='username']", "student", t)
    f.Texto("xpath", "//input[@id='password']", "Password123", t)
    f.Click("xpath", "//button[@id='submit']", t)
    yield
    print("########### Test finalizado #############")

@pytest.fixture(scope="module") # Decorador
def setup_Login2():
    global driver, f
    print("\nInicia test: \n")
    ser = Service("C:/Program Files/Python312/chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)
    f = Tests_Funciones(driver)
    f.Navegar("https://practice.expandtesting.com/login", t)
    f.Texto("xpath", "//input[@id='username']", "practice", t)
    f.Texto("xpath", "//input[contains(@id,'password')]", "SuperSecretPassword!", t)
    f.Click("xpath", "//button[contains(@class,'btn btn-bg btn-primary d-block w-100')]", t)
    yield
    print("\n########### Test finalizado #############")

@pytest.mark.LoginA #Mark
@pytest.mark.usefixtures("setup_Login1") #Llamando al decorador
def test_Login1(): 
    validar = f.Selector_Xpath("//strong[contains(.,'Congratulations student. You successfully logged in!')]").text
    assert validar=="Congratulations student. You successfully logged in!", "No hiciste login"  #Assert que valida si el test es correcto o no
    driver.close()

@pytest.mark.LoginB  #Mark
@pytest.mark.usefixtures("setup_Login2") #Llamando al decorador
def test_Login2():
    validar = f.Selector_Xpath("//h1[contains(.,'Secure Area')]").text
    assert validar == "Secure Area", "No hiciste login"   #Assert que valida si el test es correcto o no
    driver.close()
