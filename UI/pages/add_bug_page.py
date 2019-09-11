from selenium import webdriver
from common.base import Base
import time
class AddBugPage(Base):
    #定位登陆
    loc1 = ('id', 'account')
    loc2 = ('css selector', '[name="password"]')
    loc3 = ('xpath', '//*[@id="submit"]')
    #添加BUG
    loc_test = ('link text', '测试')
    loc_bug = ('xpath', ".//*[@id='subNavbar']/ul/li[1]/a")
    loc_addbug = ('xpath', ".//*[@id='mainMenu']/div[3]/a[3]")
    loc_truck = ('xpath', './/*[@id="openedBuild_chosen"]/ul')
    loc_truck_add = ('xpath', './/*[@id="openedBuild_chosen"]/div/ul/li')
    loc_input_title = ('id','title')
    #需要先切换iframe
    loc_input_body = ('class name','article-content')
    loc_avse = ('css selector','#submit')

    #新增的列表
    loc_new = ("xpath",".//*[@id='bugList']/tbody/tr/td[3]/a")


    #
    # def login(self,user='admin',psw='1234admin'):
    #     self.driver.get('http://127.0.0.1/zentao/user-login.html')
    #     self.senKeys(self.loc1,user)
    #     self.senKeys(self.loc2, psw)
    #     self.click(self.loc3)

    def add_bug(self,title='测试提交BUG'):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_addbug)
        self.click(self.loc_truck)
        self.click(self.loc_truck_add)

        self.senKeys(self.loc_input_title,title)

        #输入body
        frame = self.findElement(('class name','ke-edit-iframe'))
        self.driver.switch_to.frame(1)
        #富文本不能用clear
        body = '''[测试步骤】xxx
        [结果]xxx
        [期望结果]xxx
        '''
        self.senKeys(self.loc_input_body,body)
        self.driver.switch_to.default_content()

        self.click(self.loc_avse)

    def is_add_bug_success(self,_text):
        return self.is_txt_in_element(self.loc_new,_text)


if __name__ == '__main__':
    driver = webdriver.Firefox()
    bug = AddBugPage(driver)


    from pages.login_page import LoginPage
    a = LoginPage(driver)
    a.login()

    timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
    title = "测试tijiaoBUG"+timestr
    bug.add_bug(title)
    result = bug.is_add_bug_success(title)
    print(result)