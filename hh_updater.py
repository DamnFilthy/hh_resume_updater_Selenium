import datetime
import time

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException

# Constans
FAKE_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'


# main function
def updater(timer):
    count = 0
    while timer > count:

        # Settings
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument(
            f"user-agent={FAKE_AGENT}"
        )
        options.add_argument("--start-maximized")
        # options.add_argument("--headless")
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

            # Enter with password
            enter = driver.find_elements_by_class_name('bloko-link-switch')
            enter[1].click()
            now = datetime.datetime.now()
            print(f'Нажал кнопку "Войти с паролем". Время: {now}')
            f.write(f'Нажал кнопку "Войти с паролем". Время: {now}\n')
            f.flush()
            time.sleep(1)

            # Enter mobile phone
            login = driver.find_elements_by_class_name('bloko-input')
            time.sleep(0.5)
            login[1].send_keys('your-mobile')
            time.sleep(0.5)
            now = datetime.datetime.now()
            print(f'Ввел логин. Время: {now}')
            f.write(f'Ввел логин. Время: {now}\n')
            f.flush()
            time.sleep(1)

            # Password
            passwd = driver.find_elements_by_class_name('bloko-input')
            passwd[2].send_keys('your-pass')
            time.sleep(0.5)
            now = datetime.datetime.now()
            print(f'Ввел пароль. Время: {now}')
            f.write(f'Ввел пароль. Время: {now}\n')
            f.flush()
            time.sleep(1)

            # Enter
            enter_button = driver.find_elements_by_css_selector("button[data-qa='account-login-submit']")
            enter_button[0].click()
            now = datetime.datetime.now()
            print(f'Залогинился на сайт. Время: {now}')
            f.write(f'Залогинился на сайт. Время: {now}\n')
            f.flush()
            time.sleep(2)

            # Enter resume
            driver.find_element_by_css_selector(".HH-Supernova-NaviLevel2-Link").click()
            # driver.find_element_by_link_text("Мои резюме").click()
            now = datetime.datetime.now()
            print(f'Зашел во вкладку "Мои резюме". Время: {now} ')
            f.write(f'Зашел во вкладку "Мои резюме". Время: {now}\n')
            f.flush()
            time.sleep(2)

            # Update resume
            try:
                update_btns = driver.find_elements_by_css_selector("button[data-qa='resume-update-button']")
                for button in update_btns:
                    time.sleep(1)
                    button.click()
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
    updater(34)
