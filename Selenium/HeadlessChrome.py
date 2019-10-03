from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = 'C:\DEV\Webdriver\chromedriver.exe'
# driver = webdriver.Chrome(chromedriver)

headless_options = webdriver.ChromeOptions()
headless_options.add_argument('headless')
# headless_options.add_argument('disable-gpu') 이런 옵션들 다들 넣어줄 수 있다.
# headless_options.add_argument('window-size = 1920x1080')
# head를 바꿔줘서 headless_chrome으로 간다는 것을 속여버릴 수 있음
headless_options.add_argument("lang=Ko_KR")





driver = webdriver.Chrome(chromedriver, options = headless_options)

driver.get('https://www.python.org')

assert "Python" in driver.title

print(driver.title)
print(driver.current_url)

#id, name, tag_name, class_name, css_selector, _xpath 모두 다 크롤링이 가능하다!!!

search = driver.find_element_by_name("q")

search.clear()
search.send_keys("python")
search.send_keys(Keys.RETURN)

time.sleep(2)

assert "No result found." not in driver.page_source

data = driver.find_elements_by_css_selector("#content > div > section >form > ul >li >h3 >a")
for item in data:
    print(item.text)
driver.quit()
