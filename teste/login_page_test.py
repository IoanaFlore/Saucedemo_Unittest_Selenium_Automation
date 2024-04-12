import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class LoginPageTest(unittest.TestCase):
    MAIN_URL = "https://www.saucedemo.com/"
    TEXT_STANDARD_USER ='standard_user'
    TEXT_PASSWORD  = 'secret_sauce'
    INPUT_USERNAME = (By.ID, 'user-name')
    INPUT_PASSWORD = (By.ID, 'password')
    BUTTON_LOGIN = (By.ID, 'login-button')
    HR_LOGIN_ERROR = (By.CSS_SELECTOR,'h3[data-test="error"]')

    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get(self.MAIN_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)

    def tearDown(self):
        self.driver.quit()

    def test_page_title(self):
        expected_title = "Swag Labs"
        actual_title = self.driver.title

        # assert expected_title == actual_title, "Unexpected title"
        self.assertEqual(expected_title, actual_title, "Unexpected title")

    def test_elements_are_visible(self):
        # assert self.driver.find_element(*self.INPUT_USERNAME).is_displayed()
        self.assertTrue(self.driver.find_element(*self.INPUT_USERNAME).is_displayed(), "Username input is visible")
        self.assertTrue(self.driver.find_element(*self.INPUT_PASSWORD).is_displayed(), "Password input is not visible")
        self.assertTrue(self.driver.find_element(*self.BUTTON_LOGIN).is_displayed(), "Login button is not visible")

    def test_login_valid(self):
        self.driver.find_element(*self.INPUT_USERNAME).send_keys(self.TEXT_STANDARD_USER)
        self.driver.find_element(*self.INPUT_PASSWORD).send_keys(self.TEXT_PASSWORD)
        self.driver.find_element(*self.BUTTON_LOGIN).click()

       # assert "inventory" in self.driver.current_url, "Login Failed"
        self.assertIn("inventory",self.driver.current_url,"Login Failed")

    def test_login_invalid(self):
        self.driver.find_element(*self.INPUT_USERNAME).send_keys("username")
        self.driver.find_element(*self.INPUT_PASSWORD).send_keys("11234")
        self.driver.find_element(*self.BUTTON_LOGIN).click()

        # verifica daca eroarae e afaisata 
        self.assertTrue(self.driver.find_element(*self.HR_LOGIN_ERROR).is_displayed(),"Login error not displayed")