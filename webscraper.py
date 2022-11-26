from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import regex as re
import sys
num = sys.argv[1]
handle = open('houses{}.csv'.format(num), 'w')
driver = webdriver.Firefox('/home/axel/.local/bin')
driver.get("https://www.inmuebles24.com/casas-o-duplex-o-casa-en-condominio-o-departamentos-en-venta-en-guadalajara-o-zapopan-o-san-pedro-tlaquepaque-mas-de-200000-pesos-ordenado-por-precio-ascendente-pagina-{}.html".format(num))
time.sleep(8)
listings = driver.find_elements(By.CLASS_NAME, "sc-1tt2vbg-3") # Listings
for item in listings:
	price = item.find_element(By.CLASS_NAME, "sc-12dh9kl-4").text.split(' ')[1] # Precio
	addr = item.find_element(By.CLASS_NAME, "sc-ge2uzh-0").text # Dirección
	elems = item.find_element(By.CLASS_NAME, "sc-1uhtbxc-0") # Info
	spans = elems.find_elements(By.TAG_NAME, "span")
	details = []
	for span in spans:
		if re.search("\d+\ [A-Za-zñ]+.", span.text) and details.count(span.text) == 0:
			details.append(span.text)
	line = "{}\t{}\t{}\t{}\t{}\t{}\n".format(price, addr, details[0], details[1], details[2], details[3])
	handle.write(line)
driver.close()