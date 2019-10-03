from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#드라이버 생성
chromedriver = 'C:\DEV\Webdriver\chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

driver.get('https://www.python.org')

# assert 옆에 있는게 driver로 연 페이지의 title에 없으면 멈춰버려라!
# assert "Python" in driver.title

#find_element_by_name() 과 find_elements_by_name()도 있다.
#엘레멘트를 가져와서 거기다가 뭔가를 할 수 있다.

# elem.clear() 이거 하면, 그 input 초기화
# elem.send_keys()하면, 그 안에 이벤트 전송
# elem.send_keys(Keys.RETURN) 하면, 엔터 입력!

elem = driver.find_element_by_name("q")
elem.clear()

elem.send_keys("python")
elem.send_keys(Keys.RETURN)

#driver.page_source 가 나오면, 그건 전체 소스 가져온거
#assert "No result found" not in driver.page_source의 의미는 no result found나오면, 멈춰버려라! 라는 뜻

#검색에는 시간이 걸리기 때문에, time.sleep을 해주는 것이 좋다!
#driver.quit()는 크롬 브라우저 닫기

time.sleep(2)

h3s = driver.find_elements_by_tag_name("h3")
for h3 in h3s:
    print(h3.text)
driver.quit()

#find_element_by_tag_name도 가능하다 마찬가지로 elements도 가능!

