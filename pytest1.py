from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Funciones.Archivo_Funciones import Tests_Funciones

t=3
driver=""

def setup_function(function):
    global driver
    print("Inicia test: \n")
    ser = Service("C:/Program Files/Python312/chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=ser, options=op)

def teardown_function(function):
    print("\nFinaliza el test")

def test_Login():
    f = Tests_Funciones(driver)
    f.Navegar("https://demoqa.com/buttons", t)
    f.Mouse_doble_click("id", "doubleClickBtn", t)

def test_clickDerecho():
    f = Tests_Funciones(driver)
    f.Navegar("https://demoqa.com/buttons", t)
    f.Mouse_click_derecho("id", "rightClickBtn", t)

def test_login():
    f = Tests_Funciones(driver)
    f.Navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", t)
    f.Texto("xpath", "//input[@name='username']", "Admin", t)
    f.Texto("xpath", "//input[@type='password']", "admin123", t)
    f.Click("xpath", "//button[@type='submit']", t)



