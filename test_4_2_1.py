# Chapter 4 Section 2 exercise 1 : Working with Waits

import logging,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO)

driver = webdriver.Chrome()

def test_4_2_1():
    logging.debug("running test_3_8_1")
    driver.get("https://www.python.org")
    search_box = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'id-search-field')))
    search_box.clear()
    search_box.send_keys("comprehensions")
    time.sleep(2)
    go_button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'submit')))
    go_button.click()
    #time.sleep(2)
    results = driver.find_elements_by_xpath("//ul/li/h3/a")
    assert len(results) > 0, "No results found"
    for r in results:
        logging.info(r.text)
    driver.quit()