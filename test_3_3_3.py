# Section 3 exercise 3 : Two Browsers

import logging
import time
from selenium import webdriver

def test_3_3_3():
    logging.debug("Running test_3_3_3")
    br1 = webdriver.Chrome()
    br2 = webdriver.Chrome()

    # open Python 2 Functions Library page
    br1.get("https://docs.python.org/2/library/functions.html")

    # open Python 3 Functions Library page
    br2.get("https://docs.python.org/3/library/functions.html")
    br2.switch_to.window("")

    # Reload function should be found in Python 2
    elements = br1.find_elements_by_partial_link_text('reload')
    assert len(elements) > 0, "Reload function could not be found"

    # Reload function should not be found in Python 3
    elements = br2.find_elements_by_partial_link_text('reload')
    assert len(elements) == 0, "Reload function was found but not expected"
    br1.quit()
    br2.quit()