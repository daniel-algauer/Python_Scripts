import time
import datetime
import textReadWriteFunc as txtFunc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="/usr/local/lib/python3.6/dist-packages/selenium/webdriver/chrome/chromedriver")  # Optional argument, if not specified will search path.
driver.get('https://br.tradingview.com/chart/?symbol=BMFBOVESPA:IBOV')
print("\n -> Buscando...\n")
#search_box.submit()

RESULTS_LOCATOR = driver.find_element_by_xpath('/html/body/div[1]/div[7]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]')
WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'symbol-list'))
)

page1_results = driver.find_elements_by_class_name('symbol-list-item')
novoArray = []
cont = 0
date = datetime.datetime.now().strftime('%d.%m.%Y')
for i in page1_results:
    symbol_el = i.find_element_by_class_name('symbol')
    value_el = i.find_element_by_class_name('last')
    symbol = symbol_el.text
    value = value_el.text
    if symbol != "" and value != "":
        novoArray.append(i.text)
        cont = cont + 1
        value = float(value_el.text)
        print("%i: Açao: %s - Preço:%.2f" % (cont, symbol, value))

print("\n - >Total registros retornados: %i"%(cont))