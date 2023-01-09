from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys


def get_driver():
    # Set options to make browsing easier
    # We add some options, 'options' is intance of ChromeOptions class
    options = webdriver.ChromeOptions()

    # know options is an object of ChromeOptions, now add some arguments
    # we disable popup windows because it can confuse the scrap logic
    options.add_argument("disable-infobars")

    # always start browser in maximum window size
    options.add_argument("start-maximized")

    # this argument help us to solve the problem when we use linux systems
    options.add_argument("disable-dev-shm-usage")

    # Some browsers use sandboxes for safety, and we need to disable them
    options.add_argument("disable-sandbox")

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    # Мы используем класс Chrome веб-драйвера.
    # Chrome, этот класс ожидает путь к исполняемому файлу драйвера Chrome,
    # который вы можете скачать и установить из сети.
    # options are pozitional values that is why we to equal it options value
    driver = webdriver.Chrome(options=options)
    # Home page
    # driver.get("http://automated.pythonanywhere.com")
    # We change url adres to work with login interface
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver


# Extract only temperature value without text from site
def clean_text(text):
    # When we split text we have list of strings and we need to select second one
    output = float(text.split(": ")[-1])
    return output


# Script for main text first h1
def main():
    driver = get_driver()
    # Find our full path to our tag
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text


# When we want to scrape dynamic value we need to import time modul,
# and before scraping elements we need to stop the script a few time
def main2():
    driver = get_driver()
    # stay in page 2 second before extracting the element
    time.sleep(2)
    # Find our full path to our tag
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)


def auth_logic():
    driver = get_driver()
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)  # We do 2 operations in one func that we need to wait next one
    # keys.return means that after writing password automatically click Enter
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()  # Click to home button
    print(driver.current_url)  # Show in terminal the url in which we now


# print(main())
# print(main2())
print(auth_logic())
