import pytest
from selenium import webdriver
import time
import math

locator = '/html/body/div[1]/div[2]/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/div/div/div[2]/div/pre'


@pytest.fixture(scope="function")
def browser():
    #print("\nstart browser for test..")
    browser = webdriver.Chrome('/home/andrew/Рабочий стол/Andrei_Che/stepic_test/chromedriver')
    yield browser
    #print("\nquit browser..")
    browser.quit()

@pytest.fixture()
def urls():
    url = [
        'https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1',
    ]


class TestLesson():

    def test_open_bro_and_urls(self, browser, urls):
        answer = math.log(int(time.time()))
        tut = browser.find_element_by_xpath('//*[@id="ember94"]')
        answer.send_keys(tut)
        tam = browser.find_element_by_class_name('submit-submission')
        tam.click()
        correct = browser.find_element_by_xpath(locator)
        assert correct == 'Correct', 'Упал'




if __name__ == "__main__":
    pytest.main()