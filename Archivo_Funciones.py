import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


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

    def Selector_Xpath(self, selector):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element = self.driver.find_element(By.XPATH, selector)
        return element

    def Selector_Id(self, selector):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
        element = self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element = self.driver.find_element(By.ID, selector)
        return element
    def Texto (self, tipo, selector, texto, tiempo):
        if (tipo == "xpath"):
            try:
                driver = self.Selector_Xpath(selector)
                driver.clear()
                driver.send_keys(texto)
                print("Se esta mandando al campo {} el texto -> {}".format( selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        if (tipo == "id"):
            try:
                driver = self.Selector_Id(selector)
                driver.clear()
                driver.send_keys(texto)
                print("Se esta mandando al campo {} el texto -> {}".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)

    def Click (self, tipo, selector, tiempo):
        if (tipo == "xpath"):
            try:
                driver = self.Selector_Xpath(selector)
                driver.click()
                print("Se esta dando click a -> {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        if (tipo == "id"):
            try:
                driver = self.Selector_Id(selector)
                driver.click()
                print("Se esta dando click a -> {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)

    def Select(self, tipo, selector, select, dato, tiempo):
        if (tipo == "xpath"):
            try:
                driver = self.Selector_Xpath(selector)
                driver = Select(driver)
                if (select == "text"):
                    driver.select_by_visible_text(dato)
                elif (select == "index"):
                    driver.select_by_index(dato)
                elif (select == "value"):
                    driver.select_by_value(dato)
                print("El campo seleccionado es -> {}".format(dato))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        if (tipo == "id"):
            try:
                driver = self.Selector_Id(selector)
                driver = Select(driver)
                if (select == "text"):
                    driver.select_by_visible_text(dato)
                elif (select == "index"):
                    driver.select_by_index(dato)
                elif (select == "value"):
                    driver.select_by_value(dato)
                print("El campo seleccionado es -> {}".format(dato))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)

    def Upload(self, tipo, selector, archivo, tiempo):
        if (tipo == "xpath"):
            try:
                driver = self.Selector_Xpath(selector)
                driver.send_keys(archivo)
                print("Se esta mandando el archivo -> {}".format(archivo))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        if (tipo == "id"):
            try:
                driver = self.Selector_Id(selector)
                driver.send_keys(archivo)
                print("Se esta mandando el archivo -> {}".format(archivo))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)

    def Checkbox_Xpath(self, tipo, selector, tiempo):
        if (tipo == "xpath"):
            try:
                driver = self.Selector_Xpath(selector)
                driver.click()
                print("Se esta haciendo click en el elemento -> {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        if (tipo == "id"):
            try:
                driver = self.Selector_Id()
                driver.click()
                print("Se esta haciendo click en el elemento -> {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)

    def Checkbox_Multiple_Xpath(self, tiempo, *args):
        try:
            for i in args:
                driver = self.Selector_Xpath(i)
                driver.click()
                print("Se esta haciendo click en el elemento -> {}".format(i))
                t = time.sleep(tiempo)
                return t
        except TimeoutException as ex:
            for i in args:
                print(ex.msg)
                print("No se encontro el elemento: " + i)

    def Validacion(self, tipo, selector, tiempo):
        if (tipo == "xpath"):
            try:
                driver = self.Selector_Xpath(selector)
                print("Se esta dando click a -> {}".format(selector))
                t = time.sleep(tiempo)
                return "True", t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        if (tipo == "id"):
            try:
                driver = self.Selector_Id(selector)
                print("Se esta dando click a -> {}".format(selector))
                t = time.sleep(tiempo)
                return "True", t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)

    def Mouse_doble_click(self, tipo, selector, tiempo):
        if (tipo == "xpath"):
            try:
                driver = self.Selector_Xpath(selector)
                print("Se esta dando doble click a -> {}".format(selector))
                mouse = ActionChains(self.driver)
                mouse.double_click(driver).perform()
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        if (tipo == "id"):
            try:
                driver = self.Selector_Id(selector)
                print("Se esta dando doble click a -> {}".format(selector))
                mouse = ActionChains(self.driver)
                mouse.double_click(driver).perform()
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)

    def Mouse_click_derecho(self, tipo, selector, tiempo):
        if (tipo == "xpath"):
            try:
                driver = self.Selector_Xpath(selector)
                print("Se esta dando clicl derecho a -> {}".format(selector))
                mouse = ActionChains(self.driver)
                mouse.context_click(driver).perform()
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        if (tipo == "id"):
            try:
                driver = self.Selector_Id(selector)
                print("Se esta dando doble click a -> {}".format(selector))
                mouse = ActionChains(self.driver)
                mouse.context_click(driver).perform()
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)

    def Mouse_drag_drop(self, tipo, selector, destino, tiempo):
        if (tipo == "xpath"):
            try:
                driver = self.Selector_Xpath(selector)
                destino = self.Selector_Xpath(destino)
                print("Se esta arrastrando el elemento {} a -> {}".format(selector, destino))
                mouse = ActionChains(self.driver)
                mouse.drag_and_drop(driver, destino).perform()
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        if (tipo == "id"):
            try:
                driver = self.Selector_Id(selector)
                destino = self.Selector_Xpath(destino)
                print("Se esta arrastrando el elemento {} a -> {}".format(selector, destino))
                mouse = ActionChains(self.driver)
                mouse.drag_and_drop(driver, destino).perform()
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)

    def Mouse_drag_drop_xy(self, tipo, selector, x, y, tiempo):
        if (tipo == "xpath"):
            try:
                # self.driver.switch_to.frame(0) en caso de tener iframes
                driver = self.Selector_Xpath(selector)
                print("Se esta arrastrando el elemento -> {}".format(selector))
                mouse = ActionChains(self.driver)
                mouse.drag_and_drop_by_offset(driver, x, y).perform()
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
        if (tipo == "id"):
            try:
                # self.driver.switch_to.frame(0) en caso de tener iframes
                driver = self.Selector_Id(selector)
                print("Se esta arrastrando el elemento -> {}".format(selector))
                mouse = ActionChains(self.driver)
                mouse.drag_and_drop_by_offset(driver, x, y).perform()
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
