import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class ProductsPageTest(unittest.TestCase):
    MAIN_URL = "https://www.saucedemo.com/"
    PRODUCTS_PAGE_URL = "https://www.saucedemo.com/inventory.html"
    TEXT_STANDARD_USER = "standard_user"
    TEXT_PASSWORD = "secret_sauce"

    INPUT_USERNAME = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.ID, "login-button")
    DIV_PRODUCT_ITEM = (By.CSS_SELECTOR, "div[class='inventory_item']")
    BUTTON_ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BUTTON_REMOVE_FROM_CART_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    SPAN_SHOPPING_CART_ITEMS_NUMBER = (By.CSS_SELECTOR, "span[class='shopping_cart_badge']")

    def setUp(self) -> None:
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get(self.MAIN_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)
        self.driver.find_element(*self.INPUT_USERNAME).send_keys(self.TEXT_STANDARD_USER)
        self.driver.find_element(*self.INPUT_PASSWORD).send_keys(self.TEXT_PASSWORD)
        self.driver.find_element(*self.BUTTON_LOGIN).click()

    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.quit()

    def is_element_absent(self, locator):
        elements = self.driver.find_elements(*locator)
        return len(elements) == 0

    def test_page_url(self):
        actual_title = self.driver.current_url
        self.assertEqual(self.PRODUCTS_PAGE_URL, actual_title, "Unexpected page url")

    def test_products_displayed(self):
        products_list = self.driver.find_elements(*self.DIV_PRODUCT_ITEM)
        self.assertTrue(len(products_list) >= 3)

        for product in products_list:
            self.assertTrue(product.is_displayed(), "Error, product not visible.")

    def test_add_backpack_to_cart(self):
        self.assertTrue(self.is_element_absent(self.BUTTON_REMOVE_FROM_CART_BACKPACK), "Remove button is displayed")
        self.assertTrue(self.is_element_absent(self.SPAN_SHOPPING_CART_ITEMS_NUMBER), "Items number is displayed")

        self.driver.find_element(*self.BUTTON_ADD_TO_CART_BACKPACK).click()

        self.assertTrue(self.driver.find_element(*self.BUTTON_REMOVE_FROM_CART_BACKPACK).is_displayed(), "Remove button is not displayed")
        self.assertTrue(self.driver.find_element(*self.SPAN_SHOPPING_CART_ITEMS_NUMBER).is_displayed(), "Items number is not displayed")

        self.assertIn("1", self.driver.find_element(*self.SPAN_SHOPPING_CART_ITEMS_NUMBER).text)