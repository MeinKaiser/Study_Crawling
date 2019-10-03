from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chromedriver = 'C:\DEV\Webdriver\chromedriver.exe'
# driver = webdriver.Chrome(chromedriver)

headless_options = webdriver.ChromeOptions()
headless_options.add_argument('headless')
headless_options.add_argument('disable-gpu') 
#이런 옵션들 다들 넣어줄 수 있다.
# headless_options.add_argument('window-size = 1920x1080')
# head를 바꿔줘서 headless_chrome으로 간다는 것을 속여버릴 수 있음
headless_options.add_argument("lang=Ko_KR")

driver = webdriver.Chrome(chromedriver, options = headless_options)


driver.get('https://xangle.io/')
upside = driver.find_element_by_class_name('narrow-tr-up')
downside = driver.find_element_by_class_name('narrow-tr-down')

print(upside.text)
print(downside.text)
#head 안에 있는 내용들을 가져오고 싶다면
#head_title = driver.find_element_bu_css....
# 이렇게 뽑고 print(head_title.text)하면 안나온다
#print(head_title.get_attribute('text') 해줘야된다.)

#head 안에 있는 녀석들은 get_attribute 해줘야하고! body 녀석들은 text로 가져올 수 있다!
first = upside.text.split("\n")
first = first[0].split("₩")
print(first)

print("\n\n", type(upside.text), type(downside.text))
driver.quit()