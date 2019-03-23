# Section 7 exercise 1 : Clicking on WebElement

import logging,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

def test_3_7_1():
    url='http://automationpractice.com/index.php'
    driver.get(url)
    sign_in_link = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME,'login')))
    sign_in_link.click()
    time.sleep(5)
    logging.info("The current page URL is : " + driver.current_url)
    assert "authentication" in driver.current_url, "Incorrect page opened"
    driver.quit()