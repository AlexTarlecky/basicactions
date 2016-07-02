from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import unittest


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.facebook.com")

    def test_login(self):
        driver = self.driver
        facebookUsername="atarlecky@gmail.com"
        facebookPassword="Whitebay1!"
        emailFieldID="email"
        passwordFieldID="pass"
        loginButtonXpath="//input[@value='Log In']"
        facebookLogoXpath="//*[@id='blueBarDOMInspector']"

        emailFieldelement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passwordFieldelement = WebDriverWait(self.driver, 10).until (lambda driver: driver.find_element_by_id(passwordFieldID))
        loginButtonelement = WebDriverWait(self.driver, 10).until (lambda driver: driver.find_element_by_xpath(loginButtonXpath))

        emailFieldelement.clear()
        emailFieldelement.send_keys(facebookUsername)
        passwordFieldelement.clear()
        passwordFieldelement.send_keys(facebookPassword)
        loginButtonelement.click()

        WebDriverWait(self.driver, 20).until(lambda driver: driver.find_element_by_xpath(facebookLogoXpath))



    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
