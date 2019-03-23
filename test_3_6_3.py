# Section 6 exercise 3 : Get selected state of a checkbox

#   By default, py.test captures the result of standard out so that it can control how it prints it out. *
#   If it didn't do this, it would spew out a lot of text without the context of what test printed that text.

#   If you would like to see print statements as they are executed, you can pass the -s flag to pytest:
#       pytest -s test_3_6_3.py

import os
import logging
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome()

def test_3_6_3():
    logging.debug("Running test_3_6_3")

    url = 'http://automationpractice.com/index.php?id_category=8&controller=category#/categories-casual_dresses/compositions-cotton'
    driver.get(url)
    size_small_checkbox = driver.find_element_by_id('layered_id_attribute_group_1')
    size_small_checkbox_state=size_small_checkbox.is_selected()
    print("The size_small_checkbox element selected state is : '" + str(size_small_checkbox_state) + "'")
    print("Now click the Size S checkbox")
    time.sleep(10)
    size_small_checkbox = driver.find_element_by_id('layered_id_attribute_group_1')
    size_small_checkbox_state = size_small_checkbox.is_selected()
    print("The size_small_checkbox element selected state is : '" + str(size_small_checkbox_state) + "'")
    driver.quit()