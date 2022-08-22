from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
# import time import sleep
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
import html2text

load_dotenv()

# PATH=os.environ.get("DRIVER_PATH")

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.headless = True
options.add_argument('window-size=1200x7000') 
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

# driver = webdriver.Chrome(PATH)
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options,)

# def wikipedia():

#     url = 'https://en.wikipedia.org/wiki/English_language'
#     driver.get(url)
    
#     # text = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[2]').text
#     for i in range(1,10):
#         # if text=='':
#         try:
#             text = driver.find_element_by_xpath(f'//*[@id="mw-content-text"]/div[1]/p[{i}]').text
#             text = re.sub("[\(\[].*?[\)\]]", "", text)
#             print(text)
#         except:
#             print("for loop not running")
#     pass

# def stackoverflow():
#     url = 'https://stackoverflow.com/questions/47258636/scrape-the-p-tag-using-python-selenium'
#     driver.get(url)
#     text = driver.find_element_by_class_name('question-hyperlink').text
#     print(text)
#     # para = driver.find_element_by_class_name('s-prose js-post-body')
#     for i in range(1,5):
#         try: 
#             para1 = driver.find_element_by_xpath(f'//*[@id="question"]/div[2]/div[2]/div[1]/p[{i}]').text 
#             para1 = re.sub("[\(\[].*?[\)\]]", "", para1)

#             print(para1)
#         except:
#             print("error in the except loop")

# def medium():
#     url = 'https://medium.com/featurepreneur/aws-support-plan-12fd3e39cd7d'
#     driver.get(url)
#     text =driver.find_element_by_class_name('pw-post-title it iu iv bn iw ix iy iz ja jb jc jd je jf jg jh ji jj jk jl jm jn jo jp jq jr fx').text
#     print(text)

def raw(html_page):

    # html_page = "https://medium.com/featurepreneur/aws-support-plan-12fd3e39cd7d"

    driver.get(html_page)
    page = driver.page_source

    h = html2text.HTML2Text()
    h.ignore_links = True
    h.IMAGES_TO_ALT = True
    h.SKIP_INTERNAL_LINKS = True
    text = h.handle(str(page))

    # f = open("html_text.txt", "w")         
    # for line in h.handle(str(page)):      
    #     f.write(line)
    #     #print (line)                  
    # f.close()
    
    # print(text)
    return text

if __name__ == '__main__':
    # wikipedia()
    # stackoverflow()
    # medium()
    raw("https://medium.com/featurepreneur/aws-support-plan-12fd3e39cd7d")