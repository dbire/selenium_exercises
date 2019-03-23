# Section 6 exercise 2 : Get attribute value

#   By default, py.test captures the result of standard out so that it can control how it prints it out. *
#   If it didn't do this, it would spew out a lot of text without the context of what test printed that text.

#   If you would like to see print statements as they are executed, you can pass the -s flag to pytest:
#       pytest -s test_3_6_2.py

import os
import logging
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome()

def test_3_6_2():
    logging.debug("Running test_3_6_2")

    url = 'http://automationpractice.com/index.php'
    driver.get(url)
    try:
        element = driver.find_element_by_class_name('login')
        element_outerHTML=element.get_attribute("outerHTML")
        print("The outerHTML attribute of the element located by its login class is : '" + element_outerHTML + "'")
    except NoSuchElementException:
        print("The search box element was not found")
    driver.quit()

