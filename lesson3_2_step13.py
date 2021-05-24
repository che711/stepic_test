import time
import unittest
from selenium import webdriver


class TestClass(unittest.TestCase):

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome('/home/andrew/Рабочий стол/Andrei_Che/stepic_test/chromedriver')
        browser.get(link)
        input1 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
        input3.send_keys("Smolensk")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assertEqual("Congratulations! You have successfully registered!", welcome_text)


    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome('/home/andrew/Рабочий стол/Andrei_Che/stepic_test/chromedriver')
        browser.get(link)
        input1 = browser.find_element_by_xpath('/html/body/div/form/div[1]/div[1]/input')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
        input3.send_keys("Smolensk")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()
