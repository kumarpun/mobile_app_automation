from AppiumFramework.base.DriverClass import Driver
import AppiumFramework.utilities.CustomLogger as cl
from AppiumFramework.base.BasePage import BasePage

driver1 = Driver()
log = cl.customLogger()

driver = driver1.getDriverMethod()
log.info("Launching App")

bp = BasePage(driver)

element = bp.waitForElement("//android.widget.Button[@index='3']", "xpath")
element.click()
