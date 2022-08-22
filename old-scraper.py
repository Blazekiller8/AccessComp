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

    # driver = webdriver.Chrome(PATH)

    # url = ''
    driver.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
    
    # text = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[2]').text
    for i in range(1,10):
        # if text=='':
        try:
            text = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[2]').text
            text = re.sub("[\(\[].*?[\)\]]", "", text)
            print(text)
        except:
            print("for loop not running")
    pass

def stackoverflow():
    url = 'https://stackoverflow.com/questions/47258636/scrape-the-p-tag-using-python-selenium'
    driver.get(url)
    text = driver.find_element_by_class_name('question-hyperlink').text
    print(text)
    # para = driver.find_element_by_class_name('s-prose js-post-body')
    for i in range(1,5):
        try: 
            para1 = driver.find_element_by_xpath(f'//*[@id="question"]/div[2]/div[2]/div[1]/p[{i}]').text 
            para1 = re.sub("[\(\[].*?[\)\]]", "", para1)

            print(para1)
        except:
            print("error in the except loop")

def medium():
    url = 'https://medium.com/featurepreneur/aws-support-plan-12fd3e39cd7d'
    driver.get(url)
    text =driver.find_element_by_class_name('pw-post-title it iu iv bn iw ix iy iz ja jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq jr fx').text
    print(text)

if __name__ == '__main__':
    startpy()
    # stackoverflow()
    # medium()