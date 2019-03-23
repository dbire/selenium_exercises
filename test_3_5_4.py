# Section 5 exercise 4 : Locate by Link Text

import os
import logging
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome()

def test_3_5_4_1():
    logging.debug("Running test_3_5_4_1")

    url = 'http://automationpractice.com/index.php'
    driver.get(url)
    try:
        element = driver.find_element_by_link_text("Contact us")
        print("The search box element was found")
    except NoSuchElementException:
        print("The search box element was not found")

def test_3_5_4_2():
    logging.debug("Running test_3_5_4_2")

    url = 'http://automationpractice.com/index.php'
    driver.get(url)
    try:
        element = driver.find_element_by_partial_link_text("Contact")
        print("The search box element was found")
    except NoSuchElementException:
        print("The search box element was not found")
    driver.quit()

