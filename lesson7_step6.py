import unittest
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
'''
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome('/home/andrew/Рабочий стол/Andrei_Che/stepic_test/chromedriver')
browser.get(link)
elem = browser.find_element_by_id('treasure')
x = elem.get_attribute("valuex")
y = calc(x)
input1 = browser.find_element_by_xpath('//*[@id="answer"]')
input1.send_keys(x)
time.sleep(5)
browser.quit()


'''
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome('/home/andrew/Рабочий стол/Andrei_Che/stepic_test/chromedriver')
    browser.get(link)
    elem = browser.find_element_by_id('treasure')
    x = elem.get_attribute('valuex')
    y = calc(x)
    input1 = browser.find_element_by_xpath('//*[@id="answer"]')
    input1.send_keys(y)
    button1 = browser.find_element_by_id("robotCheckbox")
    button1.click()
    button2 = browser.find_element_by_id("robotsRule")
    button2.click()
    button3 = browser.find_element_by_class_name("btn.btn-default")
    button3.click()

finally:
    time.sleep(10)
    browser.quit()



#