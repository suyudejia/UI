from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import selenium
class LoginZenTao():
    def __init__(self,driver):
        self.driver = driver
    def login(self,user='admin',psw='1234admin'):
        self.driver.get('http://127.0.0.1/zentao/user-login.html')
        self.driver.find_element_by_id("account").send_keys(user)
        self.driver.find_element_by_name('password').send_keys(psw)
        self.driver.find_element_by_id('submit').click()
        self.driver.find_element(By.ID,'account')
        self.driver.find_element(By.NAME,'password')

    def findElement(self,driver,loctor,timeout=10,t=0.5):
        ele = WebDriverWait(driver,timeout,t).until(lambda x:x.find_element(*loctor))
if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    zentao = LoginZenTao(driver)
    zentao.login()