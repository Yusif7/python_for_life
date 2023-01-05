from selenium import webdriver
import time


def getdriver():
    # set options to make browser easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
    return driver


def clean_text(text):
    """Extract temperature from text"""
    output = float(text.split("%")[0])
    return output


def main():
    driver = getdriver()
    time.sleep(2)
    element = driver.find_element(by="xpath", value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')
    return str(clean_text(element.text))


print(main())
