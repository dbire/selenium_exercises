import time
from selenium import webdriver

driver = webdriver.Chrome()

def open_page(url):
    driver.get(url)

def close_page():
    driver.quit()

def search_for(search_expression):
    driver.find_element_by_id("search_query_top").click()
    driver.find_element_by_id("search_query_top").clear()
    driver.find_element_by_id("search_query_top").send_keys(search_expression)
    driver.find_element_by_name("submit_search").click()

def add_to_cart():
    driver.find_element_by_xpath(
        "(.//*[normalize-space(text()) and normalize-space(.)='$30.51'])[2]/following::span[2]").click()

def test_app_dynamics_job():
    open_page("http://automationpractice.com/index.php")
    search_for("printed dress")
    time.sleep(5)
    add_to_cart()