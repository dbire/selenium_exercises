# Section 5 exercise 3 : Locate by Tag Name

import os
import logging
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome()

def test_3_5_3():
    logging.debug("Running test_3_5_3")

    url = 'http://automationpractice.com/index.php'
    driver.get(url)
    try:
        element = driver.find_element_by_tag_name("h1")
        print("The search box element was found")
    except NoSuchElementException:
        print("The search box element was not found")
    driver.quit()