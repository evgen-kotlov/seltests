from selenium import webdriver
import unittest, time
from selenium.webdriver.common.keys import Keys

class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.ru/")

    def test_01(self):
        driver = self.driver
        input_field = driver.find_element_by_name('q')
        input_field.send_keys("python")
        input_field.send_keys(Keys.ENTER)

        time.sleep(2)

    def test_02(self):
        driver = self.driver
        input_field = driver.find_element_by_name('q')
        input_field.send_keys("python")
        time.sleep(2)
        input_field.send_keys(Keys.DOWN)
        input_field.send_keys(Keys.DOWN)
        input_field.send_keys(Keys.ENTER)

        time.sleep(2)


        titles = driver.find_elements_by_id("rso")
        for title in titles:
            assert "python" in title.text.lower()





    def tearDown(self):
            self.driver.quit()

if __name__=='__main__':
    unittest.main()



