from selenium import webdriver

# Section 2 Exercise: XPath

def test_2_2_1():
    url='http://automationpractice.com/index.php'
    driver=webdriver.Chrome()
    driver.get(url)

    # 1. Search edit box
    xp='//div[@id="search_block_top"]/form/input[@id="search_query_top"]'
    search_edit_box=driver.find_element_by_xpath(xp)
    xp = '//*[@id="search_query_top"]'
    search_edit_box = driver.find_element_by_xpath(xp)


    # 2. Sign-in Link
    xp='//div[@class="header_user_info"]'
    sign_in_link=driver.find_element_by_xpath(xp)
    xp = '//a[contains(.,"Sign in")]'
    sign_in_link = driver.find_element_by_xpath(xp)

    # 3. product which title is "Faded Short Sleeve T-shirts"
    xp = '//a[@title="Faded Short Sleeve T-shirts"]'
    product = driver.find_element_by_xpath(xp)

    # 4. add to cart button for a product
    xp = '//ul[@id="homefeatured"]//a[contains(@href,"id_product=1&")]//span[contains(.,"Add to cart")]'
    add_to_cart_button_for_product_id_1 = driver.find_element_by_xpath(xp)