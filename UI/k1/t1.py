from selenium import webdriver
import time
driver = webdriver.Firefox() #启动浏览器
driver.get("https://www.baidu.com")

time.sleep(2)

driver.get("https://www.sogou.com")
driver.back()

time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.quit()