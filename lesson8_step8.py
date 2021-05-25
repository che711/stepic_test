from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome('/home/andrew/Рабочий стол/Andrei_Che/stepic_test/chromedriver')
browser.maximize_window()
browser.get(link)
find1 = browser.find_element_by_xpath('/html/body/div/form/div/input[1]')
find1.send_keys('I am')
find2 = browser.find_element_by_xpath('/html/body/div/form/div/input[2]')
find2.send_keys("best of the best")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'to_download.txt')
element = browser.find_element_by_xpath('//*[@id="file"]')
element.send_keys(file_path)
find3 = browser.find_element_by_xpath('/html/body/div/form/div/input[3]')
find3.send_keys('oops@gmail.com')

button3 = browser.find_element_by_xpath("/html/body/div/form/button")
button3.click()
time.sleep(10)
browser.quit()
