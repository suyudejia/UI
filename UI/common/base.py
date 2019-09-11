from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
class Base():
    def __init__(self,driver:webdriver.Firefox):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def findElementNew(self, loctor):
        ''''''
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(loctor))
        return ele

    def findElement(self,loctor):
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loctor))
        return ele
    def findElements(self,loctor):
        try:
            eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*loctor))
            return eles
        except:
            return []

    def senKeys(self,locator,text):
        ele = self.findElement(locator)
        ele.send_keys(text)
    def click(self,locator):
        ele = self.findElement(locator)
        ele.click()
    def clear(self,loctor):
        ele = self.findElement(loctor)
        ele.clear()
    def isSelected(self,loctor):
        '''判断元素是否被选中，返回bool值'''
        ele = self.findElement(loctor)
        r = ele.is_selected()
        return r

    def isElementExist(self,loctor):
        try:
            ele = self.findElement(loctor)
            return True
        except:
            return False

    def isElementExist2(self, loctor):
        eles = self.findElements(loctor)
        n = len(eles)
        if n == 0:
            return False
        elif n ==1:
            return True
        else:
            print('定位到元素的个数： %s' %n)
            return True

    def is_title(self, _title):
        '''返回布尔值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False


    def is_title_contains(self, _title):
        '''返回布尔值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_txt_in_element(self,loctor,_title):
        '''返回布尔值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(loctor,_title))
            return result
        except:
            return False

    def is_value_in_element(self,loctor,_title):
        '''返回布尔值,value为空字符串返回False'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(loctor,_title))
            return result
        except:
            return False

    def is_alert(self):
        '''alert是不是在'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def get_text(self,loctor):
        '''获取文本'''
        try:
            t = self.findElement(loctor).text
            return t
        except:
            print("获取text失败，返回''")
            return ""

    def get_attribute(self,loctor,name):
        '''获取属性'''
        try:
            element = self.findElement(loctor)
            return element.get_attribute(name)
        except:
            return ""

    def move_to_element(self,loctor):
        '''鼠标悬停'''
        ele = self.findElement(loctor)
        ActionChains(driver).move_to_element(ele).perform()

    def select_by_index(self,loctor,index=0):
        element = self.findElement(loctor)
        Select(element).select_by_index(index)

    def select_by_index(self, loctor, value):
        element = self.findElement(loctor)
        Select(element).select_by_value(value)

    def select_by_index(self, loctor, text):
        element = self.findElement(loctor)
        Select(element).select_by_visible_text(text)

    def js_focus_element(self,loctor):
        '''聚焦元素'''
        target = self.findElement(loctor)
        self.driver.execute_script("arguments[0].scrollIntoVIEW():", target)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        '''滚动到底部'''
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)





if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1/zentao/user-login.html')
    zentao = Base(driver)
    loc1 = (By.ID,'account')
    loc2 = (By.CSS_SELECTOR, '[name="passwordsa"]')
    # loc3 = (By.XPATH, '//*[@id="submit"]')
    # zentao.senKeys(loc1,'admin')
    # zentao.senKeys(loc2,'1234admin')
    # zentao.click(loc3)
    r1 = zentao.isElementExist2(loc1)
    print(r1)
    r2 = zentao.isElementExist2(loc2)
    print(r2)