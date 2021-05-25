from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome('/home/andrew/Рабочий стол/Andrei_Che/stepic_test/chromedriver')
browser.maximize_window()
browser.get(link)
elem1 = browser.find_element_by_id('input_value')
num = elem1.text
x = int(num)
y = calc(x)
elem2 = browser.find_element_by_id('answer')
elem2.send_keys(y)

radio = browser.find_element_by_id("robotCheckbox")
radio.click()
browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
button2 = browser.find_element_by_id("robotsRule")
button2.click()
button3 = browser.find_element_by_xpath("/html/body/div/form/button")
button3.click()
time.sleep(10)
browser.quit()

#28.905823804300987