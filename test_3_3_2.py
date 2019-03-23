# Section 3 exercise : Switching to iframes

import logging
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome()

def test_3_3_2():
    logging.debug("running test_3_3")
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
    driver.maximize_window()
    driver.switch_to.frame("iframeResult")
    onclick_button = driver.find_element_by_css_selector('[onclick*="myFunction()"]')
    onclick_button.click()
    time.sleep(2)
    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)
    driver.switch_to.default_content()
    assert "Tryit Editor" in driver.title
    driver.quit()