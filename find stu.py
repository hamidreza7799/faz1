import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class StuSearch(unittest.TestCase):

    def Setup(self):
        self.driver = webdriver.Edge()

    def StuFinder(self):
        driver = self.driver
        driver.get("http://www.stu.iust.ac.ir")
        self.assertIn("stu" , driver.title)
        elem = driver.find_keys_by_name("u")
        elem.send_keys("stu")
        elem.send_keys(Keys.RETURN)
        assert "no file found" not in driver.source_page

        def tearDown(self):
            self.driver.close()

if __name__ == "main":
    unittest.main()
