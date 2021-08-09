import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/x234.html"

driver.get(URL)

submit = driver.find_element_by_id("submit")


def clear_data():
    driver.find_element_by_id('a').clear()
    driver.find_element_by_id('b').clear()


# TC1 a: 99, b: 12, Eredmény: 222 adatokkal kitoltes

test_data = ['99', '12', '222']

driver.find_element_by_id('a').send_keys(test_data[0])
driver.find_element_by_id('b').send_keys(test_data[1])
submit.click()
time.sleep(2)

assert test_data[2] == driver.find_element_by_id('result').text

clear_data()
time.sleep(2)
# TC2 hibas kitoltes: kiskutya, 12, NaN

test_data2 = ['kiskutya', '12', 'NaN']

driver.find_element_by_id('a').send_keys(test_data2[0])
driver.find_element_by_id('b').send_keys(test_data2[1])
submit.click()
time.sleep(2)

assert test_data2[2] == driver.find_element_by_id('result').text

clear_data()
time.sleep(2)

# TC3 ures kitoltes

test_data3 = [' ', ' ', 'NaN']

driver.find_element_by_id('a').send_keys(test_data3[0])
driver.find_element_by_id('b').send_keys(test_data3[1])
submit.click()
time.sleep(2)

assert test_data3[2] == driver.find_element_by_id('result').text
driver.close()
