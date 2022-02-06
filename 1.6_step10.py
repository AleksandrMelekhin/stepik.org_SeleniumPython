'''Попробуем реализовать один из автотестов из предыдущего шага.
Вам дана страница с формой регистрации.
Проверьте, что можно зарегистрироваться на сайте, заполнив только обязательные поля,
отмеченные символом *: First name, last name, email.
Текст для полей может быть любым.
Успешность регистрации проверяется сравнением ожидаемого текста
"Congratulations! You have successfully registered!" с текстом на странице,
которая открывается после регистрации.
Для сравнения воспользуемся стандартной конструкцией assert из языка Python.'''

from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_class_name("form-control.first").send_keys("Aleksandr")
    browser.find_element_by_class_name("form-control.second").send_keys("Melekhin")
    browser.find_element_by_class_name("form-control.third").send_keys("test@test.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()