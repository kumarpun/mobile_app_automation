from appium.webdriver.common.appiumby import AppiumBy

import time
from appium import webdriver

class LoginForm():

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locator values
    _updateLaterButton = "//android.widget.Button[@index='3']"