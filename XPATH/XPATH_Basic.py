# XPATH는 옛날에 자주 사용되는 기술임
# 요즘은 Selector 자주 쓰지만 옛 코드들 볼떄 XPATH가 쓸만하다!
# BeautifulSoup에서는 지원조차 하지않는다..

# Xpath: XML 문서 내의 특정 요소나 속성에 접근하기 위한 경로를 지정하는 언어

from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')
options.add_argument('window-size=1920x1080')

chromedriver = 'C:\DEV\Webdriver\chromedriver.exe'
driver = webdriver.Chrome(chromedriver, options=options)
driver.get('http://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=001&oid=025&aid=0002942167')

title = driver.find_element_by_xpath('//*[@id="articleTitle"]')

print(title.text)
