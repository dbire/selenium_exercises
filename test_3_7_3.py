# Section 7 exercise  3 : Modal Dialogs

import logging,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)

def test_3_7_3():
    url='http://automationpractice.com/index.php'
    driver.get(url)
    driver.maximize_window()

    driver.find_element_by_partial_link_text('Faded Short Sleeve T-shirts').click()
    driver.find_element_by_css_selector("#add_to_cart>button").click()
    modal=driver.find_element_by_id("layer_cart")
    proceed_to_checkout = WebDriverWait(modal,10).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Proceed to checkout']")))
    proceed_to_checkout.click()
    assert driver.title == "Order - My Store", "Checkout page is not open"
    time.sleep(10)
    driver.quit()