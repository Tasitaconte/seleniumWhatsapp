from pprint import pprint
from subprocess import TimeoutExpired
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pprint import pprint
import time

# rutas para mensajes y url
PATH = "C:/Users/thoma/OneDrive/Escritorio/SeleniumPythonTwitterClaseFESC/chromedriver.exe"
rutaMsm = '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
URL = "https://web.whatsapp.com/"

new = '//*[@id="pane-side"]/div[1]/div/div/div[1]'
# Ruta para mensajes whatsapp
rutaMsmdos = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
usuario = '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/span'

driver = webdriver.Chrome(PATH)


def seleccionChat(nombre: str):
    print("Buscando el chat wait moment")
    chatElemnt = driver.find_elements(By.TAG_NAME, "span")
    for chat in chatElemnt:
        if chat.text == nombre:
            print("te encontre esponja")
            chat.click()
            return True
    return False


def seleccionBusqueda(nombre: str):
    buscarChat = driver.find_element(By.XPATH, rutaMsm)
    buscarChat.send_keys(nombre)
    buscarChat.send_keys(Keys.ENTER)
    return True


def enviarMensaje(mensaje: str):
    boxChat = driver.find_element(By.XPATH, rutaMsmdos)
    boxChat.send_keys(mensaje)
    boxChat.send_keys(Keys.ENTER)


def main():

    driver.get(URL)

    time.sleep(15)

    while (True):
        print("digite dato a registrar: ")
        registrar = input()

        print("mensaje a enviar")
        mensaje = input()

        if (seleccionBusqueda(registrar)):
            enviarMensaje(mensaje)
            print("encontrado")
        else:
            print("contacto no encontrado")

        print("Quiere salir? Y / sino pulse cualquier tecla")
        opcion = input()
        if (opcion == 'y' or opcion == 'Y'):
            return False

    driver.close()


main()
