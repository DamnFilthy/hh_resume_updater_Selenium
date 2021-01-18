from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
from selenium.common.exceptions import ElementClickInterceptedException


# main function
def updater(timer):
    count = 0
    while timer > count:
        # Settings
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_argument("--start-maximized")
        options.add_argument("--headless")
        with open("updater_logs.txt", "a+", encoding='UTF-8') as f:
            now = datetime.datetime.now()
            print(f'Приступаю к работе. Время: {now}')
            f.write(f'Приступаю к работе. Время: {now}\n')
            f.flush()
            # Setup driver
            driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')
            # driver.maximize_window()
            # Start
            driver.get('https://hh.ru/')
            now = datetime.datetime.now()
            print(f'Открыл браузер. Время: {now}')
            f.write(f'Открыл браузер. Время: {now}\n')
            f.flush()
            # Enter
            driver.find_element_by_link_text('Войти').click()
            now = datetime.datetime.now()
            print(f'Нажал кнопку "Войти". Время: {now}')
            f.write(f'Нажал кнопку "Войти". Время: {now}\n')
            f.flush()
            time.sleep(1)
            # Login
            login = driver.find_elements_by_class_name('bloko-input')
            login[1].send_keys('Ваш телефон')
            now = datetime.datetime.now()
            print(f'Ввел номер телефона. Время: {now}')
            f.write(f'Ввел номер телефона. Время: {now}\n')
            f.flush()
            time.sleep(1)
            # Password
            passwd = driver.find_elements_by_class_name('bloko-input')
            passwd[2].send_keys('Ваш пароль')
            now = datetime.datetime.now()
            print(f'Ввел пароль. Время: {now}')
            f.write(f'Ввел пароль. Время: {now}\n')
            f.flush()
            time.sleep(1)
            # Enter
            enter = driver.find_elements_by_class_name('bloko-form-row')
            enter[1].click()
            now = datetime.datetime.now()
            print(f'Залогинился на сайт. Время: {now}')
            f.write(f'Залогинился на сайт. Время: {now}\n')
            f.flush()
            time.sleep(3)
            # Enter resume
            driver.find_element_by_css_selector(".HH-Supernova-NaviLevel2-Link").click()
            # driver.find_element_by_link_text("Мои резюме").click()
            now = datetime.datetime.now()
            print(f'Зашел во вкладку "Мои резюме". Время: {now} ')
            f.write(f'Зашел во вкладку "Мои резюме". Время: {now}\n')
            f.flush()
            time.sleep(2)
            # Поднимает в поиске резюме
            try:
                driver.find_element_by_css_selector(".bloko-link_dimmed").click()
                now = datetime.datetime.now()
                print(f'Поднял резюме в поиске. Время: {now}')
                f.write(f'Поднял резюме в поиске. Время: {now}\n')
                f.flush()
                time.sleep(2)
            except ElementClickInterceptedException:
                now = datetime.datetime.now()
                print(f'Еще рано! кнопка недоступна! Время: {now}')
                f.write(f'Еще рано! кнопка недоступна! Время: {now}\n')
                f.flush()
            # Close
            driver.close()
            now = datetime.datetime.now()
            print(f'Выключил браузер. Время: {now}')
            f.write(f'Выключил браузер. Время: {now}\n')
            f.flush()
            # Counter
            timer -= 1
            now = datetime.datetime.now()
            print(f'Перематываю счетчик, осталось отработать {timer} раз. Время: {now}')
            f.write(f'Перематываю счетчик, осталось отработать {timer} раз. Время: {now}\n')
            f.flush()
            # Waiting 4 hours
            now = datetime.datetime.now()
            print(f'Ложусь спать на 4 часа. Время: {now}')
            f.write(f'Ложусь спать на 4 часа. Время: {now}\n')
            f.flush()
            time.sleep((60 * 60) * 4)
            now = datetime.datetime.now()
            print(f'Проснулся. Время: {now}')
            f.write(f'Проснулся. Время: {now}\n')
            f.flush()


if __name__ == '__main__':
    updater(12)
