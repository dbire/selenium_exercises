# Section 3 exercise 4 : Screenshots

import os
import logging
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome()

def test_3_3_4():
    logging.debug("running test_3_3_4")
    path="./screenshots"
    if not(os.path.exists(path)):
        os.mkdir(path)

    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
    driver.save_screenshot(path + "/picture1.png")
    driver.maximize_window()
    driver.save_screenshot(path + "/picture2.png")
    driver.switch_to.frame("iframeResult")
    onclick_button = driver.find_element_by_css_selector('[onclick*="myFunction()"]')
    onclick_button.click()
    time.sleep(2)
    #It is not possible to take screenshot with the alert box using selenium
    # driver.save_screenshot(path + "/picture3.png")
    alert = driver.switch_to.alert
    alert.accept()
    driver.save_screenshot(path + "/picture4.png")
    driver.switch_to.default_content()
    driver.save_screenshot(path + "/picture5.png")
    assert "Tryit Editor" in driver.title
    driver.quit()