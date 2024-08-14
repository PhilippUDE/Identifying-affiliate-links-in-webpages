from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Initialisiere den Webdriver
driver = webdriver.Chrome()

# Öffne die Webseite
driver.get('https://www.faz.net/kaufkompass/test/die-beste-schlagbohrmaschine/')

# Warte, bis die Seite vollständig geladen ist
time.sleep(5)  # Dies ist eine einfache Methode; besser wäre es, auf ein bestimmtes Element zu warten

# Finde alle Links auf der Seite
links = driver.find_elements(By.TAG_NAME, 'a')

# Extrahiere die href-Attribute der Links
urls = [link.get_attribute('href') for link in links]

# Schließe den Browser
driver.quit()

# Drucke die gefundenen URLs
for url in urls:
    print(url)
