# Section 7 exercise 2 : Using Dropdown list

import logging,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

def test_3_7_2():
    url='http://automationpractice.com/index.php?controller=prices-drop'
    driver.get(url)

    sort_by_drop_down = driver.find_element_by_id('selectProductSort')
    sort_by_drop_down.click()

    in_stock_option_xpath="//*[@value='quantity:desc']"
    in_stock_option = driver.find_element_by_xpath(in_stock_option_xpath)
    in_stock_option.click()
    time.sleep(5)

    assert "orderby=quantity" in driver.current_url, "Incorrect page opened"
    driver.quit()