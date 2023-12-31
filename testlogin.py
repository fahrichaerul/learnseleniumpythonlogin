import unittest
import time
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
#DEFAULT_EXECUTABLE_PATH = "chromedriver"

# test scenario
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        #webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
 
    # positive case
    def test_a_success_login(self):
    # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/v1/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

    # negative case
    def test_a_empty_login(self):
    # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/v1/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        def tearDown(self):
            self.browser.close()

    # negative case
    def test_a_failed_login(self):
    # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/v1/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("test") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("test") # isi password
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        def tearDown(self):
            self.browser.close()


if __name__ == "__main__":
        unittest.main()

