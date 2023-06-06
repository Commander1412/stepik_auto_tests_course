import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()

message = "Correct!"
address = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1","https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"]

@pytest.mark.parametrize('number', address)
class Testanswer:
    def test_answer(self,browser, number):
        link = f"{number}"
        browser.get(link)

        button = browser.find_element(By.ID, "ember33")
        button.click()

        login = browser.find_element(By.ID, "id_login_email")
        login.send_keys("gurskiysv97@mail.ru")

        password = browser.find_element(By.ID, "id_login_password")
        password.send_keys("Qweasdzxc123/")

        button_1 = browser.find_element(By.CSS_SELECTOR, "#login_form > button")
        button_1.click()

        time.sleep(5)
        input = browser.find_element(By.TAG_NAME, "textarea")
        answer = math.log(int(time.time()))
        input.send_keys(answer)

        time.sleep(3)
        button_2 = browser.find_element(By.CLASS_NAME, "submit-submission")
        button_2.click()
        time.sleep(5)
        result = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
        finish = ""
        assert message in result.text, "НеУспех-неуспешный!"

