import unittest
from time import sleep

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException


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

    def compare_txt_classElements(self,classelement, txt):
        if txt == classelement.txt:
            return True
        return False


    def compare_len_classElements(self, classelement, txt):
        if len(txt) == len(classelement.text):
            return True
        return False


    def look_for_login_form(self,class_name ):
        txt = ''

        fnd_elem = self.driver.find_elements_by_class_name(class_name)

        if len(fnd_elem)>1: #we have at least 2 elements

            txt = txt + 'Username and password fields available'+'\n'
        else:
            txt = txt + 'Error Username and password not available'+'\n'
            return False,txt

        if fnd_elem[0].text == 'User name':

            txt = txt + 'Username field available' + '\n'

        else:

            txt = txt + 'Error Username fields not available' + '\n'

        if fnd_elem[1].tag_name == 'Password':


            txt = txt + 'Password field available' + '\n'

        else:

            txt = txt + 'Error Password field not available' + '\n'
            return False,txt

        return True,txt

    def raportExport(self,filename,content):
        filename = filename + '.txt'
        f = open(filename, "a")
        f.write(content)
        f.close()

    def test_login_availability(self):

        ok,txt = self.look_for_login_form('android.widget.EditText')

        if ok == False:
            ok
            assert





    def testTheUsernameAndPassword(self):


        # xm = self.driver.find_elements_by_class_name('android.widget.EditText')
        #
        # print(len(xm))
        # for i in xm:
        #     if i.text in 'User name':
        #         i.send_keys('company')
        #     if i.text in 'Password':
        #         i.send_keys('company')
        # self.driver.find_element_by_id('tn.qmed.login:id/buttonClick').click()
        # self.driver.find_element_by_id('tn.qmed.login:id/declineButton').click()
        print(self.try_catch_classes('android.widget.EditText1'))
        sleep(10)
        # if last test
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
