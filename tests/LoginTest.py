import unittest
import pytest
from selenium import webdriver

import time
from pages.LoginPage import LoginForm

@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.lf = LoginForm(self.driver)
