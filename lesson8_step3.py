from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome('/home/andrew/Рабочий стол/Andrei_Che/stepic_test/chromedriver')
browser.get(link)
elem1 = browser.find_element_by_id('num1')
elem2 = browser.find_element_by_id('num2')
num1 = elem1.text
num2 = elem2.text
y = int(num1) + int(num2)
x = str(y)
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(x)

#input1 = browser.find_element_by_id('answer')
#input1.send_keys(x)

button3 = browser.find_element_by_xpath("/html/body/div/form/button")
button3.click()
time.sleep(10)
browser.quit()


#28.858909851891642


