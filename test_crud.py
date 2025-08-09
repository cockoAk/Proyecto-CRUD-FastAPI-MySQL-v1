from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

# Abre el HTML local (ajusta la ruta si es diferente)
driver.get("file:///C:/Users/Shadow Rexton/Desktop/software/proyectos/FarmWeb/crud-fastapi/index.html")

wait = WebDriverWait(driver, 10)

# /// CREAR USUARIO ///
correo_crear = wait.until(EC.presence_of_element_located((By.ID, "crear-correo")))
contrasenia_crear = driver.find_element(By.ID, "crear-contrasenia")
boton_crear = driver.find_element(By.XPATH, "//button[contains(text(),'Crear')]")

correo_crear.send_keys("selenium_test@gmail.com")
contrasenia_crear.send_keys("Clave123!")
boton_crear.click()
time.sleep(2)

# /// ACTUALIZAR PSW //
correo_actualizar = driver.find_element(By.ID, "actualizar-correo")
nueva_contrasenia = driver.find_element(By.ID, "nueva-contrasenia")
boton_actualizar = driver.find_element(By.XPATH, "//button[contains(text(),'Actualizar')]")

correo_actualizar.send_keys("selenium_test@gmail.com")
nueva_contrasenia.send_keys("NuevaClave456!")
boton_actualizar.click()
time.sleep(2)

# === ELIMINAR PERFIL ===
correo_eliminar = driver.find_element(By.ID, "eliminar-correo")
boton_eliminar = driver.find_element(By.XPATH, "//button[contains(text(),'Eliminar')]")

correo_eliminar.send_keys("selenium_test@gmail.com")
boton_eliminar.click()
time.sleep(2)

# === MOSTRAR TODOS LOS USUARIOS ===
boton_mostrar = driver.find_element(By.XPATH, "//button[contains(text(),'Mostrar Todos')]")
boton_mostrar.click()
time.sleep(2)

# Verifica que la lista se cargó
lista = driver.find_element(By.ID, "lista-usuarios")
print("Usuarios actuales:")
print(lista.text)

driver.quit()
