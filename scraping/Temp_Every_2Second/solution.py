from datetime import datetime
from selenium import webdriver
import time


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("disable-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com")
    return driver


def clean_text(text):
    output = float(text.split(": ")[-1])
    return output


def write_file(text):
    """Write input text into a text file"""
    # Add file name like date
    filename = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.txt"
    # file and input text
    with open(filename, 'w') as file:
        file.write(text)


def temp():
    driver = get_driver()
    while True:
        # Every time when loop starts he waits for 2 seconds
        time.sleep(2)
        # Temperature value
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
        # Convert to string and assign to text variable
        text = str(clean_text(element.text))
        write_file(text)


print(temp())
