from selenium import webdriver

# to install selenium webdriver :
#  pip install selenium

# to install pytest :
#  pip install -U pytest

# to execute the test using pytest:
#  pytest test_2-1-1.py

def test_2_1_1():
    url='https://www.python.org'
    driver=webdriver.Chrome()
    driver.get(url)