import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/mm43.html"

driver.get(URL)
submit = driver.find_element_by_id('submit')
def clear_data():
    driver.find_element_by_id('email').clear()

#TC1 helyes kitoltes: teszt@elek.hu

driver.find_element_by_id('email').send_keys('teszt@elek.hu')
submit.click()
clear_data()

time.sleep(2)
#TC2 helytelen kitoltes: teszt@
#hibauzenet eredeti nyelven: Please enter a part following '@'. 'teszt@' is incomplete.
error_msg = 'Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.'
driver.find_element_by_id('email').send_keys('teszt@')
submit.click()

assert error_msg == driver.find_element_by_xpath('/html/body/div/div/form/div').text
clear_data()
#TC3 ures kitoltes
#hibauzenet eredeti nyelven: Please fill out this field.
error_msg2 = 'Kérjük, töltse ki ezt a mezőt.'
driver.find_element_by_id('email').send_keys(' ')
submit.click()
assert error_msg2 == driver.find_element_by_xpath('/html/body/div/div/form/div').text
driver.close()