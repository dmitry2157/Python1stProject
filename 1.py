from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Немного настроим наш браузер
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)

# Откроем страницу блога
driver.get("https://blog.noveogroup.ru/")

# Попытаемся найти... кого?
sleep(1)
driver.find_element_by_css_selector("[type=search]").send_keys("настоящих ниндзя")  # P.s. здесь могла бы быть ваша реклама
sleep(1)
driver.find_element_by_css_selector("[type=search]").send_keys(Keys.ENTER)

# И посмотрим, как же стать настоящим ниндзя?
sleep(1)
driver.find_element_by_tag_name("article").click()

# А мы точно открыли ту статью?
sleep(1)
title = driver.find_element_by_css_selector("article>header>h2").text
assert title == "Тестовые площадки для тренировок настоящих ниндзя", "Упс, а мы хотели стать ниндзя :("
print("Yeah! That's it!")

# А теперь можно ознакомиться со статьей
# Чтобы ознакомиться со статьёй получше - удалите строчки ниже
sleep(5)
driver.quit()