import unittest
from appium import webdriver

class test_1(unittest.TestCase):
    dc={}
    driver = None

    def setUp(self):

        self.dc['platformName'] = 'Android'
        self.dc['deviceName'] = 'emulator-5554'
        self.dc['platformVersion'] = '11'
        self.dc['app'] = "/Users/x123/Documents/GitHub/Android-Test-Automation-login-app/Login 1.0.apk"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)
        self.driver.implicitly_wait(30)



    def testTheUsernameAndPassword(self):

        xm = self.driver.find_elements_by_class_name('android.widget.EditText')
        for i in xm:
            if i.text in 'User name':
                i.send_keys('company')
            if i.text in 'Password':
                i.send_keys('company')
        self.driver.find_element_by_id('tn.qmed.login:id/buttonClick').click()
        self.driver.find_element_by_id('tn.qmed.login:id/declineButton').click()

        # if last test
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
