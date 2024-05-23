from selenium import webdriver
from selenium.webdriver.firefox.service import Service

ser = Service("C:/Program Files/Python312/geckodriver.exe")
op = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=op)
