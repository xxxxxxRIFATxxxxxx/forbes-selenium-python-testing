from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class SigninTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="E:/Programming Hero/Projects/forbes-selenium-python-testing/drivers/chromedriver.exe"
        )
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_signin_valid(self):
        self.driver.get("https://www.forbes.com/")

        self.driver.find_element(
            By.CSS_SELECTOR,
            "body > div.main-content.main-content--universal-header > header > nav > div.header__right > div > div > button",
        ).click()

        self.driver.find_element(
            By.XPATH,
            "/html/body/app-main/app-widget/screen-layout/div/main/current-screen/div/screen-login/div[2]/div[1]/input",
        ).send_keys("ckliabomkdnfyedytd@nthrw.com")

        self.driver.find_element(
            By.CSS_SELECTOR,
            "#password",
        ).send_keys("1234567890Aa*")

        self.driver.find_element(
            By.CSS_SELECTOR,
            "#autofill-form > screen-login > button.login-modal__login-button",
        ).click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Passed")
