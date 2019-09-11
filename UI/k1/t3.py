from common.base import Base
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
zentao = Base(driver)

loc1 =('link text', '设置')
mouse = zentao.findElement(loc1)
ActionChains(driver).move_to_element(mouse).perform()

loc2 = ('link text', '搜索设置')
zentao.click(loc2)
loc3 = ('xpath', ".//*[@id='nr']/option[3]")
r1 = zentao.findElement(loc3).is_selected()
print(r1)

loc4 = ('id', 'nr')
select = zentao.findElement(loc4)
Select(select).select_by_index(2)

r2 = zentao.findElement(loc3).is_selected()
print(r2)
