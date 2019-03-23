# Section 2 exercise : Navigation

import logging
from selenium import webdriver

driver = webdriver.Chrome()

def test_3_2_1():
    logging.debug("running test_3_2")
    driver.get("https://docs.python.org/")
    logging.info("URL: "  + driver.current_url)
    logging.info("Title:" + driver.title)
    assert "Documentation"in driver.title
    driver.quit()