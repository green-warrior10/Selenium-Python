import time
import unittest
from selenium.common import TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class Tests_Funciones:
    def __init__(self, driver):
        self.driver = driver

    def Tiempo(self, tiempo):
        t = time.sleep(tiempo)
        return t

    def Navegar(self, url, tiempo):
        self.driver.get(url)
        self.driver.maximize_window()
        t = time.sleep(tiempo)
        return t

    def Navegacion_Atras(self, tiempo):
        self.driver.back()
        t = time.sleep(tiempo)
        return t

    def Navegacion_Adelante(self, tiempo):
        self.driver.forward()
        t = time.sleep(tiempo)
        return t

    def Texto_Xpath(self, xpath, texto, tiempo):
        try:
            driver = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            self.driver.execute_script("arguments[0].scrollIntoView();", driver)
            driver = self.driver.find_element(By.XPATH, xpath)
            driver.send_keys(texto)
            print("Se esta mandando al campo {} el texto -> {}".format(xpath, texto))
            t = time.sleep(tiempo)
            return xpath, texto, t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: " + xpath)

    def Texto_Id(self, id, texto, tiempo):
        try:
            driver = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            self.driver.execute_script("arguments[0].scrollIntoView();", driver)
            driver = self.driver.find_element(By.ID, id)
            driver.send_keys(texto)
            print("Se esta mandando al campo {} el texto -> {}".format(id, texto))
            t = time.sleep(tiempo)
            return id, texto, t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: " + id)

    def Click_Xpath(self, xpath, tiempo):
        try:
            driver = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            self.driver.execute_script("arguments[0].scrollIntoView();", driver)
            driver = self.driver.find_element(By.XPATH, xpath)
            driver.click()
            print("Se esta dando click a -> {}".format(xpath))
            t = time.sleep(tiempo)
            return xpath, t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: " + xpath)

    def Click_Id(self, id, tiempo):
        try:
            driver = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            self.driver.execute_script("arguments[0].scrollIntoView();", driver)
            driver = self.driver.find_element(By.ID, id)
            driver.click()
            print("Se esta dando click a -> {}".format(id))
            t = time.sleep(tiempo)
            return id, t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: " + id)

    def Select_Xpath_Type(self, xpath, tipo, dato, tiempo):
        try:
            driver = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            self.driver.execute_script("arguments[0].scrollIntoView();", driver)
            driver = self.driver.find_element(By.XPATH, xpath)
            driver = Select(driver)
            if (tipo == "text"):
                driver.select_by_visible_text(dato)
            elif (tipo == "index"):
                driver.select_by_index(dato)
            elif (tipo == "value"):
                driver.select_by_value(dato)
            print("El campo seleccionado es -> {}".format(dato))
            t = time.sleep(tiempo)
            return xpath, tipo, dato, t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: " + xpath)

    def Select_Id_Type(self, id, tipo, dato, tiempo):
        try:
            driver = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            self.driver.execute_script("arguments[0].scrollIntoView();", driver)
            driver = self.driver.find_element(By.ID, id)
            driver = Select(driver)
            if (tipo == "text"):
                driver.select_by_visible_text(dato)
            elif (tipo == "index"):
                driver.select_by_index(dato)
            elif (tipo == "value"):
                driver.select_by_value(dato)
            print("El campo seleccionado es -> {}".format(dato))
            t = time.sleep(tiempo)
            return id, tipo, dato, t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: " + id)

    def Upload_Xpath(self, xpath, archivo, tiempo):
        try:
            driver = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            self.driver.execute_script("arguments[0].scrollIntoView();", driver)
            driver = self.driver.find_element(By.XPATH, xpath)
            driver.send_keys(archivo)
            print("Se esta mandando el archivo -> {}".format(archivo))
            t = time.sleep(tiempo)
            return xpath, archivo, t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: " + xpath)

    def Upload_Id(self, id, archivo, tiempo):
        try:
            driver = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            self.driver.execute_script("arguments[0].scrollIntoView();", driver)
            driver = self.driver.find_element(By.ID, id)
            driver.send_keys(archivo)
            print("Se esta mandando el archivo -> {}".format(archivo))
            t = time.sleep(tiempo)
            return id, archivo, t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: " + id)

    def Checkbox_Xpath(self, xpath, tiempo):
        try:
            driver = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            self.driver.execute_script("arguments[0].scrollIntoView();", driver)
            driver = self.driver.find_element(By.XPATH, xpath)
            driver.click()
            print("Se esta haciendo click en el elemento -> {}".format(xpath))
            t = time.sleep(tiempo)
            return xpath, t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: " + xpath)
