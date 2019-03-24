# Section 8 exercise : Working with Alerts

import logging
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome()

def test_3_8_1():
    logging.debug("running test_3_8_1")
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
    driver.switch_to.frame("iframeResult")
    onclick_button = driver.find_element_by_css_selector('[onclick*="myFunction()"]')
    onclick_button.click()
    time.sleep(2)
    alert = driver.switch_to.alert
    assert "Hello!" in alert.text, 'Incorrect text in Alert'
    alert.accept()
    time.sleep(2)
    driver.quit()