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

def add_to_cart_by_num(num):

    add_to_cart_buttons = driver.find_elements_by_xpath("//a[@title='Add to cart']")
    add_to_cart_buttons[num].click()

def test_4_4_2():
    open_page("http://automationpractice.com/index.php")
    search_for("printed dress")
    time.sleep(5)
    add_to_cart_by_num(0)