from selenium import webdriver
from utils import highlight

# Section 2 Exercise: CSS Selectors

url = 'http://automationpractice.com/index.php'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

def test_2_3_1():
    # 1. Search edit box
    css='#search_query_top'
    search_edit_box = driver.find_elements_by_css_selector(css)

    # 2. Sign-in Link
    css='a.login'
    sign_in_link = driver.find_elements_by_css_selector(css)

    # 3. product which title is "Faded Short Sleeve T-shirts"
    css = '[title="Faded Short Sleeve T-shirts"]'
    product = driver.find_elements_by_css_selector(css)

    css='ul#homefeatured div.product-image-container > a.product.img_link[href*="id_product=3&"]'
    product = driver.find_elements_by_css_selector(css)

    # 4. add to cart button for a product
    css = '[href*="product=1&token=e817bb0705dd58da8db074c69f729fd8"]'
    add_to_cart_button_for_product_id_1 = driver.find_elements_by_css_selector(css)

    css = 'ul#homefeatured a[data-id-product="3"] span'
    add_to_cart_button_for_product_id_1 = driver.find_elements_by_css_selector(css)