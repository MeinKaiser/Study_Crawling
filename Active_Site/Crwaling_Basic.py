from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait # 기다리게 하기 위해서
from selenium.webdriver.support import expected_conditions as EC #조건식 맞추기 위해서

from selenium.common.exceptions import TimeoutException # try, except 용법 사용 위해 가져오기

#EC.presence_of_element_located(( a,"b")) a형태의 b가 뜰때까지 기다려라
# a에는 By.ID, By.CLASS_NAME, By.CSS_SELECTOR, By.TAG_NAME 등등이 다 있음

#키보드,  마우스 동작 자동화
hidden_submenu = driver.find_element_bu_id ()  #이걸로 목적지 객체를 넣고
actions = webdriver.ActionChains(driver)
actions.click(hidden_submenu) #actions에 쫙 뭘 해야되는지 넣는다.
actions.perform()




