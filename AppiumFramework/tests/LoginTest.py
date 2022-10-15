from AppiumFramework.base.DriverClass import Driver
import AppiumFramework.utilities.CustomLogger as cl

driver = Driver()
log = cl.customLogger()

driver.getDriverMethod()
log.info("Launching App")
