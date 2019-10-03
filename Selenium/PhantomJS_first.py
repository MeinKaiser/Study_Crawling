#PhantomJS는 이제 selenuim의 한계를 극복하기 위해서 만들어낸 것
# - 브라우저를 키고, 다 띄우고 그리고 사람처럼 움직이는 것의 한계
# - 그렇게 함으로써 시간을 단축시킬거라고 생각했는데, 별로 그닥 눈에 띄게 좋아지지는 않았다.

#근데 이게 불안정할 수 있어서, Headless chrome 을 추천한다!!!


#PhantomJS 위치 : C:\DEV\Webdriver\phantomjs-2.1.1-windows\bin\phantomjs.exe

#########################################이전 것 그대로 로드########################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# chromedriver = 'C:\DEV\Webdriver\chromedriver.exe'
driver = webdriver.PhantomJS('C:/DEV/Webdriver/phantomjs-2.1.1-windows/bin/phantomjs.exe')

#######################Phantomjs 이제 업그레이드 안한다!!!!!##################
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
