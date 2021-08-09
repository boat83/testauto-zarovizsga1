import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/rv4.html"

driver.get(URL)

# info kigyujtese
cities = driver.find_elements_by_tag_name('li')

city = driver.find_element_by_id('missingCity')
chck_button = driver.find_element_by_id('submit')
grp_cities = driver.find_element_by_id('cites')



