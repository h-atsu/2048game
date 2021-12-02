from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://play2048.co/")
html_elem = driver.find_element_by_tag_name('html')

TIME_INTERVAL = 1.5


def send_allows():
    while(True):
        time.sleep(TIME_INTERVAL)
        html_elem.send_keys(Keys.UP)  # 「上」を送信
        time.sleep(TIME_INTERVAL)
        html_elem.send_keys(Keys.RIGHT)  # 「右」を送信
        time.sleep(TIME_INTERVAL)
        html_elem.send_keys(Keys.DOWN)  # 「下」を送信
        time.sleep(TIME_INTERVAL)
        html_elem.send_keys(Keys.LEFT)  # 「左」を送信


send_allows()
