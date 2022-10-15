from appium.webdriver import webdriver


class Driver:

    def getDriverMethod(self):
        # Create "Desired Capabilities"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '13'
        desired_caps['deviceName'] = 'sdk_gphone64_x86_64'
        desired_caps['app'] = ('/Users/apple/Downloads/c8aec8df-a539-4ef7-8105-623a4c57edb3.apk')
        desired_caps['appPackage'] = 'com.enthuziastic.mobileapp.staging'
        desired_caps['appActivity'] = 'com.enthuziastic.mobileapp.MainActivity'

        # Create "Driver object"
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver
