from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = 'C:\DEV\Webdriver\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

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
