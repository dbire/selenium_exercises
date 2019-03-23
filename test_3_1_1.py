# Section 3 Exercise: pytest html report

# pytest-html is a plugin for pytest that generates a HTML report for the test results:
#     pip install pytest-html


import logging
import time

logging.basicConfig(level=logging.DEBUG)

def test_3_3_1():
    logging.debug("running test_3_3_1")
    current_time = time.localtime()
    logging.info("current_time:" +
                 str(current_time.tm_mday) + "-" +
                 str(current_time.tm_mon)  + "-" +
                 str(current_time.tm_year) + " " +
                 str(current_time.tm_hour) + ":" +
                 str(current_time.tm_hour) + ":" +
                 str(current_time.tm_min)  + ":" +
                 str(current_time.tm_sec))
    assert current_time.tm_hour < 12

# pytest --html=report.html test_3_1_1.py