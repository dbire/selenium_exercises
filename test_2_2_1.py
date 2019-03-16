from selenium import webdriver
from selenium.webdriver import ActionChains

from utils import highlight

# Section 2 Exercise: XPath

url = 'http://automationpractice.com/index.php'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

def test_search_edit_box():
    xp='//div[@id="search_block_top"]/form/input[@id="search_query_top"]'
    search_edit_box=driver.find_element_by_xpath(xp)
    xp = '//*[@id="search_query_top"]'
    search_edit_box = driver.find_element_by_xpath(xp)
    highlight(search_edit_box)

def test_sign_in_link():
    xp='//div[@class="header_user_info"]'
    sign_in_link=driver.find_element_by_xpath(xp)
    xp = '//a[contains(.,"Sign in")]'
    sign_in_link = driver.find_element_by_xpath(xp)
    highlight(sign_in_link)

def test_product_faded_short_sleeve_tshirts():
    xp = '//a[@title="Faded Short Sleeve T-shirts"]'
    product = driver.find_element_by_xpath(xp)
    actions = ActionChains(driver)
    actions.move_to_element(product)
    actions.perform()
    highlight(product)

def test_add_to_cart_button_for_product_id_1():
    xp = '//ul[@id="homefeatured"]//a[contains(@href,"id_product=1&")]//span[contains(.,"Add to cart")]'
    add_to_cart_button_for_product_id_1 = driver.find_element_by_xpath(xp)
    actions = ActionChains(driver)
    actions.move_to_element(add_to_cart_button_for_product_id_1)
    actions.perform()
    highlight(add_to_cart_button_for_product_id_1)