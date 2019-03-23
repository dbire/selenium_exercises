# Section 3 exercise 5 : Locate by ID

import os
import logging
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome()

def test_3_5_1():
    logging.debug("Running test_3_5_1")

    url = 'http://automationpractice.com/index.php'
    driver.get(url)
    try:
        element = driver.find_element_by_id("search_query_top")
        print("The search box element was found")
    except NoSuchElementException:
        print("The search box element was not found")
    driver.quit()