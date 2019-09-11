from common.base import Base
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('https://www.taobao.com')

time.sleep(2)
js = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
# zentao = Base(driver)
# loc1 = (By.ID, 'account')
#
# e = zentao.findElement(loc1)
# r1 = e.is_displayed()
# print(r1)

time.sleep(2)
js = "window.scrollTo(0,0)"
driver.execute_script(js)

ele =driver.find_element_by_link_text("新车")
driver.execute_script("arguments[0].scrollIntoVIEW():", ele)

