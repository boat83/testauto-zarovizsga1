import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/tts4.html"

driver.get(URL)

submit = driver.find_element_by_id('submit')
# 100 gombnyomas vegrehajtasa ciklussal
for _ in range(100):
    submit.click()
result = driver.find_elements_by_tag_name('li')
counter = 0
# vegigiteralunk is megszamoljuk a fej ertekeket
for i in result:
    if i.text == 'fej':
        counter = counter + 1
print(counter)

# vizsgalat min 30 fej
assert counter > 30
print('Tobb mint harmic, helyes mukodes')
driver.close()