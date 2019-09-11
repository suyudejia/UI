
from selenium import webdriver
import unittest
from k1.dd import login

class LoginCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login_1(self):
        login(self.driver)

