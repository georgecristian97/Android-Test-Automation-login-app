import unittest
from appium import webdriver

class test_1(unittest.TestCase):
    dc={}
    driver = None

    def setUp(self):

        #self.dc['appPackage'] = "com.experitest.ExperiBank"
       # self.dc['appActivity'] = ".LoginActivity"
        self.dc['platformName'] = 'Android'
        self.dc['deviceName'] = 'emulator-5554'
        self.dc['platformVersion'] = '11'
        self.dc['app'] = "D:\\apks\\Login 1.0.apk"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)
        self.driver.implicitly_wait(30)



    def testFirstAutomationTest(self):
        # if len(self.driver.find_elements_by_xpath(“ // *[@ text=’OK’]”)) > 0:
        #     self.driver.find_element_by_xpath(“ // *[ @ text =’OK’]”).click();
        xm = self.driver.find_elements_by_class_name('android.widget.EditText')
        for i in xm:
            if i.text in 'User name':
                i.send_keys('company')
                break
        #self.driver.find_element_by_xpath(' // *[ @ text ="User name"][ @ class = "android.widget.EditText"]').send_keys('company')
        # self.driver.find_element_by_xpath(' // *[ @ text ="Password"][]').send_keys('company')
        # self.driver.find_element_by_xpath(' // *[ @ text ="Login"]').click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
