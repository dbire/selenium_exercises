# Section 6 exercise 1 : Get text value

#   By default, py.test captures the result of standard out so that it can control how it prints it out. *
#   If it didn't do this, it would spew out a lot of text without the context of what test printed that text.

#   If you would like to see print statements as they are executed, you can pass the -s flag to pytest:
#       pytest -s test_3_6_1.py

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
        element = driver.find_element_by_class_name('login')
        print("The text value of the element located by its login class is : '" + element.text + "'")
    except NoSuchElementException:
        print("The search box element was not found")
    driver.quit()

