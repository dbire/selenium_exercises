# Section 5 exercise 4 : Locate by xpath

import os
import logging
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome()

def test_3_5_5():
    logging.debug("Running test_3_5_5")

    url = 'http://automationpractice.com/index.php'
    driver.get(url)
    try:
        element = driver.find_element_by_xpath('//form[@id="seachbox"]')
        print("The search box element was found")
    except NoSuchElementException:
        print("The search box element was not found")
    driver.quit()

