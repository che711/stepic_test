"""
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
    Открыть страницу http://suninjuly.github.io/alert_accept.html
    Нажать на кнопку
    Принять confirm
    На новой странице решить капчу для роботов, чтобы получить число с ответом
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение
по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа на это
задание.

"""
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

def test_alert():
    browser = webdriver.Chrome()
    browser.get(link)
    but = browser.find_element_by_xpath("/html/body/form/div/div/button")
    but.click()
    time.sleep(0.5)
    confirm = browser.switch_to.alert
    confirm.accept()
    elem = browser.find_element_by_id('input_value')
    num = elem.text
    y = calc(num)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    sub = browser.find_element_by_css_selector(".btn")
    time.sleep(0.5)
    sub.click()
    time.sleep(5)
    browser.quit()








