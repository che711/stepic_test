from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome('/home/andrew/Рабочий стол/Andrei_Che/stepic_test/chromedriver')
browser.get(link)
find_num1 = browser.find_element_by_id('num1')
num1 = find_num1.text
find_num2 = browser.find_element_by_id('num2')
num2 = find_num2.text
y = int(num1) + int(num2)
x = str(y)
#input1 = browser.find_element_by_xpath('//*[@id="dropdown"]')
#input1.send_keys(y)

sel = Select(browser.find_element_by_xpath('//*[@id="dropdown"]'))
sel.select_by_value(x)


button3 = browser.find_element_by_class_name("btn.btn-default")
button3.click()
time.sleep(5)
browser.quit()
print(y)


#