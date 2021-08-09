import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# In order for ChromeDriverManager to work you must pip install it in your own environment.
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = "https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html"

driver.get(URL)
# szamok es operandus kiolvasasa
num1 = driver.find_element_by_id('num1').text
num2 = driver.find_element_by_id('num2').text
operator = driver.find_element_by_id('op').text

driver.find_element_by_id('submit').click()

result = driver.find_element_by_id('result').text
time.sleep(3)
print(num1)
print(str(operator))
print(num2)
print(result)
# kalkulacio vegrehajtasa

print('-'*50)
if operator == '+':
    print(int(num1) + int(num2))
elif operator == '-':
    print(int(num1) - int(num2))
elif operator == '*':
    print(int(num1) * int(num2))


driver.close()

