from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
# import time import sleep
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
import re

load_dotenv()

PATH=os.environ.get("DRIVER_PATH")


driver = webdriver.Chrome(PATH)
def startpy():

    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('window-size=1200x7000')

    driver = webdriver.Chrome(PATH)

    url = 'https://en.wikipedia.org/wiki/API'
    driver.get(url)

    text = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[2]').text
    if text=='':
        text = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[3]').text
    text = re.sub("[\(\[].*?[\)\]]", "", text)
    print(text)
    pass


if __name__ == '__main__':
    startpy()