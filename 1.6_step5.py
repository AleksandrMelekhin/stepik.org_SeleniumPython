'''На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:

Добавьте в самый верх своего кода import math
Добавьте в код команду, которая откроет страницу: http://suninjuly.github.io/find_link_text
Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой:
str(math.ceil(math.pow(math.pi, math.e)*10000))
(можно вставить данное выражение в свой код, а можно выполнить в интерпретаторе,
скопировать оттуда результат и уже его использовать в вашем коде) 

Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации

Заполните скриптом форму так же как вы делали в предыдущем шаге урока

После успешного заполнения вы получите код - отправьте его в качестве ответа на это задание'''

import math
import time
from selenium import webdriver

link = "http://suninjuly.github.io/find_link_text"
text = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_link_text(text).click()

    input1 = browser.find_element_by_tag_name("input").send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name").send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city").send_keys("Smolensk")
    input4 = browser.find_element_by_id("country").send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(30)
    browser.quit()

#25.209476263309956
