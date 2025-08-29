import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Configura la carpeta de descargas
download_dir = os.path.abspath("datasets")
os.makedirs(download_dir, exist_ok=True)

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "directory_upgrade": True,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.datos.gov.co/")

# Buscar un dataset, por ejemplo "poblacion"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("poblacion")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

# Haz clic en el primer resultado
first_result = driver.find_element(By.CSS_SELECTOR, "div.dataset-content a")
first_result.click()
time.sleep(3)

# Busca el botón de descarga (puede variar según el dataset)
download_btn = driver.find_element(By.CSS_SELECTOR, "a.btn-primary[href$='.csv'], a.btn-primary[href$='.xlsx']")
download_btn.click()
time.sleep(10)  # Espera a que se descargue el archivo

driver.quit()
print(f"Descarga completada en: {download_dir}")