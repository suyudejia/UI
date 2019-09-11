
def login(driver,user='admin',psw='1234admin'):
    driver.get('http://127.0.0.1/zentao/user-login.html')
    driver.find_element_by_id("account").send_keys(user)
    driver.find_element_by_name('password').send_keys(psw)
    driver.find_element_by_id('submit').click()


if __name__ == '__main__':
    unittest.main()