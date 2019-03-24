# Chapter 4 Section 3 exercise 1 : Working with Page Objects

import logging,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO)

class MainPage():
    # Locators
    search_form_loc = (By.ID, 'searchbox')
    search_query_input_loc= (By.NAME, 'search_query')
    submit_button_loc = (By.XPATH, "//button[@type='submit']")

    add_to_cart_buttons_loc = (By.XPATH, "//a[@title='Add to cart']")

    # Shopping cart
    product_name_loc = (By.XPATH, "//span[@id='layer_cart_product_title']")
    product_quantity_loc = (By.XPATH, "//span[@id='layer_cart_product_quantity']")

    def __init__(self, driver):
        self.driver = driver

    def Search(self, search_text):
        # Asterisk in python allow to unpack a tuple or an array as an input of a function
        search_form=self.driver.find_element(*self.search_form_loc)
        search_form.click()
        search_query_input=self.driver.find_element(*self.search_query_input_loc)
        search_query_input.clear()
        search_query_input.send_keys(search_text)
        submit_button=self.driver.find_element(*self.submit_button_loc)
        submit_button.click()

    def AddToCartByNum(self, item_num):
        add_to_cart_buttons = self.driver.find_elements(*self.add_to_cart_buttons_loc)
        add_to_cart_button = add_to_cart_buttons[item_num]
        add_to_cart_button.click()

    def GetShoppingCartContent(self):
        product_name = self.driver.find_element(*self.product_name_loc).text
        product_quantity = self.driver.find_element(*self.product_quantity_loc).text
        return (product_name, product_quantity)

def test_4_3_1():
    logging.debug("running test_3_8_3")
    driver = webdriver.Chrome()
    driver.get("http://automationpractice.com")
    MainPage(driver).Search("chiffon")
    MainPage(driver).AddToCartByNum(0)
    time.sleep(2)
    (name,quantity) = MainPage(driver).GetShoppingCartContent()
    assert name == 'Printed Chiffon Dress', 'Incorrect product name in shopping cart'
    assert quantity == '1', 'The quantity should be 1'
    driver.close()