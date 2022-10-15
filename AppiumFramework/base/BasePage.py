from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, NoSuchElementException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __int__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorValue, locatorType):
        locatorType = locatorType.lower()
        element = None

        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])

        if locatorType == "id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ID, locatorValue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locatorValue))
            return element
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                         'UiSelector().description("%s")' % (locatorValue)))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(%d)" % int(locatorValue)))
            return element
        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("%s")' % locatorValue))
            return element
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '%s' % (locatorValue)))
            return element
        else:
            self.log.info("Locator value " + locatorValue + "not found")

        return element
