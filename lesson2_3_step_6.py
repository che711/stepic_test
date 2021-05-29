"""
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно
переключить WebDriver на новую вкладку и решить в ней задачу.
Сценарий для реализации выглядит так:
    1. Открыть страницу http://suninjuly.github.io/redirect_accept.html
    2. Нажать на кнопку
    3. Переключиться на новую вкладку
    4. Пройти капчу для робота и получить число-ответ
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть
ограничение по времени), вы увидите окно с числом. Отправьте полученное
число в качестве ответа на это задание.
"""

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

def test_alert():
    browser = webdriver.Chrome()
    browser.get(link)
    but = browser.find_element_by_xpath("/html/body/form/div/div/button")
    but.click()
    time.sleep(0.5)
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)
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
