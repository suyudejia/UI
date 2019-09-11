from selenium import webdriver
import unittest
from pages.login_page import LoginPage,login_url
import ddt
from common.read_excel import ExcelUtil
import os

# testdates = [
#     {"user":"admin","psw":"1234admin","expect":"admin"},
# {"user":"admin","psw":"","expect":""},
# {"user":"admin1111","psw":"1234admin","expect":""},
# ]
propath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
filepath = os.path.join(propath,"common","datas.xlsx")
print(filepath)
sheetName = "Sheet1"
data = ExcelUtil(filepath,sheetName)
testdates = data.dict_data()
print(testdates)



@ddt.ddt
class LoginPageCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginp = LoginPage(cls.driver)
        cls.driver.get(login_url)

    def setUp(self):
        self.loginp.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.get(login_url)


    def login_case(self,user,psw,expect):
        self.loginp.input_user(user)
        self.loginp.input_psw(psw)
        self.loginp.click_login_button()
        result = self.loginp.get_login_name()
        print("测试数据 %s" % result)
        self.assertTrue(result == expect)
    @ddt.data(*testdates)
    def test_01(self,data):
        '''输入账号admin,输入密码123456 点登陆'''
        print("---------------开始测试---------")

        print("测试数据 %s" %data)
        self.login_case(data["user"],data["psw"],data["expect"])
        print("---------------结束: pass!---------")




    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()

