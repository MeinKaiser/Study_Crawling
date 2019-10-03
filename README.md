# Study_Crawling
Start Learning Crawling, Selenium, Scrapy, etc..

Selenium은 기존 방식과 다르게 브라우저를 실제로 작동시키는 방법으로 데이터를 크롤링해옵니다.
실제로 Google_Chrome이나 Headless Chorme, PahntomJS 등을 이용하여 브라우저에서 데이터가 나오게 하고 그 데이터를 기반으로 크롤링 해옵니다.

<h2>기본적인 사용방법</h2>
 <p><h4>1. Selenium을 import 합니다 </h4>

    일반적으로 아래와 같이 import하는 경우가 많습니다.
    <br>
    <strong>from selenium import webdriver
    <br>
    from selenium.webdriver.common.keys import Keys</strong>
    <br>
    <h4>2. Chromedriver의 위치를 저장한 후, driver 객체에 저장합니다.</h4>

    chormedriver = ' '
    <br> 
    driver = wevdriver.Chrome(chromedriver)
    <br>
    <h4>3.driver객체로 하여금 get을 실행시킵니다.</h4> 

    driver.get(" # 주소 " )
    <br>
    위와 같은 방식으로 간단한 request 혹은 get의 진행을 Selenuium(Chromedriver ver)로 진행할 수 있습니다.
    
  </p>
