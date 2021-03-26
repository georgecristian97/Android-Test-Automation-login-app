from appium import webdriver

@classmethod
def androidcfg():
    dc={}

    dc['platformName'] = 'Android'
    dc['deviceName'] = 'emulator-5554'
    dc['platformVersion'] = '11'
    dc['app'] = "/Users/x123/Documents/GitHub/Android-Test-Automation-login-app/Login 1.0.apk"
    driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()