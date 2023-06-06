import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://stepik.org/lesson/236895/step/1"
browser = webdriver.Chrome()
browser.implicitly_wait(5)
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

time.sleep(5)
button_2 = browser.find_element(By.CLASS_NAME, "submit-submission")
button_2.click()
time.sleep(10)
result = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
message = "Correct!"
if message in result.text:
    print('ok')
else:
    print('not ok')